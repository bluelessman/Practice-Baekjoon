import re
s = input()
slist = s.split('-',maxsplit=1)
if len(slist)==1:
  print(sum(map(int,slist[0].split('+'))))
else:
  print(sum(map(int,slist[0].split('+')))-sum(map(int,re.split(r'-|\+',slist[-1]))))