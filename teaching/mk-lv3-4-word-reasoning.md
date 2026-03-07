---
title: "MK LV3-4: Word Reasoning"
parent: Teaching
nav_order: 3
---

# MK LV3-4: Word Reasoning
{: .no_toc }

Two logic puzzle types from the MK 5-Pointers LV3-4 Logical Reasoning workbook: "exactly one correct" code-breaking, and truth-or-lie deduction.
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Strategy 1: "Exactly One Correct" Code-Breaking

You are given several guesses at a code (name, password, or ordered list). Each guess has **exactly one item that is correct in both value and position**. Your job is to find the true code.

**Steps:**
1. Take any two guesses that share one item in the same position and differ everywhere else. If that shared item is the correct one, both guesses have it right — check that no other position in either guess overlaps with the answer.
2. Alternatively, test each answer choice by verifying it produces exactly one match against every guess.
3. Eliminate choices that produce 0 or 2+ matches against any guess.

{: .note }
> **Key insight:** If two guesses share a position with the same value and that position is correct, then all other positions in both guesses must be wrong. Use this to rule out other items.

---

### Problem 1 — Three-Part Name

You meet a character and ask three times:
1. "Are you **Jason Dylan Mark**?"
2. "Are you **Martin Dylan Pumpkin**?"
3. "Are you **Jason Max Pumpkin**?"

Each time, exactly one name and its position are correct. What is the character's name?

- A. Jason Dylan Mark
- B. Martin Max Pumpkin
- C. Martin Max Mark
- D. Jason Max Pumpkin
- E. Martin Dylan Mark

**Answer: C (Martin Max Mark)**

**Step-by-step solution:**

Step 1 — Guesses 1 and 2 both have **Dylan** at position 2. If Dylan-at-2 is the one correct item in each guess, then everything else in both guesses is wrong: Jason(1), Mark(3), Martin(1), Pumpkin(3) are all wrong. The answer would have some other name at positions 1 and 3.

Step 2 — Now check guess 3 (Jason Max Pumpkin). Jason is wrong (from Step 1). Pumpkin is wrong (from Step 1). So the one correct item in guess 3 must be **Max at position 2**. But we said Dylan is at position 2. Contradiction — Dylan and Max cannot both be at position 2.

Step 3 — Therefore, Dylan-at-2 is NOT the correct item. This means in guess 1, exactly one of {Jason(1), Mark(3)} is correct. And in guess 2, exactly one of {Martin(1), Pumpkin(3)} is correct.

