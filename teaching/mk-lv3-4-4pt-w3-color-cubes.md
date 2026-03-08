---
title: "MK LV3-4 (4-Pointer): Color Cubes"
parent: Teaching
nav_order: 22
---

# MK LV3-4 (4-Pointer): Color Cubes
{: .no_toc }

Counting painted faces on 3-D cube arrangements from the MK 4-Pointers LV3-4 Week 3 workbook (Day 3).
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Strategy 1: Counting Painted Faces — The Subtraction Method

When a group of unit cubes is assembled and the **outside** of the structure is painted, the number of painted faces depends on how many cube faces are hidden (shared between adjacent cubes) and whether the **bottom** is painted.

**Starting point:** Each isolated cube has **6 faces**.

**For every pair of cubes that touch**, **2 faces become hidden** (one from each cube).

```
Painted faces = 6n − 2 × (number of shared internal faces) − (bottom faces, if unpainted)
```

Where **n** = total number of unit cubes.

{: .highlight }
> **Shortcut for a row of cubes (not painted on bottom):**
> A row of n cubes has painted faces = 4n + 2. (Top + 3 sides per cube + the two end faces.)

---

## Strategy 2: Layer-by-Layer Analysis

For more complex 3-D arrangements, analyse each layer separately:

1. **Draw or visualise the top view** — count cubes in each layer.
2. For each cube, count how many of its **6 faces** are exposed (not touching another cube or the ground).
3. If the problem says "**painted on all sides except the bottom**", the bottom layer loses its bottom faces.
4. Sum across all cubes.

**Exposed-face checklist for each cube:**

| Face | Hidden when… |
|------|-------------|
| Top | A cube sits directly above it |
| Bottom | A cube sits directly below it, OR it is a ground-level bottom face (if bottom is not painted) |
| Front | A cube is directly in front |
| Back | A cube is directly behind |
| Left | A cube is directly to the left |
| Right | A cube is directly to the right |

---

## Strategy 3: By-Position Classification

For arrangements with a recognisable pattern, classify cubes by how many neighbours they have:

| Position | Neighbours | Exposed side faces | Notes |
|----------|-----------|-------------------|-------|
| Corner cube (3-D corner) | 3 | 3 | |
| Edge cube (on an edge, not corner) | 4 | 2 | |
| Face cube (on a face, not edge) | 5 | 1 | |
| Interior cube | 6 | 0 | Completely hidden |

Add top/bottom faces separately based on the layer.

---

## Worked Examples

### Example A — Single Staircase (3 cubes: 1 high, 2 high, 3 high)

Three columns of cubes arranged as a staircase (heights 1, 2, 3) viewed from the front. Total cubes = 1 + 2 + 3 = 6. Painted on all exposed surfaces (bottom row's bottoms are **not** painted).

**Approach:**

```
Isolated faces = 6 × 6 = 36
Shared faces:
  Column 1–2 share: 1 pair (the faces where col 1 touches col 2 at ground level)
  Column 2–3 share: 2 pairs (two heights of contact)
  Vertically stacked cubes within each column: 1 shared pair in col 2, 2 shared pairs in col 3
Total internal shared pairs = 1 + 2 + 1 + 2 = 6
Bottom faces (ground level, not painted) = 3 (one per column base)

Painted = 36 − 2×6 − 3 = 36 − 12 − 3 = 21
```

---

### Example B — L-Shaped Arrangement

5 cubes form an L-shape in a single layer. Painted on all sides **including** the bottom.

```
Isolated faces = 6 × 5 = 30
Shared pairs = 4  (the 4 joints in an L of 5 cubes)
Bottom painted → no subtraction

Painted = 30 − 2×4 = 22
```

---

### Example C — 2×2×2 Cube (8 small cubes)

```
Isolated faces = 6 × 8 = 48
Shared pairs:
  Bottom layer: 2 side-by-side pairs in a row × 2 rows = 4, plus the two rows touching each other = 2 → 4 + 2 = ...
  Better to count directly:
  4 cubes on bottom: 4 internal shared pairs
  4 cubes on top: 4 internal shared pairs
  Bottom-to-top shared: 4 pairs
  Total = 4 + 4 + 4 = 12 pairs

Painted = 48 − 2×12 = 48 − 24 = 24 ✓
(A 2×2×2 cube has 6 faces × 2² = 24 painted unit squares — matches!)
```

---

## General Tips for Color Cube Problems

1. **Count cubes first.** Mis-counting cubes is the most common error — recount from the diagram.
2. **Find all shared (internal) faces.** Every place two cubes touch contributes **2 hidden faces** (one from each cube).
3. **Check the bottom rule.** If bottom faces are not painted, subtract one per ground-level cube.
4. **Use the formula:** `Painted = 6n − 2×(shared pairs) − (unpainted bottoms)`
5. **Layer-by-layer** is safest for irregular 3-D shapes — do each layer separately and sum.
6. **Sanity check:** For a rectangular block of dimensions L×W×H, painted area = 2(LW + WH + LH) unit squares — a quick verification tool.
