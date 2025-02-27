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
        allotted_time_for_subject = input("Enter an alotted time for subject in minutes: ")

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
                allotted_time_for_subject = input("Enter an allotted time for subject in minutes: ")

        # Save subject in subjects dictionary
        subjects[subject] = int(allotted_time_for_subject)

        # Print current state of subjects dictionary
        print(subjects)

        # Loop that ensures user is prompted again if incorrect input is given for question below
        gave_yes_or_no = False
        while not gave_yes_or_no:
            # Ask user if theyd like to enter another subject or not.
            add_another_subject = input("Add another subject? (yes/no): ")

            # Checks if input was valid or not.
            if add_another_subject.lower() == "no" or add_another_subject.lower() == "yes":
                # If users answer was no, break main loop
                if add_another_subject.lower() == "no":
                    flag = False
                # Otherwise, break this loop so user can be prompted for another subject
                gave_yes_or_no = True
            else:
                # Inform user of invalid input and prompt for proper input
                print("Input not valid. Please enter yes or no...")
                add_another_subject = input("Add another subject? (yes/no): ")

if __name__ == "__main__":
    main()