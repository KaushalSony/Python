import json
n=int(input('enter no. of elements'))
dict={}
for i in range(n):
    key=input('enter key')
    value=input('enter value')
    dict[key]=value
print(json.dumps(dict,indent=5,sort_keys=True))