import random

for x in range(0, 10):
    print(random.randint(5, 20))  # smallest number possable is 5 the largest is 19

    print(random.randrange(3, 10, 2))  # smallest number is 3 largest is 9 and even numbers are not possable, therefore '4' isnt possable
    print(random.uniform(2.5, 5.5))  # smallest number is 2.5 largest is 5.49
    print(random.randrange(1,101))
    print()
    