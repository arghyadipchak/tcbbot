import requests

##parameter = {'is_cracked':'true'}

request = requests.get('https://api.crackwatch.com/api/games')

##print(request.text)

request_json=request.json()
print(request_json)
##for i in range(0,len(request_json)):
##  print(request_json[i]['title'])

string='Devil May Cry 6'

string=input('Enter game name : ')

text=''
for i in string:
  if(i!=' '):
    text=text+i.lower()
  else:
    text=text+'-'
print(text)

for i in range(0,len(request_json)):
  if(request_json[i]['slug']==text):
    print(request_json[i]['title'])



