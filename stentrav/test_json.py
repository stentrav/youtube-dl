import json
import re

def test_parse(encoded):
    decoder = json.JSONDecoder()
    try:
        x = decoder.decode(encoded)
    except StopIteration as err:
        pass
    except json.JSONDecodeError as jde:
        print("Error:"+str(jde))
        m_json = decoder.decode(encoded[0:jde.pos])
        print("got it")
    print("decoded")
    return obj, end

def get_media_defs(doc):
    w = doc[doc.find("mediaDefinition:")+len("mediaDefinition:"):]
f = open("//ALPHA.DAWSON/heap/ytdl/rtube1.dump", "r", encoding="utf-8")
v = f.read()
test_parse(w)

p1 = r'mediaDefinition\s*:\s*(\[.+?\])+'
mobj = re.search(p1, v)
if mobj is not None:
    grps = mobj.groups()
    j1 = mobj.group(0)
    try:
        is_parsable = True
        json.loads(j1)
    except Exception as exc:
        is_parsable = False
        print(exc)

print(v)
