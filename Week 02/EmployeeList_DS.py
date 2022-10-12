"""
    Employee who are working in a restaurant.
    You need to be able to find an employee by their employee ID - an integer-based numeric ID.
    The function get_employee contains a for loop to iterate over the list of employees and returns an employee object if the ID matches.
"""
# employee list of dictionary
employee_list = [{"id": 1234, "name": "John", "Department": "Kitchen"},
                 {"id": 4321, "name": "Tony", "Department": "Reception"},
                 {"id": 1234, "name": "Hammer", "Department": "Kitchen"}, ]


# function for fetching employee details
def get_employee(id):
    for employee in employee_list:
        # comparing `id` for employee details
        if employee['id'] == id:
            return employee


# Calling function get_employee
print(get_employee(4321))

# Now same example using dictionary
employee_dict = {
    12345: {
        "id": "12345",
        "name": "John",
        "department": "Kitchen"
    },
    12458: {
        "id": "12458",
        "name": "Paul",
        "department": "House Floor"
    }
}


def get_employee_from_dict(id):
    return employee_dict[id]


print(get_employee_from_dict(12458))
