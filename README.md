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

**Moment 3**

- *What I asked for:*
Help me interpret the before and after evaluation runs, assign MET or MISSED
verdicts, diagnose broken attacks by stage and mechanism, and choose one
improvement.

- *What came back:*
A structured comparison of the criteria and attack results. The main
recommendation was to fix input validation before changing scoring because
malformed requests were reaching the detector and creating server errors.

- *What I changed:*
I checked the results against my five acceptance criteria, added validation in
`app.py::submit` for missing, empty, non-string, and oversized text, reran the
evaluation, and documented the remaining false-positive, evasion, malformed,
and flooding failures. I kept the original targets instead of lowering them
after missing them.

**Moment 4**

- *What I asked for:*
Help me identify the smallest code change that would fix the malformed-input
failures without changing the detector or scoring behavior.

- *What came back:*
A recommendation to validate the request body at the start of
`app.py::submit`. The validation should check that the body is a JSON object,
that `text` exists, that it is a non-empty string, and that its length is no
more than 10,000 characters.

- *What I changed:*
I added those checks before the detector and stylometry calls. The route now
returns JSON `400` errors for missing, empty, and non-string text and a `413`
error for oversized text. I reran the evaluation and confirmed that these
requests no longer create normal decision entries.

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

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict | How I decided |
|---|---|---|---|---|---|
| 1. my own writing | At most 1 of 10 high-confidence AI labels | 2/10 | 2/10 | 2/10 | MISSED | The target allowed at most 1/10 high-confidence AI labels. Each trial produced 2/10, so all trials missed the target. |
| 2. score spread | AI average at least 0.20 above human average | AI 0.480 vs human 0.510; gap -0.031 | AI 0.480 vs human 0.510; gap -0.031 | AI 0.480 vs human 0.510; gap -0.031 | MISSED | The target required the AI average to be at least 0.20 higher than the human average. Each trial produced: AI average: 0.480, Human average: 0.510, Difference: -0.031
The AI group scored lower, so the target was missed. |
| 3. label coverage | At least 1 human, unsure, and AI label | All 3 labels | All 3 labels | All 3 labels | MET | Every trial produced all three labels: human, unsure, and ai. |
| 4. appeal path | HTTP 200, one appeal audit entry, original unchanged | 200, under_review | 200, under_review | 200, under_review | MET | Every trial returned HTTP 200 with "status": "under_review". The audit log also showed one appeal entry for each content ID while preserving the original decision. |
| 5. bad input | 400–413 JSON error; no detector or decision | First 3 non-JSON errors; oversized text 200 | First 3 non-JSON errors; oversized text 200 | First 3 non-JSON errors; oversized text 200 | MISSED | The target required 400–413 JSON errors and no decision entry. Instead, the first three invalid requests produced non-JSON server errors, and the oversized request returned 200 and created a normal AI decision. |

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

### Criterion 1 — false positives

This target was MISSED in all three trials: 2 of 10 human samples received
the high-confidence AI label. The main problem is **signal one**, the model
signal. Predictable everyday wording such as “The sun is shining and the
weather is nice” received a high model score. The **combining rule** then
averaged that high model score with the style score and produced a combined
score above 0.65. The **label mapping** correctly converted that score into the
AI label, so the failure is not in the label text or threshold lookup; it is
an upstream false-positive score.

### Criterion 2 — score spread

This target was MISSED in all three trials. The five intended AI samples
averaged 0.480, while the five intended human samples averaged 0.510, giving
an AI-minus-human gap of -0.031 instead of at least 0.20.

The main failure is **signal one**: its scores did not separate the two groups.
The **signal two** scores were also similar across the groups, so the
**combining rule** had no strong independent evidence to create separation.
The equal 50/50 average preserved the overlap. The **label mapping** behaved
consistently with the resulting scores; it was not the cause of the poor
separation.

### Criterion 5 — bad input

This target was MISSED in all three trials. Missing text, empty text, and
non-string text produced non-JSON server errors instead of client-error JSON
responses. Text longer than 10,000 characters received a normal `200` decision.

