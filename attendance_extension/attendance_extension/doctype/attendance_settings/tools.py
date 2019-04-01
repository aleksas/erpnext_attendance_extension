from frappe.utils.background_jobs import enqueue
from frappe import get_single, get_all, get_doc
from attendance_extension.attendance_extension.doctype.attendance_settings.external_api import get_user_map, get_events
from datetime import datetime, timedelta, date

def update_attendance_from_external_api(start_date, is_async=True, queue='default'):
    external_api_root_url = get_single('Attendance Settings').external_api_url
    employees = get_all_active_employees()
    employees = {e['company_email'].strip():e for e in employees}
    external_email_map, _ = get_user_map(external_api_root_url)

    for email, username in external_email_map.items():
        enqueue(
            'attendance_extension.attendance_extension.doctype.attendance_settings.tools.update_employee_attendance_from_external_api_internal', 
            queue=queue, 
            is_async=is_async, 
            start_date=start_date, 
            email=email, 
            external_username=username, 
            external_api_root_url=external_api_root_url)

def update_employee_attendance(start_date, email):
    external_api_root_url = get_single('Attendance Settings').external_api_url
    external_email_map, _ = get_user_map(external_api_root_url)
    if email not in external_email_map.keys():
        return #ToDo: fix hack. not all external users may have email
    update_employee_attendance_internal(
        start_date, 
        email, 
        external_email_map[email], 
        external_api_root_url)

def update_employee_attendance_from_external_api_internal(start_date, email, external_username, external_api_root_url=None, include_attendance=True):
    if not external_api_root_url:
        external_api_root_url = get_single('Attendance Settings').external_api_url

    if isinstance(start_date, datetime):
        start_date = start_date.date()

    past_days = (date.today() - start_date).days + 1

    emp_ = get_employee(email)
    if not emp_:
        return 
    employee, company = emp_

    for days in range(past_days):
        time_logs = []
        dt = (start_date + timedelta(days = days))
        events = get_events(external_api_root_url, external_username, dt)
        if events and len(events) > 0:
            for event in events:
                if event['Status'] != 'Valid' and event['Status'] != 'Check-in':
                    continue
                event_timestamp = event['datetime'].isoformat(sep=' ')

                if len(time_logs) == 0 or "to_time" in time_logs[-1]:
                    time_logs.append({})
                        
                if "from_time" not in time_logs[-1]:
                    time_logs[-1]["from_time"] = event_timestamp
                else:
                    time_logs[-1]["to_time"] = event_timestamp

            if len(time_logs) != 0 and "to_time" not in time_logs[-1]:
                time_logs[-1]["to_time"] = None

            update_attendance(
                employee, 
                (start_date + timedelta(days = days)).strftime('%Y-%m-%d'), 
                company, 
                time_logs)

def add_attendance(employee, date, time_logs, company):
    d_ = {'doctype': 'Attendance',
        'attendance_date': date,
        'company': company,
        'employee': employee,
        'time_logs': time_logs}

    attendance = get_doc(d_)
    attendance.insert()
    attendance.submit()

    return attendance

def get_employee(email, company=None):
    filters = {'company_email': email}
    if company:
        filters['company'] = company

    for doc in get_all('Employee', filters=filters, fields=['employee', 'company']):
        return doc.employee, doc.company

def get_all_active_employees(company=None):
    filters = {'status': 'Active'}
    if company:
        filters['company'] = company

    return get_all('Employee', filters=filters, fields=['employee', 'company', 'company_email'])

def find_attendance(employee, date, company=None):
    params = {'employee':employee, 'attendance_date':date}
    if company:
        params['company'] = company
    doc = get_all('Attendance', filters=params, fields=['name'])
    if len(doc) > 0:
        return get_doc('Attendance', doc[0]['name'])

def update_attendance(employee, start_date_str, company, time_logs):
    attendance = find_attendance(employee, start_date_str, company)

    if attendance:
        attendance.update({'time_logs': time_logs})
        attendance.save()
    else:
        add_attendance(employee, start_date_str, time_logs, company)
