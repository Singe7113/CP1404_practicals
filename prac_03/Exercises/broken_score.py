def main():
    score = float(input("Enter score: "))
    grade = get_grade(score)
    print( grade)

def get_grade(score):
    if score < 0:
        print("Invalid score")
    else:
        if score >= 100:
            grade = "Invalid score"
        elif score >= 90:
            grade ="Excellent"
        elif score >= 50:
            grade ="Passable"
        elif score < 50:
            grade ="Bad"
    return grade

main()

