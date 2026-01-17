class User:
    def __init__(self, age, gender, income, utilities, entertainment,
                 school_fees, shopping, healthcare):
        self.age = int(age)
        self.gender = gender
        self.income = float(income)
        self.utilities = float(utilities)
        self.entertainment = float(entertainment)
        self.school_fees = float(school_fees)
        self.shopping = float(shopping)
        self.healthcare = float(healthcare)

    def to_dict(self):
        return {
            "age": self.age,
            "gender": self.gender,
            "income": self.income,
            "utilities": self.utilities,
            "entertainment": self.entertainment,
            "school_fees": self.school_fees,
            "shopping": self.shopping,
            "healthcare": self.healthcare
        }

    def to_list(self):
        return [
            self.age,
            self.gender,
            self.income,
            self.utilities,
            self.entertainment,
            self.school_fees,
            self.shopping,
            self.healthcare
        ]
