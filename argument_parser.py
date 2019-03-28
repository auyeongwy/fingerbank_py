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


def print_help():
	"""
	Prints the help text.
	"""
	print("Help text")



def parse_arguments(p_args):
	"""
	Parses input arguments at the command line.
	:param p_args: The python sys.args object.
	:return: A set (result, command, arguments). If result=0, the input arguments have an error. "command" is one of the commands suported my the fingerbank API - 'interrogate', 'id', etc. "arguments" is valid only if the "command" needs an additional argument. Otherwise it returns None.
	"""
	result = 0
	command = None
	argument = None

	if len(p_args) < 2:
		print("Incorrect arguments.")
		print_help()

	elif p_args[1] not in ['interrogate']:
		print("Incorrect arguments.")
		print_help()

	else:
		result = 1
		command = p_args[1]

	return (result, command, argument)