Step 4 — Compare guesses 1 and 3 at position 1: both have **Jason**. If Jason(1) were correct, it would count as the one match in both guesses 1 and 3. For guess 3, that uses up the one match — so Max(2) and Pumpkin(3) would be wrong. Check guess 2: if Jason is wrong (already established it's not position 1 now... wait, we said Jason at position 1 is the one match). For guess 2, Jason is not present at position 1, so guess 2's match must be elsewhere: Martin(1) or Dylan(2) or Pumpkin(3). Since Jason(1) is correct, Martin(1) is wrong, Dylan(2) is wrong (position 2 in the answer is not Dylan since Jason used up one match and Pumpkin-wrong means position 3 is not Pumpkin). So guess 2's match must be one of {Martin(1)=wrong, Dylan(2), Pumpkin(3)=wrong}. Only Dylan(2) remains as a candidate match for guess 2. But then the answer has Dylan at position 2.

Step 5 — Test answer C (Martin, Max, Mark):
- vs guess 1 (Jason, Dylan, Mark): Jason≠Martin ✗, Dylan≠Max ✗, **Mark=Mark ✓** → 1 match ✓
- vs guess 2 (Martin, Dylan, Pumpkin): **Martin=Martin ✓**, Dylan≠Max ✗, Pumpkin≠Mark ✗ → 1 match ✓
- vs guess 3 (Jason, Max, Pumpkin): Jason≠Martin ✗, **Max=Max ✓**, Pumpkin≠Mark ✗ → 1 match ✓

All three guesses check out. **Answer: C** ✓

---

### Problem 2 — Book Order

You ask Victoria three times about 3 books she wants on the shelf:
1. "Math, Chinese, English?"
2. "Latin, Spanish, English?"
3. "Latin, Chinese, Science?"

Each time, exactly one book and its position are correct. What is the true order?

- A. Math, Chinese, Science
- B. Math, Chinese, English
- C. Latin, Chinese, English
- D. Math, Spanish, Science
- E. Latin, Spanish, English

**Answer: D (Math, Spanish, Science)**

**Step-by-step solution:**

Step 1 — Test answer D (Math, Spanish, Science):
- vs guess 1 (Math, Chinese, English): **Math=Math(1) ✓**, Chinese≠Spanish ✗, English≠Science ✗ → 1 match ✓
- vs guess 2 (Latin, Spanish, English): Latin≠Math ✗, **Spanish=Spanish(2) ✓**, English≠Science ✗ → 1 match ✓
- vs guess 3 (Latin, Chinese, Science): Latin≠Math ✗, Chinese≠Spanish ✗, **Science=Science(3) ✓** → 1 match ✓

Every guess gives exactly 1 match. **Answer: D** ✓

{: .highlight }
> **Pattern:** Answer D gets exactly one different position correct from each guess — the matches "rotate" across positions 1, 2, 3 across the three guesses.

---

### Problem 3 — Dress Order

You ask Zoe three times about 3 dresses for the wardrobe:
1. "Black, green, blue?"
2. "Yellow, red, blue?"
3. "Yellow, green, pink?"

Each time, exactly one dress and its position are correct. What is the true order?

- A. Black, red, pink
- B. Black, green, pink
- C. Black, red, blue
- D. Yellow, red, blue
- E. Yellow, green, pink

**Answer: A (Black, red, pink)**

**Step-by-step solution:**

Step 1 — Test answer A (Black, red, pink):
- vs guess 1 (Black, green, blue): **Black=Black(1) ✓**, green≠red ✗, blue≠pink ✗ → 1 match ✓
- vs guess 2 (Yellow, red, blue): Yellow≠Black ✗, **Red=Red(2) ✓**, blue≠pink ✗ → 1 match ✓
- vs guess 3 (Yellow, green, pink): Yellow≠Black ✗, green≠red ✗, **Pink=Pink(3) ✓** → 1 match ✓

**Answer: A** ✓

---

### Problem 4 — Five-Digit Lock Password

Thomas forgot his lock password (5 digits). Family members guess:
1. 3-2-1-5-4
2. 3-7-6-5-4
3. 4-7-1-5-4
4. 3-7-1-9-4
5. 3-7-1-5-8

Each time, exactly one digit and its position are correct. What is the password?

- A. 47198 &nbsp; B. 42698 &nbsp; C. 37194 &nbsp; D. 32658 &nbsp; E. 37198

**Answer: B (42698)**

**Step-by-step solution:**

Step 1 — Note that guesses 2–5 all share **3 at position 1** and **7 at position 2**. These repeated digits are strong suspects, but they can't both be correct in the same guess. Let's test answer B (4-2-6-9-8) against all guesses:

- vs guess 1 (3,2,1,5,4): 3≠4, **2=2(pos 2)✓**, 1≠6, 5≠9, 4≠8 → 1 match ✓
- vs guess 2 (3,7,6,5,4): 3≠4, 7≠2, **6=6(pos 3)✓**, 5≠9, 4≠8 → 1 match ✓
- vs guess 3 (4,7,1,5,4): **4=4(pos 1)✓**, 7≠2, 1≠6, 5≠9, 4≠8 → 1 match ✓
- vs guess 4 (3,7,1,9,4): 3≠4, 7≠2, 1≠6, **9=9(pos 4)✓**, 4≠8 → 1 match ✓
- vs guess 5 (3,7,1,5,8): 3≠4, 7≠2, 1≠6, 5≠9, **8=8(pos 5)✓** → 1 match ✓

Every guess yields exactly 1 match. **Answer: B** ✓

---

### Problem 5 — Five-Letter Lock Password

Jane forgot her lock code (5 letters). Family members guess:
1. A-D-G-R-T
2. A-C-G-H-T
3. A-C-E-R-T
4. A-C-G-R-M
5. B-C-G-R-T

Each time, exactly one letter and its position are correct. What is the password?

- A. BDGHT &nbsp; B. BDEHM &nbsp; C. ACERM &nbsp; D. ADEHT &nbsp; E. ADGRM

**Answer: B (BDEHM)**

**Step-by-step solution:**

Step 1 — Test answer B (B-D-E-H-M) against all guesses:

- vs guess 1 (A,D,G,R,T): A≠B, **D=D(2)✓**, G≠E, R≠H, T≠M → 1 match ✓
- vs guess 2 (A,C,G,H,T): A≠B, C≠D, G≠E, **H=H(4)✓**, T≠M → 1 match ✓
- vs guess 3 (A,C,E,R,T): A≠B, C≠D, **E=E(3)✓**, R≠H, T≠M → 1 match ✓
- vs guess 4 (A,C,G,R,M): A≠B, C≠D, G≠E, R≠H, **M=M(5)✓** → 1 match ✓
- vs guess 5 (B,C,G,R,T): **B=B(1)✓**, C≠D, G≠E, R≠H, T≠M → 1 match ✓

**Answer: B** ✓

---

## Strategy 2: Truth or Lie Deduction

You are told that **exactly one person is lying** (or exactly one is telling the truth). Your job is to find who lied and what the hidden fact is.

**Steps:**
1. Look for two people making **contradictory statements** — exactly one of them must be the liar.
2. Assume each one is the liar in turn. Check whether all other statements are then consistent.
3. The scenario where only one person ends up lying is the answer.

{: .note }
> **Key insight:** If assuming person X is the liar makes everyone else's statements consistent with a single coherent story, you have your answer.

---

### Problem 6 — Broken Vase (Only One Truth-Teller)

The vase was broken! Statements:
- Dory: "Audrey broke it."
- Audrey: "Tim broke it."
- Tim: "Audrey lied." (= Audrey's statement is false = Tim did NOT break it)
- Justin: "I didn't do it."

**Only one person told the truth.** Who told the truth, and who broke the vase?

- A. Audrey, Tim &nbsp; B. Tim, Justin &nbsp; C. Tim, Dory &nbsp; D. Dory, Audrey &nbsp; E. Justin, Dory

**Answer: B (Tim told the truth; Justin broke the vase)**

**Step-by-step solution:**

Step 1 — Tim says "Audrey lied." Audrey says "Tim broke it." These two statements directly contradict each other about Tim: if Audrey is telling the truth, Tim broke it; if Tim is telling the truth, Audrey lied (= Tim did NOT break it). Since only one person tells the truth, and they can't both be truth-tellers, exactly one of them is the truth-teller.

Step 2 — Assume **Tim tells the truth**. Then Audrey lied (Tim didn't break it). All other statements are lies:
- Dory lied → Audrey did NOT break it.
- Justin lied → Justin DID do it.

Step 3 — Check consistency: nobody else broke it (not Audrey by Dory's lie, not Tim by Tim's own true statement). Justin broke it. Only Tim tells the truth. ✓

**Answer: B** ✓

---

### Problem 7 — Eaten Cookie (Only One Liar)

Five children: May, Derek, Aidan, Tina, Olivia. One ate a cookie.
- May: "Aidan did not eat the cookie."
- Derek: "I ate the cookie."
- Aidan: "Olivia ate the cookie."
- Tina: "Derek did not eat the cookie."
- Olivia: "May did not eat the cookie."

Only one child is lying. Who ate the cookie?

- A. May &nbsp; B. Derek &nbsp; C. Aidan &nbsp; D. Tina &nbsp; E. Olivia

**Answer: E (Olivia)**

**Step-by-step solution:**

Step 1 — Derek and Tina make opposite claims about Derek. Exactly one of them is the liar.

Step 2 — Assume **Derek is the liar** (Derek did not eat the cookie). Then Tina tells the truth (Derek didn't eat it ✓). Now May, Aidan, and Olivia all tell the truth:
- Aidan (truth): "Olivia ate it." → Olivia ate the cookie.
- May (truth): "Aidan did not eat it." → ✓ (Olivia ate it)
- Olivia (truth): "May did not eat it." → ✓ (Olivia ate it)
- Only Derek lied. ✓

Step 3 — Check that this is the only valid scenario (if Tina were the liar instead, Derek's claim would be true — Derek ate it — but then Aidan saying "Olivia ate it" would be false → two liars. Contradiction).

**Answer: E** ✓

---

### Problem 8 — Dog Treat (Only One Liar)

Five dogs: Dora, Oreo, Charlie, Joe, Apple. One got a treat.
- Dora: "I did not get the treat!"
- Oreo: "I did not get the treat."
- Charlie: "Dora got the treat."
- Joe: "Charlie did not get the treat."
- Apple: "Joe did not get the treat and neither did I."

Only one dog is lying. Who got the treat?

- A. Dora &nbsp; B. Oreo &nbsp; C. Charlie &nbsp; D. Joe &nbsp; E. Apple

**Answer: A (Dora)**

**Step-by-step solution:**

Step 1 — Dora and Charlie make opposite claims about Dora. One of them is lying.

Step 2 — Assume **Dora is the liar** (Dora DID get the treat). Then Charlie tells the truth ("Dora got the treat" ✓). Check the rest:
- Oreo (truth): "I didn't get it." ✓ (Dora got it)
- Joe (truth): "Charlie didn't get it." ✓ (Dora got it)
- Apple (truth): "Joe didn't and I didn't." ✓ (Dora got it)
- Only Dora lied. ✓

Step 3 — Assume Charlie is the liar (Dora did NOT get the treat). Then Dora tells the truth. But then none of the five got the treat — contradiction, since exactly one must have gotten it.

**Answer: A** ✓

---

### Problem 9 — Watermelon (Only One Liar)

Three kids: Tom, Vera, Cindy.
- Tom: "I know Vera doesn't like eating watermelon."
- Vera: "I think Tom is wrong."
- Cindy: "I like eating watermelon very much."

Only one is lying. Who likes eating watermelon?

- A. Tom &nbsp; B. Vera &nbsp; C. Cindy &nbsp; D. All of them &nbsp; E. No one

**Answer: C (Cindy)**

**Step-by-step solution:**

Step 1 — Tom and Vera make directly contradictory claims about whether Vera likes watermelon. One of them is the liar.

Step 2 — Assume **Vera is the liar**. Vera claims Tom is wrong; if she's lying, Tom is correct — Vera does NOT like watermelon. Check the others:
- Tom (truth): "Vera doesn't like it." ✓
- Cindy (truth): "I like it very much." ✓ (Cindy likes watermelon)
- Only Vera lied. ✓

Step 3 — Assume Tom is the liar. Then Vera does like watermelon. Vera's statement ("Tom is wrong") is true ✓. Cindy's statement is true ✓. Only Tom lied — but now both Vera and Cindy like watermelon. No answer choice says "Vera and Cindy," so this scenario doesn't match a clean answer.

Step 4 — With Vera as the liar, only Cindy likes watermelon (Vera doesn't; Tom's preference isn't stated).

**Answer: C** ✓

---

### Problem 10 — Chocolate (Only One Liar)

Three kids: Jim, Tim, Gina.
- Jim: "I don't like chocolate at all."
- Tim: "I know Gina likes chocolate."
- Gina: "I disagree with Jim." (= I think Jim is wrong about himself = Jim does like chocolate)

Only one is lying. Who likes chocolate?

- A. Jim &nbsp; B. Tim &nbsp; C. Gina &nbsp; D. All &nbsp; E. No one

**Answer: C (Gina)**

**Step-by-step solution:**

Step 1 — Gina's statement "I disagree with Jim" means Gina claims Jim's statement is false — i.e., Jim does like chocolate. Tim says Gina likes chocolate.

Step 2 — Assume **Gina is the liar**. Gina's claim (Jim likes chocolate) is false → Jim does NOT like chocolate (consistent with Jim's own statement ✓).
- Jim (truth): "I don't like chocolate." ✓
- Tim (truth): "Gina likes chocolate." → so Gina likes chocolate ✓
- Gina (lie): "Jim likes chocolate." → false ✓
- Only Gina lied. ✓ Gina likes chocolate.

Step 3 — Check alternative: if Tim is the liar, then Gina does not like chocolate. But Gina says Jim is wrong (Jim likes chocolate). If Gina tells the truth, Jim likes chocolate. And Jim says he doesn't — Jim would be lying too. Two liars. Contradiction.

**Answer: C** ✓

---

## Answer Key

| Problem | Answer |
|:--------|:------:|
| 1. Three-part name | C |
| 2. Book order | D |
| 3. Dress order | A |
| 4. Five-digit password | B |
| 5. Five-letter password | B |
| 6. Broken vase | B |
| 7. Eaten cookie | E |
| 8. Dog treat | A |
| 9. Watermelon | C |
| 10. Chocolate | C |
