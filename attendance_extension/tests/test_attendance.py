# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt
from __future__ import unicode_literals

import frappe, unittest
from attendance_extension.attendance_extension.doctype.attendance_settings.tasks import test

class TestAttendance(unittest.TestCase):
	def test_attendance_hourly(self):
		test()
