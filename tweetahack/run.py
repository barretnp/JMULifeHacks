from tweet import Tweet
import time
import json

try:
    f = open('since_id', 'r')
    sid = json.load(f)
    f.close()
except:
    sid = 1
    f = open('since_id', 'w')
    json.dump(sid, f)
    f.close()

f = open('since_id', 'w')

t = Tweet(since_id=sid)
while True:
    try:
        t.maintain()
        sid = t.since_id
        json.dump(sid,f)
        time.sleep(5*60)
    except KeyboardInterrupt, e:
        break

print sid
f.close()
