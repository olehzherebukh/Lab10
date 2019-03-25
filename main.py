from professor import Professor

default_professor = Professor()
math_professor = Professor(first_name = "Zinoviy",
                           last_name = "Nytrebych",
                           number_of_years_of_teaching = 20,
                           nickname = "trebych",
                           subject_of_teaching = "MatAnaliz",
                           number_of_classes_per_week = 10,
                           chair = "Department of Math")

physics_professor = Professor(first_name = "Oksana",
                           last_name = "Rybak",
                           number_of_years_of_teaching = 16,
                           nickname = "Ruby",
                           subject_of_teaching = "Physics",
                           number_of_classes_per_week = 17,
                           chair = "Department of Physics")

print(default_professor)
print(math_professor)
print(physics_professor)
