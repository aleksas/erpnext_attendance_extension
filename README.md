## Attendance Extension

ERPNext Attendance DocType Extension

**ONLY FOR FRAPPE/ERPNEXT v11 (master branch)**

### Install
Install attendance_extension app using commandline `bench`

```sh
cd /path/to/frappe-bench
bench get-app https://github.com/aleksas/erpnext_attendance_extension.git
bench install attendance_extension
bench migrate
```

_See [Bench Commands Cheatsheet](https://frappe.io/docs/user/en/bench/resources/bench-commands-cheatsheet.html) for details._

This will create two DocTypes: `Attendance Settings` and `Attendance Detail` in `Attendance Extension` module. Also this app will alter `Attendance` DocType to include 'Attendance Detail' list.

_Also see [App Tutorials](https://frappe.io/docs/user/en/tutorial)._

#### External attendance api

In `/path/to/frappe-bench/apps/attendance_extension/attendance_extension/attendance_extension/doctype/attendance_settings` directory you'll find [external_api.py](https://github.com/aleksas/erpnext_attendance_extension/blob/master/attendance_extension/attendance_extension/doctype/attendance_settings/external_api.py) Python script containing stab functions. These stub functions should be modified in order to access data from external attendace api.

If you run 

```sh
cd /path/to/frappe-bench
bench execute attendance_extension.attendance_extension.doctype.attendance_settings.tasks.test
```

it should generate some stub attendance records (haven't checked stub test myself).

##### IMPORTANT

If you are not going to use scheduled attendance updates (from external attendance info source) you have to comment regular task calls in [hooks.py](https://github.com/aleksas/erpnext_attendance_extension/blob/master/attendance_extension/hooks.py#L97-L109). You can find this file in `/path/to/frappe-bench/apps/attendance_extension/attendance_extension` directory.

### License

MIT
