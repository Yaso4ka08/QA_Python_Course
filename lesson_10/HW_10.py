import allure
import pytest

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, department, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.department = department

class Developer(Employee):
    def __init__(self, program_language, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.program_language = program_language

class TeamLead(Manager,Developer):
    def __init__(self, name, salary, program_language, department, team_size):
        super().__init__(
            name=name,
            salary=salary,
            program_language=program_language,
            department=department
        )
        self.team_size = team_size

@pytest.mark.parametrize(
    "name, salary, program_language, department, team_size",
    [
        ("Alice", 5000, "Java", "Development", 4),
        (None, 3000, "PHP", "Development", 2), # Name comes empty
        ("Bob", None, "Java", "QA", 3), # Salary comes empty
        ("Diana", 4000, None, "Management", 7),  # Program language comes empty
        ("Michael", 6000, "DevOps", None, 4), # Department comes empty
        ("Charlie", 9000, "SQL", "Analytics", None) # Team size comes empty

   ]
)
@allure.feature("Team Lead checks")
def test_teamlead_arguments_validation(
    name, salary, program_language, department, team_size
):
    lead = TeamLead(
        name=name,
        salary=salary,
        department=department,
        program_language=program_language,
        team_size=team_size
    )

    with allure.step("Checking if department is in the lead"):
        assert lead.department is not None

    with allure.step("Checking if program language is in the lead"):
        assert lead.program_language is not None




