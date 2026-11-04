# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->



---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:**
detector.py::model_signal measures the text's predictability to a local language model using perplexity. Low perplexity means the model finds the word sequence easy to predict, producing a higher AI-likelihood score.

**Why that might differ between human and AI writing:**
Language models generate text by selecting likely next words, so generated prose often uses common words, familiar sentence patterns, and predictable transitions. Human writing may be more surprising because of unusual word choices, abrupt changes, or personal phrasing.

**What it can't see:**
It cannot determine authorship. Predictable human writing—such as plain writing, second-language writing, or writing deliberately aimed at clarity—can look AI-generated. Conversely, unusual vocabulary or deliberately awkward phrasing can make AI text look human. It also does not understand who wrote the text or whether it was edited after generation.

### Signal two — the style signal

**What it measures:**
stylometry.py::style_signal measures the surface shape of the text without interpreting its meaning. It combines sentence-length variation, vocabulary repetition through type-token ratio, and punctuation density.

**Why that might differ between human and AI writing:**
Generated prose often has relatively even sentence lengths, repeated common vocabulary, and regular punctuation patterns. Human writing tends to be more uneven: short and long sentences may be mixed, vocabulary may be more idiosyncratic, and punctuation habits may vary more from writer to writer.

**What it can't see:**
It cannot understand meaning, context, or authorship. Any text-preserving or meaning-preserving edit that changes its surface form—such as adding typos, splitting or joining sentences, changing punctuation, or inserting a quotation—can change the score without changing who wrote the text. A human can naturally have AI-like stylistic statistics, and AI text can be edited to resemble human writing.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:**
I combine the two scores with a weighted average. The model signal and style
signal each contribute equally. Both signals point in the same direction:
higher means more likely AI.

When the signals disagree, the weighted average pulls the result toward the
middle rather than allowing either signal to make a confident decision alone.
Therefore, disagreement produces more uncertainty. For example, a model score
of 0.6722 and a style score of 0.4338 combine to 0.5530, which is in the unsure
range.

**The numbers:**
- Model signal weight: 0.50
- Style signal weight: 0.50
- High-confidence human: 0.00–0.35
- Unsure: 0.35–0.65
- High-confidence AI: 0.65–1.00

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**
| Test piece | Model score | Style score | Where they landed |
|---|---:|---:|---|
| clearly AI-like | 0.6828 | 0.4573 | Both lean AI, but only the model signal crosses 0.65 |
| clearly human-like | 0.3190 | 0.2972 | Both lean human, below 0.35 |
| plain conventional writing | 0.6722 | 0.4338 | Model signal leans AI; style signal remains unsure |

The plain conventional writing sample split the signals. The model score was
0.6722, which is above the high-confidence AI threshold, while the style score
was 0.4338, which is in the unsure range. This happens because plain human
writing can use common, predictable wording that the language model finds easy
to predict, even though its surface style is not strongly AI-like.

My combining rule treats this disagreement as uncertainty rather than allowing
one signal to make a confident accusation by itself. I use a weighted average
of the model and style scores in `scoring.py::combine_signals`; the combined
score should therefore fall between 0.4338 and 0.6722.

---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00–0.35, including both endpoints | We think this was probably written by a person. |
| unsure | greater than 0.35 and less than 0.65 | We cannot tell reliably whether this was written by a person or generated by AI. |
| high-confidence AI | 0.65–1.00, including both endpoints | We think this was probably generated by AI. |

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->



---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "...", "creator_id": "..."}'
```
curl.exe -X POST http://127.0.0.1:5000/submit `
  -H "Content-Type: application/json" `
  -d '{"text":"The system requires careful testing. It should record every decision clearly and consistently. Each submission receives a unique identifier. The service records the result for later review.","creator_id":"writer-001"}'
```json
{
  "content_id": "generated-uuid",
  "confidence": null,
  "guess": null,
  "label": null,
  "model_score": 0.1234,
  "style_score": null
}
```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "...", "reasoning": "..."}'
```

```json

```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=3"
```

```json
     {"timestamp": "2026-11-03T08:45:40+00:00", "content_id": "99f07cde-7fae-46df-85ce-f92c247b9e17", "creator_id": "writer-001", "guess": null, "model_score": 0.2659, "style_score": null, "combined_score": null, "label": null, "status": "decided"}
```

---

## How I Used AI

**Moment 1**

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Moment 2**

- *What I asked for:*
- *What came back:*
- *What I changed:*

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
