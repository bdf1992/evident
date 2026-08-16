# Guide for Frontier Models

## Operator prompt

> Start an Evident 30 session with me. Treat 30 minutes as a hard wall-clock investigation budget. Freeze a pre-interview prediction from the supplied/common factual baseline before substantive interview questions. Follow the evidence policy. Do not assume access implies permission. Start from work rather than title. Use the discovery playbook to choose high-information probes and test neighboring interpretations that would change routing, authority, or placement. Show me what your prediction got wrong or had to narrow. Give me a falsifiable correction/challenge step. Compile and seal the session with the trust receipt when time expires or the stop rule is met.

If the model cannot reliably track wall time, use an external timer.

## Before the session

Optionally prepare a small factual seed pack: official names, dated org charts, registered products/services, repository existence/README text, policies/runbooks, issue metadata, system inventories, published role descriptions, schemas/configuration. Keep interpretation out.

Record the operator separately from the participant. If the interviewer and participant are the same actor, assisted, delegated, or otherwise non-independent, preserve that relationship in session metadata.

## How to investigate

Read `protocol/DISCOVERY_PLAYBOOK.md` before conducting an unfamiliar session.

Do not turn its categories into a form. Use them as a scan for consequential absences. Prefer questions that distinguish nearby organizational meanings, such as:

- knows vs owns;
- can access vs may inspect;
- can execute vs may execute now;
- updates vs approves;
- permission vs authority;
- authority vs accountability;
- normal route vs exception route;
- local practice vs inherited rule;
- temporary role vs durable organizational role.

When an important claim appears, ask what neighboring interpretation would route work differently, then probe that distinction.

If stuck, use the recovery traversal:

`work -> object/system -> flow -> dependency -> capability -> authority -> accountability -> exception -> boundary -> routing`

See `protocol/WORKED_CASES.md` for behavioral examples. Learn the investigative moves; do not copy their answers.

## Prediction discipline

Before participant evidence, the model must state a small set of predictions. Predictions are hypotheses, not scores and not truths. Good predictions are relations worth testing, e.g. “Given the registered role and runbook, Chen is likely a routing target for dispatch status, but purchase approval is not established.”

Do not predict protected traits, sensitive personal attributes, personality, health, politics, or other irrelevant private characteristics. Predict only organizational relations needed for the stated purpose.

## Machine-readable relations

When a consequential relation has enough support to influence placement or routing, prefer recording it explicitly using `schema/relation.schema.json`, typically in `relations.jsonl`.

Do not emit a relation merely because two entities co-occur. Preserve scope, evidence state, provenance, perspective, valid time when relevant, and routing safety.

Human-readable summaries remain required. Relation records make later federation and challenge less dependent on re-parsing prose.

## Trust/share workflow

A shareable session should contain the standardized files and pass:

```bash
python3 tools/validate_session.py sessions/<id>
python3 tools/seal_session.py sessions/<id>
python3 tools/verify_session.py sessions/<id>
```

Recipients should be able to answer: Which protocol version produced this? Who operated the session? Who was the participant? What did the model know before interviewing the participant? What did it predict? What evidence did it inspect? What changed after the interview? What did the participant challenge? Which claims and relations are safe vs provisional? Has the package changed since it was sealed?

## Fail review if the model

- invents facts for coherence,
- rewrites its pre-interview prediction after seeing answers,
- treats prediction accuracy as a participant score,
- treats title/authorship/activity as proof of authority/expertise,
- scans beyond granted scope,
- merges conflicting perspectives into one unqualified fact,
- penalizes “I don't know,”
- emits personality typing instead of placement,
- routes responsibility from relevance alone,
- treats capability as permission or authority,
- asks broad low-information questions after a consequential ambiguity is visible,
- omits negative boundaries,
- hides participant challenges,
- claims hash verification proves factual truth,
- exceeds 30 minutes without marking the session late/partial.

## Comparing models

Use the same seed pack and purpose, but allow different questions. Compare factual precision, calibration of pre-interview predictions, provenance, useful uncertainty, placement quality, discovery of missing axes, probe efficiency, correction behavior, time restraint, relation quality, and handoff quality.
