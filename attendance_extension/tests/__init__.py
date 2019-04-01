# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals

import frappe
from werkzeug.wrappers import Request
from werkzeug.test import EnvironBuilder

def set_request(**kwargs):
	builder = EnvironBuilder(**kwargs)
	frappe.local.request = Request(builder.get_environ())

def insert_test_data(doctype, sort_fn=None):
	pass

