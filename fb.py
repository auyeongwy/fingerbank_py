# Copyright 2019 Au Yeong Wing Yau
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
A script to interface with the FingerBank REST API
Usage:

python3 fb.py <command> [arguments]
"""

import fb_config
import sys
import http.client
import json
import urllib
import argument_parser



def create_interrogate_url(p_config):
	"""
	Constructs the URL for the interrogate request
	:param p_config: A fb_config.fb_config object that contains the configuration parameters
	:return: The URL to use for the REST request.
	"""
	url = '/api/v2/combinations/interrogate'
	params = {}
	if hasattr(p_config, 'api_key'):
		params['key'] = p_config.api_key

	if len(params) > 0:
		url = url+'?'+urllib.parse.urlencode(params)
	return url



def create_payload(p_config):
	"""
	Constructs the payload for the REST request
	:param p_config: An fb_config.fb_config object that contains the configuration parameters
	"""
	payload = {}
	if hasattr(p_config, 'user_agents'):
		payload['user_agents'] = p_config.user_agents
	if hasattr(p_config, 'mac'):
		payload['mac'] = p_config.mac
	if hasattr(p_config, 'dhcp_fingerprint'):
		payload['dhcp_fingerprint'] = p_config.dhcp_fingerprint
	if hasattr(p_config, 'dhcp6_fingerprint'):
		payload['dhcp6_fingerprint'] = p_config.dhcp6_fingerprint

	if len(payload) > 0:
		payload = json.dumps(payload)

	return payload



def create_header():
	"""
	Constructs the header for the REST request
	"""
	header = {}
	header['Content-type'] = 'application/json'
	return header



"""
Main function starts here.
"""
(result, v_operation, v_argument) = argument_parser. parse_arguments(sys.argv)
if result == 0:
	sys.exit()


""" Load the config file """
try:
	config = fb_config.fb_config("config.real")
except Exception as excep:
	print(excep.args[0])
	sys.exit()

""" Prepare the REST url """
if v_operation == 'interrogate':
	v_url = create_interrogate_url(config)
else:
	sys.exit()

""" Create a JSON payload """
v_payload = create_payload(config)


""" Send the request """
try:
	v_client_conn = http.client.HTTPSConnection('api.fingerbank.org')
	v_client_conn.request("POST", v_url, v_payload, create_header())
	response = v_client_conn.getresponse()
except http.client.HTTPException as he:
	print(he.args[0])
	sys.exit


""" Work with the results """
print(response.status, response.reason)
if response.status != 200:
	print(response.read())

else:
	v_result = (response.read()).decode('utf-8')
	print(json.dumps(json.loads(v_result), indent=2, sort_keys=True))

v_client_conn.close()
