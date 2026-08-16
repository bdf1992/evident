#!/usr/bin/env python3
from pathlib import Path
import argparse,json,sys
REQUIRED=['organization.md','participant.md','facts.jsonl','prediction.jsonl','challenges.jsonl','unknowns.md','handoff.md','session.json']
STATES={"registered","declared","documented","observed","inferred","verified","contested","unknown"}
p=argparse.ArgumentParser(); p.add_argument('session_dir'); args=p.parse_args(); d=Path(args.session_dir); errors=[]
for n in REQUIRED:
 if not (d/n).exists(): errors.append(f'missing {n}')
try:
 s=json.loads((d/'session.json').read_text()); dur=float(s.get('duration_minutes',0)); status=s.get('status')
 if dur>30 and status!='late': errors.append("duration exceeds 30 minutes but status is not 'late'")
 if dur<=30 and status=='late': errors.append("status is 'late' but duration is within 30 minutes")
 if not s.get('prediction_frozen_at'): errors.append('prediction_frozen_at missing')
except Exception as e: errors.append(f'invalid session.json: {e}')
for i,line in enumerate((d/'facts.jsonl').read_text().splitlines(),1):
 if not line.strip(): continue
 try:
  x=json.loads(line)
  for f in ('id','statement','scope','state','provenance'):
   if f not in x: errors.append(f'facts.jsonl:{i} missing {f}')
  if x.get('state') not in STATES: errors.append(f'facts.jsonl:{i} invalid state')
 except Exception as e: errors.append(f'facts.jsonl:{i} invalid JSON: {e}')
for i,line in enumerate((d/'prediction.jsonl').read_text().splitlines(),1):
 if not line.strip(): continue
 try:
  x=json.loads(line)
  for f in ('id','statement','scope','basis','confidence','routing_safe','status'):
   if f not in x: errors.append(f'prediction.jsonl:{i} missing {f}')
 except Exception as e: errors.append(f'prediction.jsonl:{i} invalid JSON: {e}')
if errors:
 print('FAIL'); [print('-',e) for e in errors]; sys.exit(1)
print('PASS')
