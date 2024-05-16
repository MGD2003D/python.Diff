class AgeGroup:
    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.respondents = []

    def add_respondent(self, respondent):
        if self.lower_bound <= respondent.age <= self.upper_bound:
            self.respondents.append(respondent)
            self.respondents.sort(key=lambda x: (-x.age, x.full_name))

    def __str__(self):
        group_label = f"{self.lower_bound}-{self.upper_bound}+"
        respondents_str = ", ".join(str(res) for res in self.respondents)
        return f"{group_label}: {respondents_str}" if respondents_str else ""