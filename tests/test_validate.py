import subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def test_smoke_session_validates():
 r=subprocess.run([sys.executable,str(ROOT/'tools/validate_session.py'),str(ROOT/'tests/first-smoke')],capture_output=True,text=True)
 assert r.returncode==0,r.stdout+r.stderr
