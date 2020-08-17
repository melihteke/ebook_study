
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
"cmd": "show interface brief",
"version": 1.2
},
"id": 1
}
]
response = requests.post(url,data=json.dumps(payload), headers=myheaders,
auth=(switchuser,switchpassword)).json()

print(response)
print(json.dumps(response, indent=2, sort_keys=True))  #printing json file

with open('output_interface.txt', 'w') as f:
  print("Output is being generated !!!")
  f.write(json.dumps(response, indent=2, sort_keys=True))
f.close()

with open('output_interface.txt', 'r') as f:
  read_json_var = json.load(f)   #

#'''Note regarding json.load vs json.loads
#The json. load() is used to read the JSON document from file and The json. loads() is used to convert the JSON String document into the Python dictionary.
#'''


print("'\n'")
print("Now json data is being parsed  based on state")

for i in range(1,128):
  #print("Creating VLAN " + str(n))
  print("interface Ethernet1/" + str(i) + ":    " + read_json_var['result']['body']["TABLE_interface"]['ROW_interface'][i]['state'] )
  #print(read_json_var['result']['body']["TABLE_interface"]['ROW_interface'][i]['state'])



#print(response['result']['body']['chassis_id'])
#print(response['result']['body']['nxos_file_name'])

#print(k)
