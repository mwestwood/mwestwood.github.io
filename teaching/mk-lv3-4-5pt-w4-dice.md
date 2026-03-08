---
title: "MK LV3-4 (5-Pointer): Dice"
parent: Teaching
nav_order: 14
---

# MK LV3-4 (5-Pointer): Dice
{: .no_toc }

Cube net and dice face puzzles from the MK 5-Pointers LV3-4 Week 4 workbook.
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Strategy 1: Cube Nets — Which Nets Fold into a Cube?

A **net** of a cube is a flat arrangement of 6 squares that can be folded into a cube. Not every arrangement of 6 squares is a valid net.

**There are exactly 11 valid nets for a cube.** Learn to spot the invalid ones:

**Invalid patterns (cannot fold into a cube):**
- A row of **4 or more** squares in a straight line with extra squares attached is usually invalid if the extra squares create a collision.
- A **2×3 rectangle** (6 squares in a 2×3 grid) is **not** a valid net.
- Any pattern where two squares would end up on the same face when folded.

**Checking a net:**
1. Pick any square as the **bottom**.
2. Fold up adjacent squares as **front, right, back, left**.
3. The remaining square should become the **top** — check it doesn't collide with another face.

{: .note }
> **Quick test:** The 11 valid nets all include a "column" of 4 squares (the four sides), with the top and bottom square attached somewhere along that column. If you can't find this structure, the net is likely invalid.

---

### Problem 1 — Which Net is Valid?

Four arrangements of 6 squares are shown (A, B, C, D, E). Which one **can** be folded into a cube?

**Answer:** Use the folding test for each option.

**Common valid nets:**

```
Cross shape (most recognisable):
    [T]
[L][B][R][K]     T=top, B=bottom, L=left, R=right, K=back, Fr=front
    [Fr]
```

```
T-shape variant:
[T][B][Fr]
      [R]
      [K]
      [L]
```

**Step-by-step strategy:**
1. Label one central square as the bottom (B).
2. The four squares adjacent to B become the four side faces.
3. The remaining square must be opposite to B (becomes the top) — it must not overlap any side face.

---

### Problem 2 — Opposite Faces of a Standard Die

On a standard die, **opposite faces always sum to 7**:
- **1 is opposite 6**
- **2 is opposite 5**
- **3 is opposite 4**

A die is shown with 2 on the front, 3 on the top, and 6 on the right. What number is on the **bottom**?

- A. 1 &nbsp;&nbsp; **B. 4** &nbsp;&nbsp; C. 5 &nbsp;&nbsp; D. 6 &nbsp;&nbsp; E. 2

**Answer: B — 4**

**Step-by-step solution:**

Top = 3 → **Bottom = 4** (opposite faces sum to 7: 3 + 4 = 7).

---

### Problem 3 — Reading a Cube Net

The net below has letters/numbers on each face. When folded, which face is **opposite** to the face labelled **A**?

```
Net layout (each cell is a face):
      [  ]
[  ][A ][  ][  ]
      [  ]
      [  ]
```

**Strategy:**
1. The central row of 4 squares forms the four "side" faces when the top and bottom squares fold up.
2. The square **two positions away** in the central row is opposite to the square at the other end of the row.
3. The two squares branching off (above/below) form the top/bottom pair.

**General rule for a cross-shaped net:**

| Position | Opposite |
|----------|----------|
| Left end of row | Right-of-centre in row |
| Top branch | Bottom branch |
| etc. | depends on net layout |

*Always trace the folding manually using the net provided in the workbook.*

---

## Strategy 2: Visualising a Die's Orientation

When a die is **rolled** or **rotated**, track which face ends up where by using the opposite-face rule and a systematic rotation.

**Rotation rules:**
- Rolling **forward** (away from you): top → front, front → bottom, bottom → back, back → top. Left and right unchanged.
- Rolling **right**: top → right, right → bottom, bottom → left, left → top. Front and back unchanged.
- Rolling **left**: reverse of rolling right.
- Rotating **clockwise** (viewed from top): front → right, right → back, back → left, left → front. Top and bottom unchanged.

---

### Problem 4 — Tracking a Rolling Die

A standard die starts with **1 on top, 2 facing you**. It is rolled forward twice, then rolled right once. What number is now on **top**?

**Step-by-step solution:**

Initial state: Top=1, Front=2, Right=?, Bottom=6, Back=5, Left=?

Standard die orientation (right-hand): with 1 on top and 2 facing you, 3 is on the right.
So: Top=1, Front=2, Right=3, Bottom=6, Back=5, Left=4.

**Roll forward (1st):** top→front, front→bottom, bottom→back, back→top.
- Top=5, Front=1, Right=3, Bottom=2, Back=6, Left=4

**Roll forward (2nd):**
- Top=6, Front=5, Right=3, Bottom=1, Back=2, Left=4

**Roll right:** top→right, right→bottom, bottom→left, left→top.
- Top=4, Front=5, Right=6, Bottom=3, Back=2, Left=1

**Top = 4**

---

### Problem 5 — Which Die Matches the Net?

A cube net is shown with numbers placed on specific squares. Four dice are shown from different angles. Which die could have been folded from this net?

**Step-by-step strategy:**
1. From the net, identify which number is opposite which.
2. For each die option, check if the visible faces are consistent with those opposite-face pairings.
3. Eliminate any die where visible faces show numbers that should be opposite each other (both faces of an opposite pair cannot be visible at once).

**Opposite-pair check:**
- If the net shows 1 opposite 4, then no valid die can show **both** 1 and 4 visible at the same time.

{: .highlight }
> **Quick elimination:** For each answer option, list the three visible faces. If any two visible faces are opposite pairs in the given net, that option is **immediately invalid**.

---

### General Tips for Dice Problems

1. **Memorise standard die opposites:** 1↔6, 2↔5, 3↔4 (sums to 7).
2. **Three faces meet at each corner** of a die — use corner-triples to verify orientation.
3. **On a standard die,** the 1, 2, and 3 faces share a single vertex, arranged counter-clockwise when viewed from that corner.
4. **When given a net,** determine opposite pairs before trying to answer any question.
5. **For rolling problems,** track all six faces through each rotation step by step.
