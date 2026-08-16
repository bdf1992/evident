# Skill: Evident 30 Session

## Purpose

In at most 30 minutes, conduct one attributable session that creates an evidence-backed update to a bounded organizational model and places one participant within it for recognition, routing, and organizational navigation.

## Session outputs

A session is not complete until it has scope receipt, frozen pre-interview prediction, participant interview evidence, evidence ledger, participant challenge opportunity, placement + organizational view, unknowns/handoff, and trust manifest/receipt.

## Inputs

Required: participant willing to be interviewed, session purpose, bounded space or permission to help define one.

Optional: prior sessions/baseline, registered organization/domain/concern seed, factual seed pack, explicitly allowed files/repositories/exports/directories/systems.

## Core primitives

Space, Session, Participant, Domain, Concern/Axis, Object, Work, Role, Relation, Claim, Evidence, Placement, Authority.

Prefer registered vocabulary and relations over new primitives.

## Procedure

### A. Bind session (0-3m)
Establish scope, purpose, participant representation, prior session/baseline references, allowed and excluded evidence, sensitivity constraints, and completion criteria. Create `session.json`. The session ID must remain stable.

### B. Register + predict (3-7m)
Capture only enough coordinates to navigate: spaces, domains, axes, systems/objects, roles/authority vocabulary, federated/inherited context.

Then freeze **pre-interview predictions** before substantive participant questioning.

A prediction may use registered/common facts deliberately supplied for the session, a factual seed pack, explicitly allowed artifacts inspected before interview, and ordinary low-risk inference from those facts.

A prediction may **not** use participant answers from this session, hidden personal context, unstated assumptions presented as facts, or title/activity/authorship as proof of ownership, expertise, or authority.

For each prediction record statement/relation, scope, basis/provenance, confidence, falsifier/update condition, and `routing_safe=false` unless independently established.

### C. Interview adaptively (7-18m)
Ask probes that most reduce uncertainty or test high-value predictions. Prefer formal vs operational ownership, knowledge vs authority, documented vs lived process, normal vs exception path, local vs inherited rule, recognizable vs routable work, and current vs historical reality.

Useful probe families: existence, definition, recognition, ownership, authority, process, routing, dependency, boundary, exception, evidence, failure.

Do not exhaust a questionnaire. Record claims and provenance as the session proceeds.

### D. Test evidence + prediction (18-23m)
Inspect only high-value authorized sources. Classify material predictions as `supported`, `narrowed`, `contradicted`, `unresolved`, or `not-tested`.

Do not reward the model for prediction accuracy. Prediction exists for auditability, calibration, and discovery of assumptions.

### E. Challenge (23-27m)
Show the participant the emerging organization view, their placement, important prediction deltas, strongest evidence, weakest assumptions, contradictions/unknowns, and explicit `do-not-route` / authority boundaries.

Record corrections in `challenges.jsonl`; do not silently overwrite challenged claims.

### F. Compile + seal (27-30m)
Stop exploratory questioning. Write human and machine-readable outputs, then run `tools/seal_session.py SESSION_DIR`.

If time expires, compile and seal a `partial` session rather than extending the interview.

## Placement relations

Attempt to distinguish `knows-about`, `works-with`, `owns`, `approves`, `contributes-to`, `reviews`, `supports`, `consults-on`, `routes-to`, `do-not-route`, and `outside-authority`.

Knowledge/relevance never implies responsibility or authority.

## Session federation

A later session may reference earlier receipts and corroborate, specialize, contest, supersede-for-scope, or leave them unresolved. Do not mutate earlier sealed session evidence to make the current model cleaner.

## Stop rule

Stop at 30 minutes or when the stated purpose has enough evidence and further probing has low value. A successful session is a useful, inspectable, correctable update—not complete knowledge.
