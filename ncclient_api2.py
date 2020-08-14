
"""
NX-API-BOT
"""
import requests
import json

url='http://192.168.178.142/ins'
switchuser='admin'
switchpassword='cisco1985'
myheaders={'content-type':'application/json-rpc'}

payload=[
{
"jsonrpc": "2.0",
"method": "cli",
"params": {
"cmd": "show vdc",
"version": 1.2
},
"id": 1
}
]
response = requests.post(url,data=json.dumps(payload), headers=myheaders,
auth=(switchuser,switchpassword)).json()
print(response)
print(json.dumps(response, indent=2, sort_keys=True))  #printing json file

