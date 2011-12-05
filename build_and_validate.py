#!/usr/bin/env python

import os, sys
sys.path.append(os.path.join(sys.path[0], "pyxform", "pyxform"))

def output(message):
	try:
		import ctypes
		MessageBox = ctypes.windll.user32.MessageBoxA
		MessageBox(None, str(message), "XLS2XForm", 0)	
	except Exception as e2:
		# not windows?
		print message

try:
	import xls2xform
	path_to_excel_file = './zambia-ranq-round3.xls'
	survey = xls2xform.create_survey_from_path(path_to_excel_file)
	directory, filename = os.path.split(path_to_excel_file)
	path_to_xform = os.path.join(directory, survey.print_name() + ".xml")
	survey.print_xform_to_file(path_to_xform, False)

	import odk_validate
	odk_validate.check_xform(path_to_xform)
except Exception as e:
	output(e)
	sys.exit(1)

output("Finished!")
sys.exit(0)
