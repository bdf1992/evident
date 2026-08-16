#!/usr/bin/env python3
from pathlib import Path
import argparse,json,hashlib,sys
p=argparse.ArgumentParser(); p.add_argument('session_dir'); args=p.parse_args(); d=Path(args.session_dir); errors=[]
try:
 mbytes=(d/'manifest.json').read_bytes(); m=json.loads(mbytes); r=json.loads((d/'receipt.json').read_text())
 if hashlib.sha256(mbytes).hexdigest()!=r.get('manifest_sha256'): errors.append('manifest hash does not match receipt')
 for f in m.get('files',[]):
  pth=d/f['path']
  if not pth.exists(): errors.append(f"missing sealed file {f['path']}"); continue
  if hashlib.sha256(pth.read_bytes()).hexdigest()!=f['sha256']: errors.append(f"hash mismatch {f['path']}")
except Exception as e: errors.append(str(e))
if errors:
 print('FAIL'); [print('-',e) for e in errors]; sys.exit(1)
print('PASS')
