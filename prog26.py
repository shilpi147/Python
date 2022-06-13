import json
d={"kmv":123, "vmk":456}
with open("userinfo.json","w")as fb:
   fb.write(json.dumps(d,indent=4))
