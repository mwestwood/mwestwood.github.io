#!/usr/bin/env ruby
# encrypt-batch.rb — Ruby port of encrypt-batch.js
# Uses PBKDF2-SHA256 + AES-256-GCM matching the JS implementation exactly.
# Blob layout: salt[16] + iv[12] + ciphertext (same as encrypt-batch.js)
#
# Usage: ruby _tools/encrypt-batch.rb <passphrase> <directory>

require 'openssl'
require 'base64'
require 'fileutils'

passphrase = ARGV[0]
target_dir = ARGV[1]

if passphrase.nil? || target_dir.nil?
  warn 'Usage: ruby _tools/encrypt-batch.rb <passphrase> <directory>'
  exit 1
end

unless Dir.exist?(target_dir)
  warn "Directory not found: #{target_dir}"
  exit 1
end

# ── Crypto ──────────────────────────────────────────────────────────────────

def encrypt_content(passphrase, plaintext)
  salt = OpenSSL::Random.random_bytes(16)
  iv   = OpenSSL::Random.random_bytes(12)

  key = OpenSSL::PKCS5.pbkdf2_hmac(
    passphrase,
    salt,
    100_000,
    32,          # 256-bit key
    'SHA256'
  )

  cipher = OpenSSL::Cipher.new('aes-256-gcm')
  cipher.encrypt
  cipher.key = key
  cipher.iv  = iv

  ciphertext = cipher.update(plaintext.encode('UTF-8')) + cipher.final
  tag        = cipher.auth_tag   # 16-byte GCM authentication tag (matches Web Crypto)

  blob = salt + iv + ciphertext + tag
  Base64.strict_encode64(blob)
end

# ── Front-matter helpers ─────────────────────────────────────────────────────

def split_front_matter(content)
  m = content.match(/\A---\r?\n(.*?)\r?\n---\r?\n?(.*)\z/m)
  return [{}, content] unless m

  fields = {}
  m[1].each_line do |line|
    kv = line.match(/^([a-zA-Z_][\w-]*)\s*:\s*(.*)$/)
    next unless kv
    fields[kv[1]] = kv[2].strip.gsub(/\A["']|["']\z/, '')
  end
  [fields, m[2]]
end

NEEDS_QUOTES_RE = /[:#"']/

def needs_quotes?(val)
  val.is_a?(String) && (
    val.match?(NEEDS_QUOTES_RE) ||
    val.start_with?(' ') ||
    val.end_with?(' ') ||
    val.empty? ||
    val.length > 200
  )
end

def build_front_matter(fields)
  lines = ['---']
  fields.each do |k, v|
    next if v.nil?
    s = v.to_s
    lines << (needs_quotes?(s) ? "#{k}: \"#{s.gsub('"', '\\"')}\"" : "#{k}: #{s}")
  end
  lines << '---'
  lines.join("\n") + "\n"
end

# ── Markdown cleaner ─────────────────────────────────────────────────────────

def clean_markdown(md)
  md
    .gsub(/^## Table of contents[\s\S]*?^---$/m, '---')  # remove TOC section
    .gsub(/^\{:.*?\}\s*$/m, '')                           # remove Kramdown attribute lines
    .gsub(/\{%[^%]*%\}/, '')                              # remove Liquid tags
    .gsub(/\n{3,}/, "\n\n")                               # collapse blank lines
    .strip
end

# ── Process files ────────────────────────────────────────────────────────────

files = Dir.glob(File.join(target_dir, '*.md')).sort

if files.empty?
  warn "No .md files found in #{target_dir}"
  exit 1
end

puts "\n🔐  Encrypting #{files.length} files in #{File.basename(target_dir)}/\n\n"

files.each do |file_path|
  raw = File.read(file_path, encoding: 'UTF-8')
  fields, body = split_front_matter(raw)

  clean_body = clean_markdown(body)
  if clean_body.empty?
    puts "  ⚠  Skipping #{File.basename(file_path)} — empty body"
    next
  end

  blob = encrypt_content(passphrase, clean_body)

  new_fields = {}
  new_fields['layout']       = 'protected'
  new_fields['title']        = fields['title']       if fields['title']
  new_fields['parent']       = fields['parent']      if fields['parent']
  new_fields['nav_order']    = fields['nav_order']   if fields['nav_order']
  new_fields['has_children'] = fields['has_children'] if fields['has_children']
  new_fields['permalink']    = fields['permalink']   if fields['permalink']
  new_fields['encrypted']    = blob

  File.write(file_path, build_front_matter(new_fields), encoding: 'UTF-8')
  puts "  ✓  #{File.basename(file_path)}"
end

puts "\n✅  Done — #{files.length} files encrypted.\n"
