from programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

programing_list = [ruby,python,visual_basic]

for program in programing_list:
    if program.is_dynamic():
        print(program.name)
