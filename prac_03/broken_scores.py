import random

def main():
    number_of_scores = int(input("what number of scores do you want? : "))
    for x in range(number_of_scores):
        score = random.randrange(1,100)
        grade = get_grade(score)
        print("{} is {}".format(score,grade),file=file)

def get_grade(score):
    if score < 0:
        print("Invalid score")
    else:
        if score >= 100:
            grade = "Invalid score"
        elif score >= 90:
            grade = "Excellent"
        elif score >= 50:
            grade = "Passable"
        elif score < 50:
            grade = "Bad"
    return grade

file = open("results.txt","a")
main()
file.close()