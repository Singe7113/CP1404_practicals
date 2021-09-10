def determine_grade(percentage):
    if percentage >= 85:
        result = "HD"
    elif percentage >= 75:
        result =  "D"
    else:
        result = "N"
    
    return result

print(determine_grade(100))