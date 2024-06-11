import json

with open('output.json') as f:
    obj = json.loads(f.read())

a = []
for i in obj:
    b = float(i['_source']['layers']['frame']['frame.time_epoch'])
    a.append(b * 1000)
for i in range(len(a) - 1):
    print(chr(int(round(a[i+1] - a[i]))), end='')
