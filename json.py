import simplejson as json

user=input("enter one string")
with open('error.json') as fileObject:
  fileContents = fileObject.read()
  r = json.loads(fileContents)
j=0
while True:
  a=r['values'][j]['from']
  if user in a:
    print(r['values'][j]['to'])
    break
  j+=1
#print(r)
#a=r['values'][0]['from']
#print(r['values'][0]['from'])
#if user in a:
#  print(r['values'][0]['to'])
#data=json.loads(string)
#print(data)