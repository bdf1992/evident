#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime, timezone
import argparse,json,hashlib
EXCLUDE={'manifest.json','receipt.json'}
p=argparse.ArgumentParser(); p.add_argument('session_dir'); args=p.parse_args(); d=Path(args.session_dir)
if not d.is_dir(): raise SystemExit('session directory not found')
files=[]
for pth in sorted(d.iterdir()):
 if pth.is_file() and pth.name not in EXCLUDE:
  b=pth.read_bytes(); files.append({'path':pth.name,'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)})
manifest={'algorithm':'sha256','sealed_at':datetime.now(timezone.utc).isoformat(),'files':files}
mb=(json.dumps(manifest,indent=2,sort_keys=True)+'\n').encode(); (d/'manifest.json').write_bytes(mb)
s=json.loads((d/'session.json').read_text())
receipt={'session_id':s.get('session_id'),'protocol_version':s.get('protocol_version'),'status':s.get('status'),'scope':s.get('scope'),'participant':s.get('participant'),'model':s.get('model'),'start':s.get('start'),'end':s.get('end'),'duration_minutes':s.get('duration_minutes'),'prediction_frozen_at':s.get('prediction_frozen_at'),'manifest_sha256':hashlib.sha256(mb).hexdigest(),'sealed_at':manifest['sealed_at'],'trust_note':'Integrity/provenance receipt; does not certify factual truth.'}
(d/'receipt.json').write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n'); print(receipt['manifest_sha256'])
