# Stage 1 objectives:
# 1. Allow users to input their study subjects and the time in minutes for each subject
# 2. Ask user if theyd like to add another subject. If not, stop reading input, else continue reading.
# 3. Save the input in a dictionary where the keys are subject names and the values are the time allocated
# 4. Handle input type validation for allocated time. If not an integer prompt for a new input with reason
#    as to why


def main():

    # Dict that will hold info about all the subjects of our study plan
    subjects = {}

    # Loop that will continuously prompt for a new subject until the flag is set to False, breaking the
    # loop.
    flag = True
    while flag:
        # Input prompts for a subject and time allotted for studying said subject.
        subject = input("Enter a subject name: ")
        allotted_time_for_subject = input("Enter alotted time for subject: ")

        # Loop that continuously runs until a valid input type of integer is given for allotted
        # time
        integer_input_given = False
        while not integer_input_given:
            # Checks to see if allotted time input was a digit, and breaks the loop if it is.
            if allotted_time_for_subject.isdigit():
                integer_input_given = True
            # Informs user of invalid input, and prompts for new input.
            else:
                print("Input not valid. Please enter an integer...")
                allotted_time_for_subject = input("Enter a allotted time for subject: ")

        # Save subject in subjects dictionary
        subjects[subject] = int(allotted_time_for_subject)

        # Ask user if theyd like to enter another subject or not, if no, break loop
        add_another_subject = input("Add another subject? (yes/no): ")
        if add_another_subject.lower() == "no":
            flag = False

if __name__ == "__main__":
    main()