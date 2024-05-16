class Respondent:
    def __init__(self, full_name, age):
        self.full_name = full_name
        self.age = age

    def __str__(self):
        return f"{self.full_name} ({self.age})"