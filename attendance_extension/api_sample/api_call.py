import requests
import base64
import json

"""
RPC: /api/method/frappe.core.doctype.user.user?user="user_name"
Command: bench execute frappe.core.doctype.user.user --args ['user_name']
Web: User -> Api Access -> Generate Keys
"""

api_key = "API_KEY"
api_secret = "API_SECRET"

headers = {
    'Authorization': "token %s:%s" % (api_key, api_secret)
}

url = "http://erp/api/method/frappe.auth.get_logged_user"
response = requests.request("GET", url, headers=headers)
print(response.status_code)

url = "http://erp/api/method/frappe.client.get_time_zone"
response = requests.request("GET", url, headers=headers)
print(response.status_code)

url = "http://erp/api/method/attendance_extension.attendance_extension.doctype.attendance_settings.tasks.test"
response = requests.request("GET", url, headers=headers, data=json.dumps)
print(response.status_code)


