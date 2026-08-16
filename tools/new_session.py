#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime, timezone
import argparse, json, shutil

FILES = ["organization.md", "participant.md", "unknowns.md", "handoff.md"]
p=argparse.ArgumentParser(); p.add_argument('session_dir'); p.add_argument('--participant',default=''); p.add_argument('--scope',default=''); p.add_argument('--purpose',default=''); args=p.parse_args()
root=Path(__file__).resolve().parents[1]; out=Path(args.session_dir); out.mkdir(parents=True,exist_ok=False)
for n in FILES: shutil.copy(root/'templates'/n,out/n)
for n in ['facts.jsonl','prediction.jsonl','challenges.jsonl']: (out/n).write_text('',encoding='utf-8')
now=datetime.now(timezone.utc).isoformat()
s={"session_id":out.name,"protocol_version":"0.2.0","start":now,"end":"","duration_minutes":0,"status":"partial","scope":args.scope,"purpose":args.purpose,"participant":args.participant,"model":None,"prior_session_receipts":[],"sources_allowed":[],"sources_inspected":[],"excluded_sources":[],"prediction_frozen_at":None,"notes":"Session initialized; seal at compile phase."}
(out/'session.json').write_text(json.dumps(s,indent=2)+'\n',encoding='utf-8'); print(out)
