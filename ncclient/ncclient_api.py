#!/usr/bin/env python3
from ncclient import manager
conn = manager.connect(
host='192.168.178.142',
port=22,
username='admin',
password='cisco1985',
hostkey_verify=False,
device_params={'name': 'nexus'},
look_for_keys=False
)

for value in conn.server_capabilities:
	print(value)

conn.close_session()


#Here is the output
#root@server:/home/python_examples/ncclient# python3 first_ncc_example.py
#urn:ietf:params:netconf:capability:writable-running:1.0
#urn:ietf:params:netconf:capability:url:1.0?scheme=file
#urn:ietf:params:netconf:capability:candidate:1.0
#urn:ietf:params:netconf:capability:rollback-on-error:1.0
#urn:ietf:params:netconf:capability:confirmed-commit:1.0
#urn:ietf:params:netconf:base:1.0
#urn:ietf:params:netconf:capability:validate:1.0
#urn:ietf:params:xml:ns:netconf:base:1.0
#root@server:/home/python_examples/ncclient#

#INSTALL ncclient:
#(venv) $ git clone https://github.com/ncclient/ncclient
#(venv) $ cd ncclient/
#(venv) $ python setup.py install
