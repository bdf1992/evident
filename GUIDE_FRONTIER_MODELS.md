# Guide for Frontier Models

## Operator prompt

> Start an Evident 30 session with me. Treat 30 minutes as a hard wall-clock investigation budget. Freeze a pre-interview prediction from the supplied/common factual baseline before substantive interview questions. Follow the evidence policy. Do not assume access implies permission. Ask adaptive probes. Show me what your prediction got wrong or had to narrow. Give me a correction/challenge step. Compile and seal the session with the trust receipt when time expires or the stop rule is met.

If the model cannot reliably track wall time, use an external timer.

## Before the session

Optionally prepare a small factual seed pack: official names, dated org charts, registered products/services, repository existence/README text, policies/runbooks, issue metadata, system inventories, published role descriptions, schemas/configuration. Keep interpretation out.

## Prediction discipline

Before participant evidence, the model must state a small set of predictions. Predictions are hypotheses, not scores and not truths. Good predictions are relations worth testing, e.g. “Given the registered role and runbook, Chen is likely a routing target for dispatch status, but purchase approval is not established.”

Do not predict protected traits, sensitive personal attributes, personality, health, politics, or other irrelevant private characteristics. Predict only organizational relations needed for the stated purpose.

## Trust/share workflow

A shareable session should contain the standardized files and pass:

```bash
python3 tools/verify_session.py sessions/<id>
```

Recipients should be able to answer: Which protocol version produced this? What did the model know before interviewing the participant? What did it predict? What evidence did it inspect? What changed after the interview? What did the participant challenge? Which claims are safe vs provisional? Has the package changed since it was sealed?

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
- omits negative boundaries,
- hides participant challenges,
- claims hash verification proves factual truth,
- exceeds 30 minutes without marking the session late/partial.

## Comparing models

Use the same seed pack and purpose, but allow different questions. Compare factual precision, calibration of pre-interview predictions, provenance, useful uncertainty, placement quality, discovery of missing axes, correction behavior, time restraint, and handoff quality.
