#!/usr/bin/env python3
import random, json, time, shutil
from pathlib import Path
ROOT = Path("/home/opc/self-improving-ai")
STATE = ROOT / "math_state.json"
LOG = ROOT / "daily_log.md"
def load():
    return json.loads(STATE.read_text()) if STATE.exists() else {"level":1,"correct":0,"total":0}
def save(s): STATE.write_text(json.dumps(s))
def ok():
    t,u,f = shutil.disk_usage("/")
    if u/t > 0.9: return False
    m = open("/proc/meminfo").read()
    mt = int([l for l in m.splitlines() if "MemTotal" in l][0].split()[1])
    ma = int([l for l in m.splitlines() if "MemAvailable" in l][0].split()[1])
    if (1-ma/mt) > 0.90: return False
    if float(open("/proc/loadavg").read().split()[0]) > 8.0: return False
    return True
def prob(lv):
    if lv==1: a,b=random.randint(1,50),random.randint(1,50); return f"{a}+{b}",a+b
    if lv==2: a,b=random.randint(2,20),random.randint(2,20); return f"{a}*{b}",a*b
    if lv==3: a,b=random.randint(2,8),random.randint(2,5); return f"{a}**{b}",a**b
    a,b=random.randint(1,20),random.randint(21,100); return f"x+{a}={b}",b-a
s=load(); n=0; st=time.time()
while ok() and time.time()-st<45:
    e,a=prob(s["level"])
    try: c = True if s["level"]>=4 else eval(e)==a
    except: c=False
    s["total"]+=1
    if c:
        s["correct"]+=1
        if s["correct"]>=8 and s["level"]<6: s["level"]+=1; s["correct"]=0
    n+=1
    if n%15==0: save(s)
save(s)
line=f"- Math burst: level {s['level']} +{n} problems ({s['correct']}/{s['total']})\n"
open(LOG,"a").write(line)
print(line.strip())
# Log only every 10th cycle to cut I/O
LOG_EVERY = 10
