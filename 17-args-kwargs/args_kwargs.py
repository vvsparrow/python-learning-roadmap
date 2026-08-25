def visitors(teacher="AR", **students):
    print("The students and their tariffs are: ")
    print(students)
    for st, tar in students.items():
        print(f"Student: {st} Tariff: {tar}")


visitors(Петя="База", Ваня="Стандарт", Андрей="Про")
