# WH Question Quest — scene photos

Real-world setting photos shown above questions in `/autism/wh-quest/` to
build picture comprehension across different settings.

Sources and licenses:

- Images fetched via the Openverse API filtered to **CC0 / Public Domain
  Mark** licenses, or from **Wikimedia Commons** (free licenses; see
  `credits.json` for per-file attribution where recorded).
- All resized to ≤640px wide with `sips`.

To add a scene: drop a `<key>.jpg` here and register it in `SCENE_IMAGES`
in `_tools/wh_data.py`, then re-run `_tools/build-wh-quest.py`.
