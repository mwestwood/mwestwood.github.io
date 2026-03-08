---
title: "MK LV3-4 (5-Pointer): Picture Reasoning"
parent: Teaching
nav_order: 2
---

# MK LV3-4 (5-Pointer): Picture Reasoning
{: .no_toc }

Combination and placement constraint puzzles from the MK 5-Pointers LV3-4 Logical Reasoning workbook.
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Strategy: Combination Constraints

In these problems, you have groups of items and a limited set of labels (toppings, colors, etc.). The key rule is: **no two items of the same type can share the same label**. This means each type must "use up" different labels, and you can track what's left for other types.

**Steps:**
1. List each item type and how many there are.
2. List each label type and how many there are.
3. Note the rule: same-type items must have different labels.
4. Assign labels to the largest group first — they'll use the most variety.
5. See what remains for smaller groups and determine what's impossible.

---

### Problem 1 — Cupcake Toppings

Six people each order one cupcake: **2 mint-chocolate, 3 chocolate, 1 cream**. Toppings available: **1 cherry, 2 marshmallows, 3 chocolate chips**. One topping per cupcake; no two cupcakes of the same flavor get the same topping.

Which combination is **not** possible?

- A. Mint-chocolate with a chocolate chip
- B. Chocolate with a cherry
- C. Chocolate with a chocolate chip
- D. Cream with a cherry
- E. Mint-chocolate with a marshmallow

**Answer: D**

**Step-by-step solution:**

Step 1 — Handle the largest group first (3 chocolate cupcakes). They all have the same flavor, so they need 3 **different** toppings. There are exactly 3 topping types, so each chocolate cupcake gets one of each: 1 cherry, 1 marshmallow, 1 chocolate chip.

Step 2 — What's left for the 2 mint-chocolate cupcakes? After the chocolate group claims 1 cherry, 1 marshmallow, 1 chocolate chip, the remaining toppings are: **1 marshmallow + 2 chocolate chips**. The 2 mint-chocolate cupcakes must differ from each other, so they take 1 marshmallow and 1 chocolate chip.

Step 3 — What's left for the 1 cream cupcake? The only topping remaining is **1 chocolate chip**.

Step 4 — Check each answer:
- Cherry was fully used by the chocolate group. No cream cupcake can get a cherry. → **D is impossible** ✓
- A, C, E are all covered by the assignments above. B is covered by the chocolate group's assignment.

---

### Problem 2 — Ice Cream Toppings

Seven people each order one scoop: **4 vanilla, 2 chocolate, 1 lemon**. Toppings: **3 marshmallows, 2 cherries, 1 waffle, 1 chocolate chip**. One topping per scoop; no two of the same flavor get the same topping.

Which combination is **not** possible?

- A. Vanilla with a chocolate chip
- B. Chocolate with a cherry
- C. Chocolate with a marshmallow
- D. Vanilla with a waffle
- E. Lemon with a cherry

**Answer: E**

**Step-by-step solution:**

Step 1 — Handle the largest group (4 vanilla scoops). They need 4 different toppings. There are exactly 4 topping types, so each vanilla scoop claims one of each: 1 marshmallow, 1 cherry, 1 waffle, 1 chocolate chip.

Step 2 — Remaining toppings for the 2 chocolate scoops: **2 marshmallows + 1 cherry**. The 2 chocolate scoops must differ, so they take 1 marshmallow and 1 cherry.

Step 3 — Remaining for the 1 lemon scoop: **1 marshmallow**.

Step 4 — The lemon scoop can only get a marshmallow. A cherry combination with lemon is impossible. → **E is impossible** ✓

---

## Strategy: Color/Adjacent-Difference Constraints

In these problems, shapes share edges and must satisfy a rule: **adjacent shapes must be different**. Work from the **known** values outward, eliminating options at each step.

**Steps:**
1. Map out which positions are adjacent.
2. Start from known colors and mark what each neighbor cannot be.
3. If only one color remains for a position, fill it in.
4. Check if any position is still ambiguous; if so, see what the question specifically asks about.

---

### Problem 3 — Triangle Coloring

Terry has 9 small triangles: **3 red (R), 3 yellow (Y), 3 blue (B)**. He builds a big triangle where any two triangles sharing an edge must be different colors. He has placed:

- Top: **R**
- Row 2 (left→right): position 2, position 1, **Y**
- Row 3 (left→right): **B**, position 3, **B**, position 4, position 5

Which statement is true?

- A. 1 and 3 are blue
- B. 1 is blue and 5 is yellow
- C. 1 and 3 are yellow
- D. 2 and 4 can only be red
- E. 4 is blue and 5 is yellow

**Answer: B**

**Step-by-step solution:**

Step 1 — Find position 1's color. Position 1 (center of row 2, inverted triangle) is adjacent to **R** (above) and **Y** (right). It cannot be R or Y. → **Position 1 = B**

Step 2 — Find position 4's color. Position 4 (inverted, row 3) is adjacent to the second **B** on its left and **Y** above. It cannot be B or Y. → **Position 4 = R**

