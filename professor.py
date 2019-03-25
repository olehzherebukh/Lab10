class Professor:
    
    number_of_professors = 0
    
    def __init__(self,
                 first_name = "NoName", last_name = "NoName",
                 number_of_years_of_teaching = 0, nickname = "NoName",
                 subject_of_teaching = "NoName", number_of_classes_per_week = 0,
                 chair = "NoName"):
        self.first_name = first_name
        self.last_name = last_name
        self.number_of_years_of_teaching = number_of_years_of_teaching
        self.nickname = nickname
        self.subject_of_teaching = subject_of_teaching
        self.number_of_classes_per_week = number_of_classes_per_week
        self.chair = chair

    def __del__(self):
        print(self.first_name, 'was deleted')

    def __str__(self):
        return ('first_name = {}, last_name = {}, ' +
                'number_of_years_of_teaching = {}, ' +
                'nickname  = {}, subject_of_teaching  = {}, ' +
                'number_of_classes_per_week = {}, ' +
                'chair = {}').format(self.first_name, self.last_name,
                                    self.number_of_years_of_teaching,
                                    self.nickname, self.subject_of_teaching,
                                    self.number_of_classes_per_week,
                                    self.chair)
                                    
    @staticmethod
    def get_number_of_professors():
        return Proffesor.number_of_professors

    

    
    
