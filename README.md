## Attendance Extension

ERPNext Attendance DocType Extension

### Install
Install attendance_extension app using `bench`

```sh
bench get-app https://github.com/aleksas/erpnext_attendance_extension.git
bench install attendance_extension
bench migrate
```

_See [Bench Commands Cheatsheet](https://frappe.io/docs/user/en/bench/resources/bench-commands-cheatsheet.html) for details._

This will create two DocTypes: `Attendance Settings` and `Attendance Detail` in `Attendance Extension` module. Also this app will alter `Attendance` DocType to include 'Attendance Detail' list.

_Also see [App Tutorials](https://frappe.io/docs/user/en/tutorial)._

#### External attendance api
In `/apth/to/frappe-bench/apps/attendance_extension/attendance_extension/attendance_extension/doctype/attendance_settings` directory you'll find [external_api.py](https://github.com/aleksas/erpnext_attendance_extension/blob/master/attendance_extension/attendance_extension/doctype/attendance_settings/external_api.py) Python script containing stab functions. These stub functions should be modified in order to access data from external attendace api.


#### License

MIT
