# Skill: Evident 30 Session

## Purpose

In at most 30 minutes, conduct one attributable session that creates an evidence-backed update to a bounded organizational model and places one participant within it for recognition, routing, and organizational navigation.

Evident is not a questionnaire. It is an active organizational discovery process. The model should choose probes that resolve consequential distinctions rather than exhaust categories.

## Session outputs

A session is not complete until it has scope receipt, frozen pre-interview prediction, participant interview evidence, evidence ledger, participant challenge opportunity, placement + organizational view, unknowns/handoff, and trust manifest/receipt.

When important organizational relations are established, prefer also recording canonical relation objects using `schema/relation.schema.json`. Relations should remain attributable to evidence rather than being reconstructed later from prose.

## Inputs

Required: participant willing to be interviewed, session purpose, bounded space or permission to help define one.

Optional: prior sessions/baseline, registered organization/domain/concern seed, factual seed pack, explicitly allowed files/repositories/exports/directories/systems.

## Core primitives

Space, Session, Participant, Domain, Concern/Axis, Object, Work, Role, Relation, Claim, Evidence, Placement, Authority.

Prefer registered vocabulary and relations over new primitives.

## Discovery stance

Start from **work rather than title**. Discover what enters the participant's world, what they do with it, what leaves changed, what systems mediate it, who can decide or approve, what persists, what fails, what crosses boundaries, and where the participant stops being a valid route.

During the interview scan for missing dimensions: **where, who, what, how, power, flow, failure, time, evidence, unknown**. Do not force every dimension into every session; use absence to choose the next high-value probe.

Use `protocol/DISCOVERY_PLAYBOOK.md` for probe selection, claim-neighbor branching, recovery when stuck, and challenge presentation. Use `protocol/WORKED_CASES.md` as behavioral examples, not scripts.

## Procedure

### A. Bind session (0-3m)
Establish scope, purpose, participant representation, **operator identity**, operator/participant relationship, prior session/baseline references, allowed and excluded evidence, sensitivity constraints, and completion criteria. Create `session.json`. The session ID must remain stable.

Distinguish the participant being modeled from the operator/model conducting the session. If they are the same actor, assisted, delegated, or otherwise non-independent, record that explicitly.

### B. Register + predict (3-7m)
Capture only enough coordinates to navigate: spaces, domains, axes, systems/objects, roles/authority vocabulary, federated/inherited context.

Then freeze **pre-interview predictions** before substantive participant questioning.

A prediction may use registered/common facts deliberately supplied for the session, a factual seed pack, explicitly allowed artifacts inspected before interview, and ordinary low-risk inference from those facts.

A prediction may **not** use participant answers from this session, hidden personal context, unstated assumptions presented as facts, or title/activity/authorship as proof of ownership, expertise, or authority.

For each prediction record statement/relation, scope, basis/provenance, confidence, falsifier/update condition, and `routing_safe=false` unless independently established.

### C. Interview adaptively (7-18m)
Ask probes that most reduce uncertainty or test high-value predictions. Prefer formal vs operational ownership, knowledge vs authority, documented vs lived process, normal vs exception path, local vs inherited rule, recognizable vs routable work, and current vs historical reality.

Useful probe families: existence, definition, recognition, ownership, authority, process, routing, dependency, boundary, exception, evidence, failure.

Prefer a probe when it combines high uncertainty, high organizational or routing consequence, and a reasonable chance the participant can resolve it. Do not re-ask established facts merely to complete a category.

When an important claim appears, identify the nearest alternative interpretation that would materially change placement or routing and probe that distinction. For example, `maintains status` should not silently become `owns`, `approves`, or `is accountable for`.

If stuck, traverse: `work -> object/system -> flow -> dependency -> capability -> authority -> accountability -> exception -> boundary -> routing`.

Do not exhaust a questionnaire. Record claims, relations, and provenance as the session proceeds.

### D. Test evidence + prediction (18-23m)
Inspect only high-value authorized sources. Before inspecting a source, identify which live claim or distinction it could resolve. Classify material predictions as `supported`, `narrowed`, `contradicted`, `unresolved`, or `not-tested`.

Do not reward the model for prediction accuracy. Prediction exists for auditability, calibration, and discovery of assumptions.

Do not use evidence volume as a substitute for relevance or independence.

### E. Challenge (23-27m)
Show the participant the emerging organization view, their placement, important prediction deltas, strongest evidence, weakest assumptions, contradictions/unknowns, and explicit `do-not-route` / authority boundaries.

Present a falsifiable map rather than asking only whether the summary "looks right." Ask which relation, boundary, route, authority label, or missing actor is wrong.

Record corrections in `challenges.jsonl`; do not silently overwrite challenged claims.

### F. Compile + seal (27-30m)
Stop exploratory questioning. Write human and machine-readable outputs, then run `tools/seal_session.py SESSION_DIR`.

Before sealing, check that the result makes the consequential parts of **where / who / what / how / power / flow / failure / time / evidence / unknown** visible or explicitly unknown for the session purpose.

If time expires, compile and seal a `partial` session rather than extending the interview.

## Placement relations

Attempt to distinguish `knows-about`, `works-with`, `owns`, `approves`, `contributes-to`, `reviews`, `supports`, `consults-on`, `routes-to`, `do-not-route`, and `outside-authority`.

Also preserve nearby distinctions when material: `can-access`, `can-execute`, `permitted-to-execute`, `accountable-for`, `depends-on`, `governed-by`, `persists-in`, and `performed-through`.

Knowledge/relevance never implies responsibility or authority. Capability never implies permission. Permission never automatically implies ownership or accountability.

## Session federation

A later session may reference earlier receipts and corroborate, specialize, contest, supersede-for-scope, or leave them unresolved. Do not mutate earlier sealed session evidence to make the current model cleaner.

When federating machine-readable results, prefer explicit relation records with subject, relation, object, scope, evidence state, provenance, perspective, and valid time over extracting relations from prose.

## Stop rule

Stop at 30 minutes or when the stated purpose has enough evidence and further probing has low value. Stop an interview branch when its routing consequence is established, remaining ambiguity would not change placement, the participant cannot resolve it and a handoff path exists, or it is outside scope.

A successful session is a useful, inspectable, correctable update—not complete knowledge.
