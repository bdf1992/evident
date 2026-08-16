# Organizational Discovery Playbook

This playbook teaches a model how to discover an unfamiliar organization during an Evident 30 session. It is not a questionnaire. Use it to choose the next useful distinction.

## Start from work, not title

Begin with what enters the participant's world, what they do with it, and what leaves changed.

Ask enough to locate:

- **work** — requests, decisions, artifacts, incidents, cases, transactions, responsibilities;
- **actors** — people, teams, agents, services, vendors, governing bodies;
- **objects/systems** — things the work acts on or passes through;
- **flow** — inputs, outputs, handoffs, crossings, routing;
- **power** — capability, permission, authority, approval, accountability;
- **boundaries** — where the participant stops being a valid route;
- **dependencies** — what must be available, correct, approved, or inherited;
- **time** — current vs historical, temporary vs persistent, normal vs exception;
- **failure** — what breaks, who notices, who can repair, who decides;
- **evidence** — why an important relation should be believed.

Do not require every category to be populated. Treat a conspicuous absence as a candidate unknown or next probe.

## Organizational scan

When entering an unfamiliar space, scan for these questions:

### WHERE
What space or subspace is in scope? What is outside it? Which boundaries can work cross?

### WHO
Who participates, governs, supplies, receives, approves, supports, or is affected?

### WHAT
What work, objects, systems, records, services, or resources matter?

### HOW
How does work actually move? What is the normal path? What changes in exceptions?

### POWER
Who can do something? Who may do it? Who decides? Who is accountable afterward?

### FLOW
Where does work enter, leave, wait, transform, escalate, or get routed?

### FAILURE
Who detects failure? Who can repair it? Who owns recovery? Who may accept risk?

### TIME
What is stable, temporary, inherited, historical, scheduled, or session-scoped?

### EVIDENCE
Which claims are declared, documented, observed, inferred, contested, or unknown?

### UNKNOWN
Which unresolved distinction would most change routing or placement?

## Probe priority

Prefer a probe when it has high expected information value:

`probe value ≈ uncertainty × organizational consequence × routing consequence × participant resolvability`

This is a heuristic, not a numeric score. A question is usually low value when the answer is already established or cannot affect placement. A question is high value when nearby interpretations would route work differently.

Examples:

- Low value: re-asking who assigns work after that relation is already established.
- High value: asking whether the person who updates deployment status may also approve a deployment.
- High value: asking whether an apparent local rule is inherited from a parent organization.
- High value: asking who handles the exception path when the normal owner is unavailable.

## Claim-neighbor branching rule

Whenever an important claim appears:

1. Record what was actually established.
2. Ask whether the claim affects placement, authority, or routing.
3. If yes, identify the nearest alternative interpretation that would materially change the model.
4. Probe that distinction.
5. Stop branching when the remaining ambiguity has low organizational consequence.

Example:

Participant: "I maintain deployment status."

Do not silently expand this to deployment ownership. Candidate neighboring distinctions include:

- update vs approve;
- report vs operate;
- normal path vs incident path;
- application vs infrastructure;
- local authority vs inherited authority;
- capability vs permission;
- current duty vs historical familiarity.

Probe only the neighbors that would matter for the session purpose.

## Work-to-boundary traversal

A reliable path when the interview is stuck is:

`work -> object/system -> flow -> dependency -> capability -> authority -> accountability -> exception -> boundary -> routing`

Do not force this sequence when another branch is more informative. It is a recovery path, not a form.

Useful moves:

- **Work:** "What reaches you that requires action?"
- **Object/system:** "What do you actually touch or change?"
- **Flow:** "Where did it come from, and where does it go next?"
- **Dependency:** "What must be true before you can act?"
- **Capability:** "What can you technically do?"
- **Authority:** "Which of those actions are you allowed to decide yourself?"
- **Accountability:** "Who remains responsible for the outcome?"
- **Exception:** "What changes when the normal path fails?"
- **Boundary:** "What nearby work would be wrong to send to you?"
- **Routing:** "Who should receive that instead?"

## Distinctions worth preserving

Especially test these when they are easy to collapse:

- title vs actual work;
- knowledge vs responsibility;
- capability vs permission;
- permission vs authority;
- authority vs accountability;
- participation vs ownership;
- information ownership vs physical/system ownership;
- normal path vs exception path;
- local practice vs parent/inherited rule;
- temporary/session role vs durable organizational role;
- can-access vs may-inspect;
- can-execute vs may-execute-now;
- current vs historical familiarity;
- absence vs not observed;
- contradiction vs legitimate perspective difference.

## Evidence selection

Evidence checks should resolve a live distinction, not merely accumulate documents.

Before opening a source, state which claim or branch it could support, narrow, contradict, or leave unresolved. Prefer the smallest authorized source that can answer the question.

Do not use evidence volume as a confidence substitute.

## Challenge presentation

Do not ask only "Does this look right?" Present the participant with a falsifiable emerging map:

- strongest positive routes;
- explicit do-not-route boundaries;
- authority and accountability limits;
- important dependencies;
- prediction deltas;
- one or two weakest assumptions;
- unresolved contradictions;
- what the model would currently tell another participant to do.

Invite corrections by relation: "Which arrow, boundary, or label is wrong? What is missing?"

## Stop rule inside the interview

Stop exploring a branch when one of these is true:

- the routing consequence is established;
- further detail would not change placement;
- the participant cannot resolve it and an evidence/handoff path is known;
- it is outside scope;
- the remaining distinction is lower value than another unresolved branch.

Depth on a few consequential relations is better than broad organizational trivia.