Step 3 — Count the blues used so far. Known blues: row3-left B, row3-middle B, position 1. That is all **3 blue** pieces used up.

Step 4 — Find position 5's color. Position 5 is only adjacent to position 4 (= R). Position 5 cannot be R, and cannot be B (all 3 used). → **Position 5 = Y**

Step 5 — What remains for positions 2 and 3? We have used 2R (top, position 4) and 1Y (row2-right) and 3B. Remaining: 1R, 2Y for positions 2 and 3. Both (2=R, 3=Y) and (2=Y, 3=R) satisfy the adjacency rules — so 2 and 3 are **not** uniquely determined. Answer D is false.

Step 6 — Check each answer against confirmed values (1=B, 5=Y):
- A: 3 cannot be blue (all blues used). ✗
- **B: 1=B ✓, 5=Y ✓** ← correct
- C: 1=B, not yellow. ✗
- D: Position 2 can be R or Y. ✗
- E: Position 4=R, not blue. ✗

---

## Strategy: Linear Placement Constraints

In these problems, stickers (or items) are placed on a row of numbered squares. Clues give you fixed positions, exclusions, and adjacency requirements. Use **process of elimination** to pin down each item's position.

**Steps:**
1. Note any item with a fixed position — place it immediately.
2. Apply exclusion clues (e.g., "not on square 3") to narrow down options.
3. Use adjacency clues ("next to X and Y") — find the only position where both neighbors can be satisfied.
4. Fill in the remaining item by elimination.

---

### Problem 4 — Dinosaur Stickers

Jack places 5 dinosaur stickers on squares 1–5. Clues:
- The **green dinosaur** is not on square 3.
- The **pink dinosaur** is on square 4.
- The **blue spiky dinosaur** is next to both the **triceratops** and the **long-neck dinosaur**.

On which square is the **blue spiky dinosaur**?

- A. 1 &nbsp; B. 2 &nbsp; C. 3 &nbsp; D. 4 &nbsp; E. 5

**Answer: B (square 2)**

**Step-by-step solution:**

Step 1 — Fix the known position: **pink = square 4**.

Step 2 — The blue spiky dinosaur must be adjacent to **two** different stickers (triceratops and long-neck). On a 5-square row, only squares 2, 3, and 4 have two neighbors. Square 4 is taken (pink), so blue spiky is on square 2 or 3.

Step 3 — If blue spiky = square 3, its neighbors are squares 2 and 4. Square 4 = pink, which is neither triceratops nor long-neck. Contradiction. → Blue spiky ≠ square 3.

Step 4 — Therefore **blue spiky = square 2**. Its neighbors are squares 1 and 3, which hold the triceratops and long-neck (in either order).

Step 5 — The green dinosaur is not on square 3. The remaining square for the green dinosaur must be square 5 (squares 1, 2, 3 are taken by triceratops/long-neck/blue-spiky, square 4 = pink). This is consistent.

---

### Problem 5 — Fruit Stickers

Ketty places 5 fruit stickers (apple, grapes, watermelon, orange, blueberries) on squares 1–5. Clues:
- **Grapes** are not on square 1 or 5.
- **Watermelon** is on square 2.
- **Orange** is next to **blueberries**.

On which square is the **apple**?

- A. 1 &nbsp; B. 2 &nbsp; C. 3 &nbsp; D. 4 &nbsp; E. 5

**Answer: A (square 1)**

**Step-by-step solution:**

Step 1 — Fix the known position: **watermelon = square 2**.

Step 2 — Grapes cannot be on 1, 2, or 5. So **grapes = square 3 or 4**.

Step 3 — Orange must be adjacent to blueberries. The remaining squares for orange, blueberries, apple, and grapes are 1, 3, 4, 5.

Step 4 — Try **grapes = square 4**. Then orange and blueberries must be placed in {1, 3, 5}. Check for adjacent pairs: squares 1 & 3 are not adjacent (watermelon is between them at sq 2, but sq 1 and sq 3 are not neighbors in the linear sense — they are 2 apart). Squares 3 & 5 are also not adjacent (sq 4 = grapes between them). Squares 1 & 5 are not adjacent. No adjacent pair available. → Grapes ≠ square 4.

Step 5 — Try **grapes = square 3**. Then orange and blueberries occupy 2 of {1, 4, 5}, and apple gets the remaining one. Adjacent pairs in {1, 4, 5}: squares 4 & 5 are adjacent. So orange = 4 and blueberries = 5 (or vice versa), and **apple = square 1** ✓.

Step 6 — Verify no constraint is violated: grapes=3 (not 1 or 5 ✓), watermelon=2 ✓, orange(4) next to blueberries(5) ✓. All good.

---

## Answer Key

| Problem | Answer |
|:--------|:------:|
| 1. Cupcake toppings | D |
| 2. Ice cream toppings | E |
| 3. Triangle coloring | B |
| 4. Dinosaur stickers | B |
| 5. Fruit stickers | A |
