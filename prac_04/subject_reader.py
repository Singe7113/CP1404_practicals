"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "prac_04/subject_data.txt"


def main():
    data = get_data()
    for subject_list in data:
        print("{} is taught by {} and {} students attend".format(subject_list[0],subject_list[1],subject_list[2]))


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = []
    for line in input_file:
        #print(line)  # See what a line looks like
        #print(repr(line))  # See what a line really looks like

        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts

        #print(parts)  # See what the parts look like (notice the integer is a string)

        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)

        #print(parts)  # See if that worked

        #print("----------")
        data.append(parts)
    input_file.close()
    return data


main()