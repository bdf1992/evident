# Trust Receipt

Evident sessions are intended to be shareable without asking recipients to trust the model blindly.

## Trust stack

### 1. Attribution
`session.json` identifies session, protocol version, model identity as reported by the runner, participant representation, purpose, timing, and source boundaries.

### 2. Precommitment
`prediction.jsonl` is frozen before substantive interview answers. This exposes model priors and prevents retrospective claims that the final result was obvious.

### 3. Provenance
`facts.jsonl` connects claims to source references, participant statements, prior sessions, or explicit inference inputs.

### 4. Contestability
`challenges.jsonl` preserves corrections/disputes and their resolution status rather than replacing history.

### 5. Integrity
`manifest.json` contains SHA-256 hashes for shareable session files. `receipt.json` hashes the manifest and summarizes the session.

Run:

```bash
python3 tools/seal_session.py sessions/<id>
python3 tools/verify_session.py sessions/<id>
```

### 6. Minimal disclosure
A session package should reference sensitive source material rather than duplicate it when possible. A recipient may verify integrity of the package without receiving every underlying private artifact.

## What a receipt does not prove

A valid hash proves bytes have not changed since sealing. It does **not** prove the participant was truthful, the model interpreted evidence correctly, a source was current, or an authority endorsed the result.

Trust comes from the combination of scope, provenance, prediction delta, contestability, integrity, and repeatability across later sessions.
