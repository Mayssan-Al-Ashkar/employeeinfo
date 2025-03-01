company_employees = {
    "Engineering": {
        "Alice": {"age": 30, "role": "Software Engineer"},
        "Bob": {"age": 28, "role": "DevOps Engineer"}
    },
    "HR": {
        "Charlie": {"age": 35, "role": "HR Manager"}
    }
}
print("Company Employees:", company_employees)

company_employees["Engineering"]["David"] = {"age": 27, "role": "Data Scientist"}

def count_employees(company):
    total = sum(len(department) for department in company.values())
    return total

print("\nTotal Employees:", count_employees(company_employees))