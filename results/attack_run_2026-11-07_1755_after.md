# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-07 17:55
- Auto-marked BROKE (5xx, crash, no response): **1**
- Left for you to judge: **55**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

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

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 1 | 19 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "0168c2cd-fdce-4228-9e5c-8ee68a2b252b",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.3588,
  "model_score": 0.1635,
  "style_score": 0.554,
  "label": "We cannot tell reliably whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "6dd8d7f6-873b-4c5b-b0b3-2e8f3720079c",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.4385,
  "model_score": 0.5943,
  "style_score": 0.2826,
  "label": "We cannot tell reliably whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "8fe27f76-b6da-403a-9d47-d497dc3773be",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5507,
  "model_score": 0.6662,
  "style_score": 0.4352,
  "label": "We cannot tell reliably whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "9db01e98-f09a-426f-bb82-fa045a288e49",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.5783,
  "model_score": 0.6114,
  "style_score": 0.5451,
  "label": "We cannot tell reliably whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "ce5306f4-7fda-4283-a72f-05937645f6cc",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.3415,
  "model_score": 0.3212,
  "style_score": 0.3617,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "d0b80f2f-8844-44e4-8786-31df6496c91a",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.4239,
  "model_score": 0.5727,
  "style_score": 0.275,
  "label": "We cannot tell reliably whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "96f8a2aa-6270-4884-905c-fffd40e0d493",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.6078,
  "model_score": 0.5862,
  "style_score": 0.6293,
  "label": "We cannot tell reliably whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "d0e33b4c-ade8-4878-949a-5f0de280e906",
  "creator_id": "attacker_EV08",
  "guess": "human",
  "confidence": 0.3352,
  "model_score": 0.2452,
  "style_score": 0.4253,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "5b6a3aeb-8afd-4bf4-b836-551accd80053",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.5656,
  "model_score": 0.7042,
  "style_score": 0.427,
  "label": "We cannot tell reliably whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "1f21d952-2b2d-4659-a5cc-8c31dde2dc53",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.8412,
  "model_score": 0.9792,
  "style_score": 0.7032,
  "label": "We think this was probably generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "11165cf1-820d-4480-944e-cff849dc36c5",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5564,
  "model_score": 0.6175,
  "style_score": 0.4953,
  "label": "We cannot tell reliably whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "370175eb-a371-4e3d-b29c-c47245628507",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.6624,
  "model_score": 0.7387,
  "style_score": 0.5861,
  "label": "We think this was probably generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "31cacd0e-57ea-4c78-91bd-2966b3cb20b5",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.6756,
  "model_score": 0.8051,
  "style_score": 0.5461,
  "label": "We think this was probably generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "5dabc30e-0820-4ed7-8e38-094d208d97d1",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.6611,
  "model_score": 0.8329,
  "style_score": 0.4892,
  "label": "We think this was probably generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "68e8a32d-9af8-4da4-b1f8-f2ca402d7ac1",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.7048,
  "model_score": 0.8005,
  "style_score": 0.6092,
  "label": "We think this was probably generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "8894cea9-af88-405b-9d0c-bb8841dd365f",
  "creator_id": "attacker_FP06",
  "guess": "ai",
  "confidence": 0.6702,
  "model_score": 0.8814,
  "style_score": 0.4589,
  "label": "We think this was probably generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "9ca46c32-b8e7-48de-b000-4d59e3c4fcdb",
  "creator_id": "attacker_FP07",
  "guess": "ai",
  "confidence": 0.6763,
  "model_score": 0.8816,
  "style_score": 0.4709,
  "label": "We think this was probably generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "a5430f6f-20fd-404f-a198-86e5a0fa4b57",
  "creator_id": "attacker_FP08",
  "guess": "human",
  "confidence": 0.2912,
  "model_score": 0.3223,
  "style_score": 0.2601,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "9749e8c7-4aaf-44dd-9ed7-20849a2a116d",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.3965,
  "model_score": 0.4625,
  "style_score": 0.3304,
  "label": "We cannot tell reliably whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "0b9b9cac-10eb-447d-90c6-b997bb226a29",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.2496,
  "model_score": 0.2044,
  "style_score": 0.2949,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "108dbbc5-266d-475f-bd78-0434c5f13740",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5282,
  "model_score": 0.5943,
  "style_score": 0.462,
  "label": "We cannot tell reliably whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "30a779a8-bfd6-42be-991a-a997fa429442",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.4362,
  "model_score": 0.4998,
  "style_score": 0.3726,
  "label": "We cannot tell reliably whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "8d6cbf20-e174-4266-b42f-4176f8ca7597",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.4433,
  "model_score": 0.6401,
  "style_score": 0.2464,
  "label": "We cannot tell reliably whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "a473590b-c41d-4406-ac98-697a62ee9790",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5299,
  "model_score": 0.5583,
  "style_score": 0.5015,
  "label": "We cannot tell reliably whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: Text is too short to score \u2014 a few sentences at least.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&a",
  "verdict": "BROKE"
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "8e692dde-9efa-4a87-b54b-1e13c080f99c",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.2,
  "model_score": 0.0,
  "style_score": 0.4,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "a7204197-1f30-479b-b7c2-1385c2ad09b3",
  "creator_id": "attacker_MF04",
  "guess": "unsure",
  "confidence": 0.4056,
  "model_score": 0.0112,
  "style_score": 0.8,
  "label": "We cannot tell reliably whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "94365cb6-b1f1-44f6-99b6-8e792a18abf9",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.7988,
  "model_score": 0.9976,
  "style_score": 0.6,
  "label": "We think this was probably generated by AI.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "4cb9ab66-3614-4a51-bccc-7fdb050e4ca4",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.8984,
  "model_score": 0.9969,
  "style_score": 0.8,
  "label": "We think this was probably generated by AI.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "10aa970f-6441-4701-a433-6e2fdbdeca08",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.9437,
  "model_score": 0.9064,
  "style_score": 0.981,
  "label": "We think this was probably generated by AI.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 413,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 200,
  "content_id": "d95f4d5c-d78a-413d-9c7d-3a0c04ada38f",
  "creator_id": null,
  "guess": "unsure",
  "confidence": 0.4015,
  "model_score": 0.2395,
  "style_score": 0.5636,
  "label": "We cannot tell reliably whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 200,
  "content_id": "1b486109-b8b1-4d84-b8f9-be7c13902e3a",
  "creator_id": {
    "id": "x"
  },
  "guess": "human",
  "confidence": 0.2691,
  "model_score": 0.0492,
  "style_score": 0.4889,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "a07e30e4-d2fc-4224-9ed7-882cff7ebf3e",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2961,
  "model_score": 0.0287,
  "style_score": 0.5636,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "44b9ec06-e9b2-47ac-8c79-0b1d308d32bf",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2961,
  "model_score": 0.0287,
  "style_score": 0.5636,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "f57bf133-13cc-4ab2-bf36-3642f1a3c3da",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2961,
  "model_score": 0.0287,
  "style_score": 0.5636,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "dd322acb-24cb-4d34-8faf-f5ad41fe426c",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2961,
  "model_score": 0.0287,
  "style_score": 0.5636,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "dbff1970-f37f-4258-91ad-aef4f53a5db2",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2961,
  "model_score": 0.0287,
  "style_score": 0.5636,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
