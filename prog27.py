import json
with open("userinfo.json","r")as fb:
   y=fb.read()
   m=json.loads(y)
   m["kmv"]=200
   print(m)
with open("userinfo.json","w")as fb:
    fb.write(json.dumps(m))

'''import json
d={"kmv":123, "vmk":456}
with open("userinfo.json","w")as fb:
   fb.write(json.dumps(d,indent=4))'''
