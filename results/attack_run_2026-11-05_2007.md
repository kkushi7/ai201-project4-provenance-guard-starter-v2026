# Attack run

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-05 20:07
- Auto-marked BROKE (5xx, crash, no response): **9**
- Left for you to judge: **47**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `09af37ac-4441-4dbe-87d1-0e086f94588e` | unsure | 0.359 | Held |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `5ad489bc-fbb9-4d98-9480-51eedae9c962` | unsure | 0.439 | Held |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `1f7b2fb1-eb0d-4d70-8974-23523c6119d1` | unsure | 0.551 | Held |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `5fa1357f-847f-4b5b-98ee-95d880a1ca7a` | unsure | 0.578 | Held |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `129009c6-b5e7-45d3-a6cc-12854367b268` | human | 0.342 | Held |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `1d04d895-299a-45e1-a2cc-4634e8726ecc` | unsure | 0.424 | Held |
| EV07 | evasion | signal two: padding with punctuation | 200 | `5fb56094-03ed-4dba-96b6-eb41b32c0f73` | unsure | 0.608 | Held |
| EV08 | evasion | signal one: text below the token window | 200 | `1f7f3cc5-81a4-4e06-ba56-2a579ef68219` | human | 0.335 | Held |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `f8aaacdd-d06d-449c-aa94-1c9519220a34` | unsure | 0.566 | Held |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `549112ef-68bd-4707-b58b-69337d8ea872` | ai | 0.841 | Broke |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `6def28f2-84ae-41c3-90d8-a7834c1eb141` | unsure | 0.556 | Broke |
| FP02 | false_positive | human writing in a formal register | 200 | `f383305d-f65d-46e2-bbd5-0edb425d9988` | ai | 0.662 | Held |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `584a35e1-d384-46f1-be7e-871ddcf381d0` | ai | 0.676 | Held |
| FP04 | false_positive | a student essay written to a rubric | 200 | `7c1a1019-1edc-4353-b397-b10905da25f7` | ai | 0.661 | Held |
| FP05 | false_positive | technical documentation written by a person | 200 | `9ce14d7c-69e3-4e4b-b331-a52dd34199d0` | ai | 0.705 | Held |
| FP06 | false_positive | a person imitating a formal template | 200 | `cc939153-7227-4b30-9b66-34d614f71760` | ai | 0.670 | Held |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `dd86f194-049d-4936-9863-b9410b81740c` | ai | 0.676 | Held |
| FP08 | false_positive | very short genuine human submission | 200 | `f5ed6eb5-71cd-4bd0-9b98-979c257c26e5` | human | 0.291 | Broke |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `bfbba0ec-6314-4f81-bce8-73a84d40b1f0` | unsure | 0.397 | Broke |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `830f3cf0-faac-4ac2-a888-5f06668fe33d` | human | 0.250 | Held |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `99f9a967-5a22-4949-aa05-3bc52643a58b` | unsure | 0.528 | Broke |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `0273da9e-176e-4849-b0fa-6befd1cd4209` | unsure | 0.436 | Broke |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `b42193ce-af09-498b-a572-33b84b02c705` | unsure | 0.443 | Broke |
| PI06 | prompt_injection | instruction plus real human text | 200 | `dc521d97-33e9-464f-ac77-db48aba029c3` | unsure | 0.530 | Broke |
| MF01 | malformed | text is only whitespace | 200 | `2ea0c60d-5ba1-4ba1-b2f1-7eb59716500c` | unsure | 0.353 | Held |
| MF02 | malformed | text is a single character | 500 | `—` | — | — | BROKE |
| MF03 | malformed | text is control characters | 200 | `05bca16a-e381-4341-a466-b453f1af28c1` | human | 0.200 | Held |
| MF04 | malformed | text is only punctuation | 200 | `339aedb9-cf4c-4301-852e-c9b5011a4236` | unsure | 0.406 | Held |
| MF05 | malformed | text is a very long single word | 200 | `a125a6d3-e3cf-48d1-b290-46095fe6f035` | ai | 0.799 | Held |
| MF06 | malformed | text is emoji only | 200 | `35073a32-72a6-45ba-b603-dcc139fbfb76` | ai | 0.898 | Held |
| MF07 | malformed | text is right-to-left script | 200 | `cfc66ffd-8953-4f32-8d18-9878dd538926` | ai | 0.944 | Held |
| MF08 | malformed | text is 60,000 characters | 200 | `8c4bc0cc-ee12-458c-b4d5-5945b57ee2fb` | ai | 0.888 | Held |
| RQ01 | malformed | no text field at all | 500 | `—` | — | — | BROKE |
| RQ02 | malformed | no creator_id | 200 | `f201ae44-620f-4330-9e1c-7ba0e83bb54c` | unsure | 0.402 | Held |
| RQ03 | malformed | text is a number | 500 | `—` | — | — | BROKE |
| RQ04 | malformed | text is a list | 500 | `—` | — | — | BROKE |
| RQ05 | malformed | text is null | 500 | `—` | — | — | BROKE |
| RQ06 | malformed | creator_id is an object | 200 | `eb37f7bf-abcc-4c74-a98b-c60b1bf4e3b2` | human | 0.269 | Held |
| RQ07 | malformed | body is a JSON array, not an object | 500 | `—` | — | — | BROKE |
| RQ08 | malformed | body is unparseable JSON | 500 | `—` | — | — | BROKE |
| RQ09 | malformed | body is empty | 500 | `—` | — | — | BROKE |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — | Held |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — | Held |
| RQ12 | malformed | deeply nested JSON | 500 | `—` | — | — | BROKE |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7e02d5b9-43e8-4557-8db1-81123ced3e22` | human | 0.296 | Broke |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `9cb10c7d-d48b-413b-949e-621a8ce449c8` | human | 0.296 | Broke |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `77e4966a-47fd-43cd-a647-e82fba373976` | human | 0.296 | Broke |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5a560ec8-a181-4a8f-80a3-5cc711d31098` | human | 0.296 | Broke |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `154341d1-3a75-4c0a-905d-129fe52a7040` | human | 0.296 | Broke |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | Held |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | Held |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | Held |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | Held |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | Held |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | Held |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | Held |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 9 | 11 |
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
  "content_id": "09af37ac-4441-4dbe-87d1-0e086f94588e",
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
  "content_id": "5ad489bc-fbb9-4d98-9480-51eedae9c962",
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
  "content_id": "1f7b2fb1-eb0d-4d70-8974-23523c6119d1",
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
  "content_id": "5fa1357f-847f-4b5b-98ee-95d880a1ca7a",
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
  "content_id": "129009c6-b5e7-45d3-a6cc-12854367b268",
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
  "content_id": "1d04d895-299a-45e1-a2cc-4634e8726ecc",
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
  "content_id": "5fb56094-03ed-4dba-96b6-eb41b32c0f73",
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
  "content_id": "1f7f3cc5-81a4-4e06-ba56-2a579ef68219",
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
  "content_id": "f8aaacdd-d06d-449c-aa94-1c9519220a34",
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
  "content_id": "549112ef-68bd-4707-b58b-69337d8ea872",
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
  "content_id": "6def28f2-84ae-41c3-90d8-a7834c1eb141",
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
  "content_id": "f383305d-f65d-46e2-bbd5-0edb425d9988",
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
  "content_id": "584a35e1-d384-46f1-be7e-871ddcf381d0",
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
  "content_id": "7c1a1019-1edc-4353-b397-b10905da25f7",
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
  "content_id": "9ce14d7c-69e3-4e4b-b331-a52dd34199d0",
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
  "content_id": "cc939153-7227-4b30-9b66-34d614f71760",
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
  "content_id": "dd86f194-049d-4936-9863-b9410b81740c",
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
  "content_id": "f5ed6eb5-71cd-4bd0-9b98-979c257c26e5",
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
  "content_id": "bfbba0ec-6314-4f81-bce8-73a84d40b1f0",
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
  "content_id": "830f3cf0-faac-4ac2-a888-5f06668fe33d",
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
  "content_id": "99f9a967-5a22-4949-aa05-3bc52643a58b",
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
  "content_id": "0273da9e-176e-4849-b0fa-6befd1cd4209",
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
  "content_id": "b42193ce-af09-498b-a572-33b84b02c705",
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
  "content_id": "dc521d97-33e9-464f-ac77-db48aba029c3",
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
  "status": 200,
  "content_id": "2ea0c60d-5ba1-4ba1-b2f1-7eb59716500c",
  "creator_id": "attacker_MF01",
  "guess": "unsure",
  "confidence": 0.3527,
  "model_score": 0.2053,
  "style_score": 0.5,
  "label": "We cannot tell reliably whether this was written by a person or generated by AI.",
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
  "content_id": "05bca16a-e381-4341-a466-b453f1af28c1",
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
  "content_id": "339aedb9-cf4c-4301-852e-c9b5011a4236",
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
  "content_id": "a125a6d3-e3cf-48d1-b290-46095fe6f035",
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
  "content_id": "35073a32-72a6-45ba-b603-dcc139fbfb76",
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
  "content_id": "cfc66ffd-8953-4f32-8d18-9878dd538926",
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
  "status": 200,
  "content_id": "8c4bc0cc-ee12-458c-b4d5-5945b57ee2fb",
  "creator_id": "attacker_MF08",
  "guess": "ai",
  "confidence": 0.8878,
  "model_score": 0.9876,
  "style_score": 0.788,
  "label": "We think this was probably generated by AI.",
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: Text is too short to score \u2014 a few sentences at least.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&a",
  "verdict": "BROKE"
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 200,
  "content_id": "f201ae44-620f-4330-9e1c-7ba0e83bb54c",
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
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: text input must be of type `str` (single example), `list[str]` (batch or single pretokenized example) or `list[list[str]]` (batch of pret",
  "verdict": "BROKE"
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: Text is too short to score \u2014 a few sentences at least.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&a",
  "verdict": "BROKE"
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: You need to specify either `text` or `text_target`.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&amp;",
  "verdict": "BROKE"
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 200,
  "content_id": "eb37f7bf-abcc-4c74-a98b-c60b1bf4e3b2",
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
  "status": 500,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>AttributeError: &#39;list&#39; object has no attribute &#39;get&#39;\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes",
  "verdict": "BROKE"
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 500,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: Text is too short to score \u2014 a few sentences at least.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&a",
  "verdict": "BROKE"
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 500,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: Text is too short to score \u2014 a few sentences at least.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&a",
  "verdict": "BROKE"
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
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: text input must be of type `str` (single example), `list[str]` (batch or single pretokenized example) or `list[list[str]]` (batch of pret",
  "verdict": "BROKE"
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "7e02d5b9-43e8-4557-8db1-81123ced3e22",
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
  "content_id": "9cb10c7d-d48b-413b-949e-621a8ce449c8",
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
  "content_id": "77e4966a-47fd-43cd-a647-e82fba373976",
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
  "content_id": "5a560ec8-a181-4a8f-80a3-5cc711d31098",
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
  "content_id": "154341d1-3a75-4c0a-905d-129fe52a7040",
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
