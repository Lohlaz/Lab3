import employee_info

def test_get_employees_by_age_range():
    lower_limit = 0
    upper_limit = 70000
    results = []
    results = employee_info.get_employees_by_age_range(lower_limit,upper_limit)
    employee_info.display_records(results)

def test_calculate_average_salary():
    average = employee_info.calculate_average_salary()
    assert (average)
    print(average)


def test_employees_by_dept():
    department = "Marketing"
    result = employee_info.get_employees_by_dept(department)
    employee_info.display_records(result)
    assert (result)


