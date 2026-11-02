# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1.

Of 10 independently written human samples, at most 1 may receive the high-confidence AI label.

**Why this target:**
A false accusation can unfairly damage a writer’s credibility, so the system should prioritize avoiding confident accusations of human writing. One error in 10 allows for imperfect signals without treating frequent false positives as acceptable.

---

## 2.

The average combined score for 5 clearly AI-generated samples must be at least 0.20 higher than the average combined score for 5 clearly human-written samples.

**Why this target:**
The detector does not need perfect separation, but clearly different source groups should produce a measurable difference. A 0.20 gap is large enough to show that the signals provide useful evidence rather than random scores.

---

## 3.

A test set of at least 15 submissions must produce all three labels: high-confidence human, unsure, and high-confidence AI, with at least 1 submission in each category.

**Why this target:**
Every label represents a different user-facing outcome. If one label cannot be reached, the thresholds or scoring rule are not useful in practice and uncertain cases may be forced into an overconfident category.

---

## 4.

For every valid appeal submitted for an existing content_id, the service must return HTTP 200, append exactly one audit entry with "event": "appeal" and "status": "under_review", and leave the original decision entry unchanged.

**Why this target:**
 A writer needs a reliable way to challenge a decision. Keeping the original entry while appending the appeal preserves an auditable history instead of silently overwriting the first decision.

---

## 5.

For each of these inputs—missing text, empty text, non-string text, and text longer than 10,000 characters—the /submit endpoint must return a client-error response in the 400–413 range, include a JSON error message, and must not run the detector or create a normal decision entry.

**Why this target:**
Invalid or excessively large input should be rejected clearly and cheaply rather than causing a server error, wasting model resources, or producing a misleading score.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