The failure is at the **route** stage. `/submit` uses a default empty string for
missing text and passes invalid values directly to the detector and style
functions. It performs no type, empty-string, or length validation before
running the pipeline. The route therefore allows invalid requests to reach
the signals, and the oversized request reaches the normal scoring path and
creates a decision. The **label mapping** is not responsible for this failure.

### Broken attack patterns

The broken attacks show three main patterns rather than independent failures.

**Evasion: EV10.** The repeated-stanza attack was classified as AI with a
combined score of 0.8412. This is primarily a **signal one** and **signal two**
failure: repeated text is highly predictable to the model and has a regular,
repetitive surface shape. The **combining rule** reinforces both signals
because they point in the same AI direction, and the **label mapping** correctly
returns the high-confidence AI label.

**False positives: FP02–FP07.** These genuine human samples were classified
as AI. The recurring mechanism is **signal one** overvaluing formal,
predictable, or carefully structured language. The style signal does not
provide enough counter-evidence, so the **combining rule** keeps the combined
score above the 0.65 threshold. The **label mapping** then correctly reports
AI for those scores.

FP01 returned `unsure` and FP08 returned `human`; those should be treated as
held rather than broken if the attack succeeds only when human writing receives
the high-confidence AI label.

**Prompt injection: PI01 and PI03–PI06.** The **route** accepts
instruction-bearing text as ordinary submission content and has no explicit
prompt-injection detection or isolation step. The text is sent directly to the
signals. The detector does not follow the instruction as a language-model
assistant, but the route also does not reject or separately record the
injection. This is a route/input-handling weakness, not a label-mapping
failure.

**Malformed requests: MF02, RQ01, RQ03–RQ05, RQ07–RQ09, and RQ12.** These
fail at the **route** boundary. Missing fields, wrong JSON types, non-object
bodies, and empty bodies are not validated before detector or style processing.
They therefore produce uncaught exceptions and HTML `500` responses instead of
controlled JSON client errors. The **signals** are being called with invalid
inputs because the route does not stop them first.

**Flooding: FL01_01–FL01_05.** The **route/rate-limiting stage** deliberately
allows the first five requests under the configured limit of five per minute.
Those requests receive normal decisions; later requests receive `429`
responses. This is a partial result of the configured policy, not five
independent detector failures. The protection begins only after the allowance
has been consumed.

### Overall pattern

The largest repeated problem is upstream scoring and validation. Predictable
human writing receives high model scores, while the style signal is not strong
enough to correct it. Separately, `/submit` lacks a validation guard before
calling either signal. The label mapping is comparatively consistent: it
returns the label associated with the combined score it receives.

The targets were not all too low. Criterion 3 was met and criterion 4 was met,
but criterion 1 exposed an unacceptable false-positive rate and criterion 5
exposed a clear route-validation failure.

---

## The Improvement

**What I changed:**
I added input validation at the beginning of `app.py::submit`, before either
detector signal runs. The route now rejects missing text, empty text,
non-string text, and text longer than 10,000 characters. It returns JSON error
responses with status `400` for invalid requests and `413` for oversized text.
These requests return before a detector call or normal audit decision.

