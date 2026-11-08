"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        # ⚠️ PUT YOUR OWN WRITING HERE. Not AI text, not a sample from the web —
        # things you actually wrote. This is the criterion that matters most and
        # it's meaningless with someone else's prose.
        "texts": [
            "I am having a great day today! The sun is shining and the weather is nice.",
            "I am so tired. I slept late because I was up watching tv.",
            "I just made an amazing lasgna. It was made with white sauce and had a spinach ricotta filling.",
            "I hope I am able to finish this project in time so that I can relax afterwards.",
            "It's so fun talking with my friends after not seeing them for so long.",
            "Halloween was so fun this year! I was able to go out anf dance.",
            "I am looking forward to winter break to relax and chill basically the whole day.",
            "The movie I watched last night was ok. Wish there was a better plot line.",
            "It has been so cold lately, I wish it was summer again.",
            "I really hope I can get a cat one day when I move out to my own apartment. They are so cute and cuddly."
        ],
    },
    {
        "name": "score spread",
        "criterion": 2,
        "texts": [
            "Artificial intelligence systems can analyze large datasets, identify patterns, and generate consistent summaries with remarkable speed.",
            "The proposed initiative uses automation to improve efficiency, standardize decisions, and reduce delays across organizational workflows.",
            "Machine-learning models are increasingly used to classify information, predict outcomes, and support evidence-based operational planning.",
            "A well-designed digital platform can integrate data from multiple sources and provide users with timely, actionable recommendations.",
            "Modern language models produce fluent, structured explanations by learning statistical relationships from extensive collections of text.",
            "I missed the bus this morning, so I walked the rest of the way. It was cold, but I got there before the meeting started.",
            "The kitchen tap has been dripping for weeks. I put a bowl underneath it and keep forgetting to call the landlord.",
            "We had pasta for dinner and watched half a film. The children were tired and went to bed before it ended.",
            "My notebook is full of crossed-out lists. I eventually found the number I needed on an old receipt.",
            "I usually shop on Saturday morning because the market is quieter later in the day.",
        ],
    },
    # A bad-input criterion looks like this. Uncomment and adjust if that's one
    # of your five — these are raw request bodies, sent exactly as written.
    {
        "name": "label coverage",
        "criterion": 3,
        "texts": [
            "AI-generated systems optimize workflows through scalable automation and data-driven decision support.",
            "The algorithm evaluates relevant features and returns a ranked prediction for each submitted record.",
            "This report presents a structured analysis of operational efficiency, measurable outcomes, and future implementation priorities.",
            "I left my coat on the train and did not notice until I reached the next stop.",
            "The dog barked at the delivery driver, then fell asleep beside the radiator.",
            "We bought oranges, bread, and soap before heading home through the rain.",
            "I know the answer is probably somewhere in the folder, but I cannot remember which folder.",
            "The meeting was useful, although we spent too long discussing the first item.",
            "Some parts of the plan make sense to me and other parts still need work.",
            "It was a good idea in theory, but I am not sure how it would work in practice.",
            "The result looks promising, though the sample is too small to support a strong conclusion.",
            "I agree with the general direction, but I would want to test it before committing.",
            "The instructions are clear enough, apart from the final step.",
            "This change may save time, although it could introduce problems elsewhere.",
            "I understand the benefit, but I am still undecided about whether it is worth the cost.",
        ],
    },
    {
        "name": "appeal path",
        "criterion": 4,
        "texts": [
            "I wrote this submission myself and want to appeal the decision."
        ],
        "requires_appeal": True,
    },
    {
        "name": "bad input",
        "criterion": 5,
        "bodies": [
            {"creator_id": "eval_missing_text"},
            {"text": "", "creator_id": "eval_empty_text"},
            {"text": 12345, "creator_id": "eval_non_string"},
            {"text": "x" * 10001, "creator_id": "eval_too_long"},
        ],
    },
    # TODO: add what your remaining criteria need.
    #
    # A criterion about the appeal path can't be tested by sending text alone;
    # it needs a submission first and then an appeal against the content_id
    # that came back. You'll need to test that one by hand, or extend this file
    # and run_eval.py to do it. Saying which you did is part of the write-up.
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
