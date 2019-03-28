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



import configparser

class fb_config:
	"""
	Manages reading the config file parameters into variables.
	Usage:

	import fb_config

	try:
	my_config = fb_config.fb_config("configfile")
	except Exception as except:
		print(except.args[0])
		print("Abort")
		sys.exit()

	print(vars(my_config))
	"""

	def read_fingerprint_config(self, p_config):
		"""
		Reads config options from the "Fingerprint" part of the config file into the current object's variables.
		:param p_config: The configparser.ConfigParser object that has opened the config file.
		"""
		if "user_agents" in p_config["Fingerprint"]:
			self.user_agents = p_config["Fingerprint"]["user_agents"]
		if "mac" in p_config["Fingerprint"]:
			self.mac = p_config["Fingerprint"]["mac"]
		if "dhcp_fingerprint" in p_config["Fingerprint"]:
			self.dhcp_fingerprint = p_config["Fingerprint"]["dhcp_fingerprint"]
		if "dhcp6_fingerprint" in p_config["Fingerprint"]:
			self.dhcp6_fingerprint = p_config["Fingerprint"]["dhcp6_fingerprint"]
		if "dhcp_vendor" in p_config["Fingerprint"]:
			self.dhcp_vendor = p_config["Fingerprint"]["dhcp_vendor"]
		if "dhcp6_enterprise" in p_config["Fingerprint"]:
			self.dhcp6_enterprise = p_config["Fingerprint"]["dhcp6_enterprise"]
		if "destination_hosts" in p_config["Fingerprint"]:
			self.destination_hosts = p_config["Fingerprint"]["destination_hosts"]
		if "mdns_services" in p_config["Fingerprint"]:
			self.mdns_services = p_config["Fingerprint"]["mdns_services"]
		if "upnp_user_agents" in p_config["Fingerprint"]:
			self.upnp_user_agents = p_config["Fingerprint"]["upnp_user_agents"]
		if "upnp_server_strings" in p_config["Fingerprint"]:
			self.upnp_server_strings = p_config["Fingerprint"]["upnp_server_strings"]
		if "tcp_syn_signatures" in p_config["Fingerprint"]:
			self.tcp_syn_signatures = p_config["Fingerprint"]["tcp_syn_signatures"]
		if "tcp_syn_ack_signatures" in p_config["Fingerprint"]:
			self.tcp_syn_ack_signatures = p_config["Fingerprint"]["tcp_syn_ack_signatures"]
		if "hostname" in p_config["Fingerprint"]:
			self.hostname = p_config["Fingerprint"]["hostname"]			



	def __init__(self, p_file):
		"""
		Reads config options from a configuration file into this object.
		:param p_file: The configuration file.
		"""
		config = configparser.ConfigParser()
		if len(config.read(p_file)) == 0:
			raise Exception("Config file error.")

		if "API_KEY" in config["Key"]:
			self.api_key = config["Key"]["API_KEY"]
		else:
			"""If API key is missing just give up."""
			raise Exception("Missing API key.")

		self.read_fingerprint_config(config)
