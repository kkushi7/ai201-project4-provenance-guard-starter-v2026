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
A submission arrives at POST /submit as JSON containing text and a creator ID. The service generates a unique content ID, runs the model signal from detector.py, calculates the surface-style signal from stylometry.py, and combines both scores in scoring.py. It converts the combined score into a human-readable label, records the decision through audit.py, and returns the content ID, both signal scores, combined score, guess, confidence, and label. A writer can later send the content ID and reasoning to POST /appeal; the appeal is appended to the audit log with an under_review status. GET /log returns the recorded entries as JSON.

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
I used neutral language because the system cannot prove who wrote a piece of
text. The unsure result should communicate that the two signals did not provide
enough agreement for a reliable conclusion, rather than accuse the writer of
using AI. Saying "We cannot tell reliably" acknowledges the system's limits and
leaves room for the writer's own explanation.

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
curl.exe -X POST "http://127.0.0.1:5000/appeal" `
  -H "Content-Type: application/json" `
  --data-raw '{"content_id": "10e65145-d84c-49f6-9198-9cc9649a0b5d","reasoning":"I wrote this submission myself and would like the decision reviewed."}'

```json
{
  "content_id": "10e65145-d84c-49f6-9198-9cc9649a0b5d",
  "creator_id": "writer-001",
  "event": "appeal",
  "status": "under_review",
  "reasoning": "I wrote this submission myself and would like the decision reviewed."
}

```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=3"
```

```json
     {"timestamp": "2026-11-03T08:45:40+00:00", "content_id": "99f07cde-7fae-46df-85ce-f92c247b9e17", "creator_id": "writer-001", "guess": null, "model_score": 0.2659, "style_score": null, "combined_score": null, "label": null, "status": "decided"}
```
     {"timestamp": "2026-11-04T05:17:15+00:00", "content_id": "10e65145-d84c-49f6-9198-9cc9649a0b5d", "creator_id": "writer-001", "event": "appeal", "status": "under_review", "reasoning": "I wrote this submission myself and would like the decision reviewed."}


---

## How I Used AI

**Moment 1**

- *What I asked for:*
Help me understand what the model signal and stylometry signal measure, including the blind spot of each signal.

- *What came back:*
An explanation that detector.py measures language-model predictability using perplexity, while stylometry.py measures surface features such as sentence-length variation, vocabulary repetition, and punctuation density. The model signal cannot determine authorship, and the style signal cannot understand meaning or context.

- *What I changed:*
I rewrote the explanation in my own README language and included the limitations of both signals.


**Moment 2**

- *What I asked for:*
Help me implement and test the scoring pipeline, including the style signal, combining rule, labels, audit logging, and appeal route.

- *What came back:*
Suggestions for implementing the three stylometry measures, combining the signals with equal weights, writing reader-facing labels, passing both signal scores through /submit, recording decisions with audit.log_decision, and recording appeals with audit.log_appeal.

- *What I changed:*
I reviewed the suggestions against the starter code, applied the relevant changes, tested the signals on multiple text samples, used curl to test /submit, /appeal, and /log, and documented the observed scores and audit entries in the README.


<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 5 per minute, 100 per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->
I chose 5 submissions per minute because a writer can still submit several
revisions, while an automated script trying many variations is stopped quickly.
I chose 100 submissions per day to allow regular use without permitting an
unlimited number of expensive model evaluations or threshold-probing requests.
The lower limits prioritize protecting the service and reducing false
confidence from repeated automated experiments.

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->
A caller is identified by `creator_id`. This gives each writer an independent
limit and makes the behavior easy to test. The tradeoff is that a malicious
caller could evade the limit by changing creator IDs; using an IP address would
make that harder but could unfairly group writers who share a network.

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```200 200 200 200 200 429 429 429 429 429 429 429 429 429 429
```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json
{"content_id":"549112ef-68bd-4707-b58b-69337d8ea872","creator_id":"attacker_EV10","guess":"ai","combined_score":0.8412,"status":"decided"}
{"content_id":"6def28f2-84ae-41c3-90d8-a7834c1eb141","creator_id":"attacker_FP01","guess":"unsure","combined_score":0.5564,"status":"decided"}
{"content_id":"584a35e1-d384-46df-be7e-871ddcf381d0","creator_id":"attacker_FP03","guess":"ai","combined_score":0.6756,"status":"decided"}
{"content_id":"9ce14d7c-69e3-4e4b-b331-a52dd34199d0","creator_id":"attacker_FP05","guess":"ai","combined_score":0.7048,"status":"decided"}
{"content_id":"dd86f194-049d-4936-9863-b9410b81740c","creator_id":"attacker_FP07","guess":"ai","combined_score":0.6763,"status":"decided"}
{"content_id":"bfbba0ec-6314-4f81-bce8-73a84d40b1f0","creator_id":"attacker_PI01","guess":"unsure","combined_score":0.3965,"status":"decided"}
{"content_id":"0273da9e-176e-4849-b0fa-6befd1cd4209","creator_id":"attacker_PI04","guess":"unsure","combined_score":0.4362,"status":"decided"}
{"content_id":"35073a32-72a6-45ba-b603-dcc139fbfb76","creator_id":"attacker_MF06","guess":"ai","combined_score":0.8984,"status":"decided"}
{"content_id":"cfc66ffd-8953-4f32-8d18-9878dd538926","creator_id":"attacker_MF07","guess":"ai","combined_score":0.9437,"status":"decided"}
{"content_id":"eb37f7bf-abcc-4c74-a98b-c60b1bf4e3b2","creator_id":{"id":"x"},"guess":"human","combined_score":0.2691,"status":"decided"}
{"creator_id":"attacker_flood","event":"rejected","status":"rejected","reason":"rate_limited","limit":"5 per 1 minute"}
```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:
The worst outcome was FP07. It was human writing that deliberately repeated a phrase, but the service classified it as AI with a score of 0.6763. This is a difficult false positive to explain because the repeated wording was an intentional stylistic choice.

