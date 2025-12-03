class Employee:
    def __init__(self, name, position, experience_years):
        self.name = name
        self.position = position
        self.experience_years = experience_years

    def get_experience_bonus(self):
        if self.experience_years < 5:
            return 5
        elif 5 <= self.experience_years <= 10:
            return 10
        else:
            return 15