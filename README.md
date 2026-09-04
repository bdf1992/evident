# Evident 30

**A 30-minute, session-based, AI-native organizational bootstrap instrument.**

Evident 30 is not a questionnaire and not a personality test. Each **session**
is one bounded attempt by a model to understand part of an organization and
place a person within it, so later work can be routed to whoever it actually
belongs to.

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

## Discovery, not form completion

Evident starts from work rather than title. A good session discovers what enters a participant's world, what changes, which systems and actors mediate the work, where authority and accountability sit, what fails, what crosses boundaries, and where routing should stop.

The operator does not need to encode every possible organizational concept in advance. Instead it uses a compact discovery grammar and chooses probes that resolve consequential uncertainty.

See [`protocol/DISCOVERY_PLAYBOOK.md`](protocol/DISCOVERY_PLAYBOOK.md) for the discovery scan, probe-priority heuristic, claim-neighbor branching, and interview recovery path. See [`protocol/WORKED_CASES.md`](protocol/WORKED_CASES.md) for contrasting behavioral examples across a team member, an AI session operator, a founder, and a federation.

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

## Relations as organizational data

Important organizational relations should not exist only inside prose. `schema/relation.schema.json` provides a canonical optional shape with:

`subject -> relation -> object`, plus scope, evidence state, provenance, perspective, valid time, qualifiers, and routing safety.

This lets later sessions federate, challenge, specialize, or supersede relations without reinterpreting natural-language summaries.

## Trust and shareability

Every sealed session contains `session.json`, `prediction.jsonl`, `facts.jsonl`, `challenges.jsonl`, human-readable organization/participant views, unknowns/handoff, `manifest.json`, and `receipt.json`. Sessions may additionally contain `relations.jsonl` using the canonical relation schema.

`tools/seal_session.py` generates the manifest/receipt. `tools/verify_session.py` verifies hashes later. Cryptographic signatures can be layered on top, but the base protocol requires no secret key to be inspectable.

A trust receipt proves **integrity and provenance of the package**, not that every claim inside is true.

## Evidence states

Keep these distinct: `registered`, `declared`, `documented`, `observed`, `inferred`, `verified`, `contested`, `unknown`.

Never silently turn prediction, inference, title, authorship, access, or activity frequency into authority or expertise.

## Start here

- [`SKILL.md`](SKILL.md) — compressed agent/session procedure
- [`protocol/DISCOVERY_PLAYBOOK.md`](protocol/DISCOVERY_PLAYBOOK.md) — how to investigate an unfamiliar organization
- [`protocol/WORKED_CASES.md`](protocol/WORKED_CASES.md) — contrasting worked-case guidance
- [`GUIDE_FRONTIER_MODELS.md`](GUIDE_FRONTIER_MODELS.md) — running with frontier models
- [`CONSTITUTION.md`](CONSTITUTION.md) — invariants
- [`protocol/EVIDENCE_POLICY.md`](protocol/EVIDENCE_POLICY.md) — evidence rules
- [`protocol/30_MINUTE_PROTOCOL.md`](protocol/30_MINUTE_PROTOCOL.md) — time budget
- [`protocol/TRUST_RECEIPT.md`](protocol/TRUST_RECEIPT.md) — trust/shareability contract
- [`schema/relation.schema.json`](schema/relation.schema.json) — canonical machine-readable organizational relation
- [`tests/first-smoke/REVIEW.md`](tests/first-smoke/REVIEW.md) — synthetic structural smoke session

## Safety / privacy

The model inspects only sources deliberately put in scope. “Can access” is not “authorized to inspect.” A shareable session should prefer source references, hashes, and minimal extracts over copying sensitive source material.

<!-- lineage:begin — generated from system-cartographer lineage/lineage.yaml. Do not hand-edit. -->

## Where this sits

This is one of 20 repositories on this account whose relations are recorded, with the evidence for each, in [`lineage.yaml`](https://github.com/bdf1992/system-cartographer/blob/claude/access-requirements-zbl1s7/lineage/lineage.yaml). What that record says about this one:

**Claim.** A session-based instrument for bootstrapping how an organization works, in about thirty minutes.

**Checked.** `python -m pytest -q` — 1 passed, observed 2026-09-04.

**Relations.** None recorded, in either direction. 12 of the 20 repositories are unconnected; that absence is recorded rather than papered over with a plausible edge.

<!-- lineage:end -->