---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. my own writing | At most 1 of 10 high-confidence AI labels | 2/10 | 2/10 | 2/10 | MISSED |
| 2. score spread | AI average at least 0.20 above human average | AI 0.480 vs human 0.510; gap -0.031 | AI 0.480 vs human 0.510; gap -0.031 | AI 0.480 vs human 0.510; gap -0.031 | MISSED |
| 3. label coverage | At least 1 human, unsure, and AI label | All 3 labels | All 3 labels | All 3 labels | MET |
| 4. appeal path | HTTP 200, one appeal audit entry, original unchanged | 200, under_review | 200, under_review | 200, under_review | MET |
| 5. bad input | 400–413 JSON error; no detector or decision | First 3 non-JSON errors; oversized text 200 | First 3 non-JSON errors; oversized text 200 | First 3 non-JSON errors; oversized text 200 | MISSED |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

**Source:** `results/run_2026-11-07_1638_before.md`, produced by `run_eval.py::main` and written by `run_eval.py::write_report`. The following are Trial 1 results.

### Criterion 1 — `my own writing`

```json
[
  {"status":200,"guess":"ai","confidence":0.6734,"model_score":0.8217,"style_score":0.5252,"label":"We think this was probably generated by AI."},
  {"status":200,"guess":"unsure","confidence":0.4231,"model_score":0.4724,"style_score":0.3738,"label":"We cannot tell reliably whether this was written by a person or generated by AI."},
  {"status":200,"guess":"human","confidence":0.3421,"model_score":0.2931,"style_score":0.3911,"label":"We think this was probably written by a person."},
  {"status":200,"guess":"ai","confidence":0.6799,"model_score":0.738,"style_score":0.6217,"label":"We think this was probably generated by AI."},
  {"status":200,"guess":"unsure","confidence":0.6334,"model_score":0.6953,"style_score":0.5714,"label":"We cannot tell reliably whether this was written by a person or generated by AI."},
  {"status":200,"guess":"human","confidence":0.3282,"model_score":0.1721,"style_score":0.4843,"label":"We think this was probably written by a person."},
  {"status":200,"guess":"unsure","confidence":0.4404,"model_score":0.2791,"style_score":0.6017,"label":"We cannot tell reliably whether this was written by a person or generated by AI."},
  {"status":200,"guess":"unsure","confidence":0.499,"model_score":0.4639,"style_score":0.5342,"label":"We cannot tell reliably whether this was written by a person or generated by AI."},
  {"status":200,"guess":"unsure","confidence":0.6029,"model_score":0.6453,"style_score":0.5606,"label":"We cannot tell reliably whether this was written by a person or generated by AI."},
  {"status":200,"guess":"unsure","confidence":0.546,"model_score":0.7804,"style_score":0.3117,"label":"We cannot tell reliably whether this was written by a person or generated by AI."}
]
```

### Criterion 2 — `score spread`

