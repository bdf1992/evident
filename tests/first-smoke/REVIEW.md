# First Smoke Test Review

## Result
**PASS as a structural author smoke test, with revisions required before treating it as a benchmark.**

The measured rerun was intentionally fast because the fictional participant answers and evidence corpus were pre-staged. It tests output discipline and evidence handling, **not** the full 30-minute interactive burden.

The protocol successfully avoided three common failures:
1. It did not convert Chen's proximity to stock data into ownership of stock accuracy.
2. It separated procurement familiarity from approval authority.
3. A participant correction materially changed the placement and remained visible as a challenge rather than being silently overwritten.

## What the test exposed

### 1. The protocol needs a stronger claim target discipline
Questions should preferably identify which relation is being tested. Otherwise frontier models may ask pleasant but low-information interview questions.

### 2. Verified needs to remain purpose-bounded
A global verified label would overstate what the tiny fixture establishes.

### 3. Physical vs informational ownership is a valuable distinction
The participant challenge revealed three nearby but different things: physical inventory, dispatch state, and stock reporting.

### 4. We need a pre-session factual seed compilation pass for real users
For the first real session, gather a compact packet of uncontroversial, sourced facts before the 30-minute clock begins.

## v0.2 session/trust revision
The fixture now freezes three pre-interview predictions and preserves the participant correction as a separate challenge record. The session can be sealed and hash-verified, making prediction delta and package integrity independently inspectable.
