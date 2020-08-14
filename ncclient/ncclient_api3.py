
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
"cmd": "show version",
"version": 1.2
},
"id": 1
}
]
response = requests.post(url,data=json.dumps(payload), headers=myheaders,
auth=(switchuser,switchpassword)).json()

print(response)

print(response['result']['body']['chassis_id'])
print(response['result']['body']['nxos_file_name'])

#print(k)
