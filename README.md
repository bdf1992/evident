# Evident 30

**A 30-minute, session-based, AI-native organizational bootstrap instrument.**

Evident 30 is not a fixed questionnaire and not a personality test. Each **session** is a bounded attempt by a frontier model to understand part of an organizational space and place a participant within it for future recognition and routing.

A session must:

1. bind scope, purpose, consent, and evidence access,
2. register the initial organizational coordinates,
3. make a **pre-interview prediction** using only common/supplied facts and explicitly allowed evidence,
4. interview and probe the participant adaptively,
5. compare prediction, participant account, and inspected evidence,
6. let the participant challenge the emerging model,
7. compile an evidence-backed placement plus contradictions and unknowns, and
8. seal the session with a **trust receipt** that makes the result inspectable and shareable.

The same session protocol should work for one person, a four-person team, a company, a federated enterprise, or a government-like federation. Scale should add **spaces, relations, perspectives, evidence, and sessions** rather than new core primitives.

## Why session-based

A session is a first-class evidence object. It has a start/end, purpose, participant, model identity, inputs, pre-interview predictions, inspected sources, corrections, outputs, and receipt. Later sessions may supersede, narrow, challenge, or corroborate earlier ones without silently rewriting history.

The organization model is therefore built from a **federation of attributable sessions**, not from one omniscient questionnaire run.

## The 30-minute contract

The wall-clock investigation budget is hard.

| Minute | Activity |
|---:|---|
| 0-3 | Bind session: scope, purpose, consent, allowed evidence |
| 3-7 | Register coordinates + compile pre-interview prediction |
| 7-18 | Adaptive participant interview / scenario probes |
| 18-23 | High-value evidence checks and prediction testing |
| 23-27 | Show model + prediction deltas; participant challenges/corrections |
| 27-30 | Compile and seal trust receipt |

Preparation of a small factual seed pack may happen **before** the clock. The session itself records exactly which seed pack was used.

## Pre-interview prediction

Before asking substantive participant questions, the model must write `prediction.jsonl` containing a small number of explicit hypotheses based only on common/supplied facts and authorized pre-interview evidence.

Each prediction records the predicted relation/fact, scope, basis, confidence, what would change the prediction, and whether it is safe to use for routing before interview (`false` by default).

This prevents hindsight: the final placement can show what the model got right, what the participant corrected, and what evidence changed.

## Trust and shareability

Every sealed session contains `session.json`, `prediction.jsonl`, `facts.jsonl`, `challenges.jsonl`, human-readable organization/participant views, unknowns/handoff, `manifest.json`, and `receipt.json`.

`tools/seal_session.py` generates the manifest/receipt. `tools/verify_session.py` verifies hashes later. Cryptographic signatures can be layered on top, but the base protocol requires no secret key to be inspectable.

A trust receipt proves **integrity and provenance of the package**, not that every claim inside is true.

## Evidence states

Keep these distinct: `registered`, `declared`, `documented`, `observed`, `inferred`, `verified`, `contested`, `unknown`.

Never silently turn prediction, inference, title, authorship, access, or activity frequency into authority or expertise.

## Start here

- [`SKILL.md`](SKILL.md) — agent/session procedure
- [`GUIDE_FRONTIER_MODELS.md`](GUIDE_FRONTIER_MODELS.md) — running with frontier models
- [`CONSTITUTION.md`](CONSTITUTION.md) — invariants
- [`protocol/EVIDENCE_POLICY.md`](protocol/EVIDENCE_POLICY.md) — evidence rules
- [`protocol/30_MINUTE_PROTOCOL.md`](protocol/30_MINUTE_PROTOCOL.md) — time budget
- [`protocol/TRUST_RECEIPT.md`](protocol/TRUST_RECEIPT.md) — trust/shareability contract
- [`tests/first-smoke/REVIEW.md`](tests/first-smoke/REVIEW.md) — synthetic smoke session

## Safety / privacy

The model inspects only sources deliberately put in scope. “Can access” is not “authorized to inspect.” A shareable session should prefer source references, hashes, and minimal extracts over copying sensitive source material.