```json
[
  {"status":200,"guess":"unsure","confidence":0.5091,"model_score":0.4625,"style_score":0.5556,"label":"We cannot tell reliably whether this was written by a person or generated by AI."},
  {"status":200,"guess":"unsure","confidence":0.3816,"model_score":0.2073,"style_score":0.5559,"label":"We cannot tell reliably whether this was written by a person or generated by AI."},
  {"status":200,"guess":"unsure","confidence":0.5961,"model_score":0.6653,"style_score":0.527,"label":"We cannot tell reliably whether this was written by a person or generated by AI."},
  {"status":200,"guess":"unsure","confidence":0.6045,"model_score":0.6545,"style_score":0.5545,"label":"We cannot tell reliably whether this was written by a person or generated by AI."},
  {"status":200,"guess":"human","confidence":0.3071,"model_score":0.0436,"style_score":0.5706,"label":"We think this was probably written by a person."},
  {"status":200,"guess":"ai","confidence":0.6935,"model_score":0.8414,"style_score":0.5455,"label":"We think this was probably generated by AI."},
  {"status":200,"guess":"unsure","confidence":0.3745,"model_score":0.3001,"style_score":0.449,"label":"We cannot tell reliably whether this was written by a person or generated by AI."},
  {"status":200,"guess":"unsure","confidence":0.5222,"model_score":0.4904,"style_score":0.554,"label":"We cannot tell reliably whether this was written by a person or generated by AI."},
  {"status":200,"guess":"unsure","confidence":0.4256,"model_score":0.3802,"style_score":0.4711,"label":"We cannot tell reliably whether this was written by a person or generated by AI."},
  {"status":200,"guess":"unsure","confidence":0.5354,"model_score":0.4685,"style_score":0.6023,"label":"We cannot tell reliably whether this was written by a person or generated by AI."}
]
```

### Criterion 3 — `label coverage`

```json
[
  {"status":200,"guess":"unsure","confidence":0.4029,"model_score":0.2652,"style_score":0.5406,"label":"We cannot tell reliably whether this was written by a person or generated by AI."},
  {"status":200,"guess":"human","confidence":0.3236,"model_score":0.0671,"style_score":0.58,"label":"We think this was probably written by a person."},
  {"status":200,"guess":"unsure","confidence":0.4388,"model_score":0.3245,"style_score":0.5531,"label":"We cannot tell reliably whether this was written by a person or generated by AI."},
  {"status":200,"guess":"ai","confidence":0.6829,"model_score":0.7447,"style_score":0.6211,"label":"We think this was probably generated by AI."},
  {"status":200,"guess":"unsure","confidence":0.5362,"model_score":0.4634,"style_score":0.6089,"label":"We cannot tell reliably whether this was written by a person or generated by AI."},
  {"status":200,"guess":"human","confidence":0.3434,"model_score":0.17,"style_score":0.5167,"label":"We think this was probably written by a person."},
  {"status":200,"guess":"unsure","confidence":0.6394,"model_score":0.6482,"style_score":0.6306,"label":"We cannot tell reliably whether this was written by a person or generated by AI."},
  {"status":200,"guess":"unsure","confidence":0.4382,"model_score":0.2976,"style_score":0.5788,"label":"We cannot tell reliably whether this was written by a person or generated by AI."},
  {"status":200,"guess":"unsure","confidence":0.5715,"model_score":0.544,"style_score":0.5989,"label":"We cannot tell reliably whether this was written by a person or generated by AI."},
  {"status":200,"guess":"ai","confidence":0.7641,"model_score":0.935,"style_score":0.5932,"label":"We think this was probably generated by AI."},
  {"status":200,"guess":"unsure","confidence":0.5617,"model_score":0.5412,"style_score":0.5822,"label":"We cannot tell reliably whether this was written by a person or generated by AI."},
  {"status":200,"guess":"unsure","confidence":0.6222,"model_score":0.6665,"style_score":0.5779,"label":"We cannot tell reliably whether this was written by a person or generated by AI."},
  {"status":200,"guess":"unsure","confidence":0.464,"model_score":0.3536,"style_score":0.5744,"label":"We cannot tell reliably whether this was written by a person or generated by AI."},
  {"status":200,"guess":"unsure","confidence":0.4392,"model_score":0.3325,"style_score":0.5459,"label":"We cannot tell reliably whether this was written by a person or generated by AI."},
  {"status":200,"guess":"ai","confidence":0.7235,"model_score":0.8434,"style_score":0.6035,"label":"We think this was probably generated by AI."}
]
```

### Criterion 4 — `appeal path`

```json
[
  {
    "status":200,
    "guess":"unsure",
    "confidence":0.4213,
    "model_score":0.2742,
    "style_score":0.5683,
    "label":"We cannot tell reliably whether this was written by a person or generated by AI.",
    "appeal_status":200,
    "appeal_response":{
      "content_id":"d43132a8-6067-4678-aefe-bfaf1d55f3d9",
      "message":"Your appeal has been recorded and is under review.",
      "status":"under_review"
    }
  }
]
```

### Criterion 5 — `bad input`

```json
[
  {"status":null,"error":"JSONDecodeError: Expecting value: line 1 column 1 (char 0)","sent":"{\"creator_id\": \"eval_missing_text\"}"},
  {"status":null,"error":"JSONDecodeError: Expecting value: line 1 column 1 (char 0)","sent":"(empty text)"},
  {"status":null,"error":"JSONDecodeError: Expecting value: line 1 column 1 (char 0)","sent":"{\"text\": 12345, \"creator_id\": \"eval_non_string\"}"},
  {"status":200,"guess":"ai","confidence":0.7988,"model_score":0.9976,"style_score":0.6,"label":"We think this was probably generated by AI.","sent":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}
]
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
