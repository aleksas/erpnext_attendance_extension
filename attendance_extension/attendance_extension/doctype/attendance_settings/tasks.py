# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe 
from datetime import datetime, date, timedelta
from attendance_extension.attendance_extension.doctype.attendance_settings.tools import update_attendance_from_external_api

@frappe.whitelist()
def test():
    hourly(is_async=False)

def hourly(is_async=True):
    start_date = datetime.now()
    update_attendance_from_external_api(start_date, queue='default', is_async=is_async)

def daily():
    start_date =  datetime.now() - timedelta(weeks=1)
    update_attendance_from_external_api(start_date, queue='long')

def weekly():
    start_date =  datetime.now() - timedelta(weeks=4)
    update_attendance_from_external_api(start_date, queue='long')

def monthly():
    start_date =  datetime.now() - timedelta(weeks=52)
    update_attendance_from_external_api(start_date, queue='background')
