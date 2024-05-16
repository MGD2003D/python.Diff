from src.lab4.survey_sorter.models.age_group import AgeGroup
from src.lab4.survey_sorter.models.respondent import Respondent

class SurveyProcessor:
    def __init__(self, age_bounds):
        self.age_groups = []
        prev_bound = 0
        for bound in age_bounds:
            self.age_groups.append(AgeGroup(prev_bound, bound))
            prev_bound = bound + 1
        if age_bounds[-1] < 123:
            self.age_groups.append(AgeGroup(prev_bound, 123))

    def process_respondents(self, input_lines):
        for line in input_lines:
            full_name, age = line.split(',')
            age = int(age)
            if age <= 123:
                respondent = Respondent(full_name, age)
                for group in self.age_groups:
                    group.add_respondent(respondent)

    def get_results(self):
        return "\n".join(str(group) for group in self.age_groups if str(group))