**Which diagnosis pointed at it:**
Criterion 5 and the malformed-request attacks showed a route-stage failure.
Invalid input reached the detector and caused HTML `500` responses, while
oversized input was scored normally and created a decision. The diagnosis was
that `/submit` needed to validate the request before calling
`detector.model_signal()` or `stylometry.style_signal()`.

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->
| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `0168c2cd-fdce-4228-9e5c-8ee68a2b252b` | unsure | 0.359 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `6dd8d7f6-873b-4c5b-b0b3-2e8f3720079c` | unsure | 0.439 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `8fe27f76-b6da-403a-9d47-d497dc3773be` | unsure | 0.551 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `9db01e98-f09a-426f-bb82-fa045a288e49` | unsure | 0.578 | BROKE |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `ce5306f4-7fda-4283-a72f-05937645f6cc` | human | 0.342 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `d0b80f2f-8844-44e4-8786-31df6496c91a` | unsure | 0.424 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `96f8a2aa-6270-4884-905c-fffd40e0d493` | unsure | 0.608 | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | `d0e33b4c-ade8-4878-949a-5f0de280e906` | human | 0.335 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `5b6a3aeb-8afd-4bf4-b836-551accd80053` | unsure | 0.566 | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `1f21d952-2b2d-4659-a5cc-8c31dde2dc53` | ai | 0.841 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `11165cf1-820d-4480-944e-cff849dc36c5` | unsure | 0.556 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `370175eb-a371-4e3d-b29c-c47245628507` | ai | 0.662 | BROKE |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `31cacd0e-57ea-4c78-91bd-2966b3cb20b5` | ai | 0.676 | BROKE |
| FP04 | false_positive | a student essay written to a rubric | 200 | `5dabc30e-0820-4ed7-8e38-094d208d97d1` | ai | 0.661 | BROKE |
| FP05 | false_positive | technical documentation written by a person | 200 | `68e8a32d-9af8-4da4-b1f8-f2ca402d7ac1` | ai | 0.705 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | `8894cea9-af88-405b-9d0c-bb8841dd365f` | ai | 0.670 | BROKE |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `9ca46c32-b8e7-48de-b000-4d59e3c4fcdb` | ai | 0.676 | BROKE |
| FP08 | false_positive | very short genuine human submission | 200 | `a5430f6f-20fd-404f-a198-86e5a0fa4b57` | human | 0.291 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `9749e8c7-4aaf-44dd-9ed7-20849a2a116d` | unsure | 0.397 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `0b9b9cac-10eb-447d-90c6-b997bb226a29` | human | 0.250 | HELD |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `108dbbc5-266d-475f-bd78-0434c5f13740` | unsure | 0.528 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `30a779a8-bfd6-42be-991a-a997fa429442` | unsure | 0.436 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `8d6cbf20-e174-4266-b42f-4176f8ca7597` | unsure | 0.443 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `a473590b-c41d-4406-ac98-697a62ee9790` | unsure | 0.530 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 500 | `—` | — | — | BROKE |
| MF03 | malformed | text is control characters | 200 | `8e692dde-9efa-4a87-b54b-1e13c080f99c` | human | 0.200 | BROKE |
| MF04 | malformed | text is only punctuation | 200 | `a7204197-1f30-479b-b7c2-1385c2ad09b3` | unsure | 0.406 | BROKE |
| MF05 | malformed | text is a very long single word | 200 | `94365cb6-b1f1-44f6-99b6-8e792a18abf9` | ai | 0.799 | BROKE |
| MF06 | malformed | text is emoji only | 200 | `4cb9ab66-3614-4a51-bccc-7fdb050e4ca4` | ai | 0.898 | BROKE |
| MF07 | malformed | text is right-to-left script | 200 | `10aa970f-6441-4701-a433-6e2fdbdeca08` | ai | 0.944 | BROKE |
| MF08 | malformed | text is 60,000 characters | 413 | `—` | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 200 | `d95f4d5c-d78a-413d-9c7d-3a0c04ada38f` | unsure | 0.402 | BROKE |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 200 | `1b486109-b8b1-4d84-b8f9-be7c13902e3a` | human | 0.269 | BROKE |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a07e30e4-d2fc-4224-9ed7-882cff7ebf3e` | human | 0.296 | BROKE |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `44b9ec06-e9b2-47ac-8c79-0b1d308d32bf` | human | 0.296 | BROKE |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `f57bf133-13cc-4ab2-bf36-3642f1a3c3da` | human | 0.296 | BROKE |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `dd322acb-24cb-4d34-8faf-f5ad41fe426c` | human | 0.296 | BROKE |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `dbff1970-f37f-4258-91ad-aef4f53a5db2` | human | 0.296 | BROKE |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |


| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. my own writing | At most 1 of 10 high-confidence AI labels | 2/10 | 2/10 | 2/10 | MISSED |
| 2. score spread | AI average at least 0.20 above human average | AI 0.480 vs human 0.510; gap -0.031 | AI 0.480 vs human 0.510; gap -0.031 | AI 0.480 vs human 0.510; gap -0.031 | MISSED |
| 3. label coverage | At least 1 human, unsure, and AI label | All 3 labels | All 3 labels | All 3 labels | MET |
| 4. appeal path | HTTP 200, one appeal audit entry, original unchanged | 200, under_review | 200, under_review | 200, under_review | MET |
| 5. bad input | 400–413 JSON error; no detector or decision | 400, 400, 400, 413 | 400, 400, 400, 413 | 400, 400, 400, 413 | MET |

**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->

Yes, it fixed the specific route-validation failures from criterion 5. Missing
text, empty text, non-string text, and text longer than 10,000 characters are
rejected before scoring and do not create normal decision entries. It does not
fix the false-positive or score-separation problems because those occur in the
signals and combining rule. I verified the change by rerunning:python run_eval.py --label after and checking that all four bad-input cases returned JSON 400 or 413
responses.

---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->

### Missed criteria

**Criterion 1 — false positives:** 2 of 10 human samples were still labelled
high-confidence AI in every trial. I would reduce the influence of the model
signal or raise the AI threshold so predictable human writing is more likely to
remain `unsure`. I stopped because changing the scoring rule would affect every
attack family, and I chose to fix the route-validation failure first.

**Criterion 2 — score spread:** The AI samples still averaged 0.480 while the
human samples averaged 0.510, producing a gap of -0.031 instead of +0.20. I
would replace or recalibrate the model signal and reconsider the equal 50/50
combining rule. I stopped because the existing signals did not provide enough
separation for a safe threshold change, and I did not have time to redesign the
detector.

### Evasion attacks that still got through

**EV01–EV09:** These AI texts received `unsure` or `human` labels after typos,
punctuation changes, sentence restructuring, unusual vocabulary, or a human
opening changed their surface statistics. The problem is mainly **signal two**,
with the combining rule allowing the lower style score to pull the result away
from AI. I would make the model signal more influential or add a signal that is
less sensitive to surface editing. I stopped because that would require
recalibrating the scoring pipeline and rerunning all criteria.

### False-positive attacks that still got through

**FP02–FP07:** Formal, careful, technical, templated, or deliberately repetitive
human writing was labelled high-confidence AI. The mechanism is **signal one**
overvaluing predictable wording; the style signal did not provide enough
counter-evidence, and the combining rule kept the score above 0.65. I would
lower the model signal weight or widen the `unsure` band above 0.65. I stopped
because reducing false positives would allow more AI text to pass and I did not
want to change the thresholds without another full evaluation.

### Malformed inputs that still got through

**MF02:** A one-character string caused a `500` because the detector rejected
text that passed the route's current validation. I would add a minimum-length or
minimum-token check and return a JSON `400` response before calling the
detector. I stopped after fixing the five malformed cases required by criterion
5 because the one-character minimum-length rule was outside that criterion.

**MF03–MF07:** Control characters, punctuation-only text, emoji-only text, and
right-to-left text were accepted and scored. The route checks type, emptiness,
and maximum length, but not whether the text contains meaningful scorable
content. I would add a deliberate content-validity policy, while preserving
legitimate multilingual text. I stopped because rejecting these cases safely
requires a clearer language and Unicode policy than this project currently
defines.

**RQ02:** A missing `creator_id` was accepted and scored. I would require a
non-empty string creator ID before submission. I stopped because creator ID
validation was not part of criterion 5.

**RQ06:** An object was accepted as `creator_id`. I would validate that
`creator_id` is a non-empty string and reject other types with JSON `400`. I
stopped for the same scope reason as RQ02.

### Flooding attacks that still got through

**FL01_01–FL01_05:** The first five rapid submissions were accepted because the
configured policy allows five submissions per minute. I would add a smaller
burst limit or a short cooldown so a flood cannot consume five model evaluations
immediately. I stopped because the current rate limit already blocks requests
six through twelve, and a stricter burst limit could interfere with legitimate
writers making several revisions.

The remaining flood requests, `FL01_06`–`FL01_12`, were correctly held with
`429` responses. The prompt-injection attacks were also held because the
instructions stayed inside the submitted text and did not change the service's
response format or audit behavior.

### Overall stopping point

The input-validation improvement fixed criterion 5 in all three trials. I
stopped before changing the scoring weights or thresholds because those changes
would affect false positives, evasion resistance, label coverage, and the
score-spread criterion at the same time.


**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->
I would prioritize fewer wrong accusations and widen the `unsure` range, even
if more AI-written text passed undetected. The AI authors would pay that cost
through reduced detection coverage, while real human writers would be protected
from being falsely accused.


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
