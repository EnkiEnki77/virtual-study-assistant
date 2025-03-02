# Write your code here >>>

# Stage 1 objectives:
# 1. Allow users to input their study subjects and the time in minutes for each subject
# 2. Ask user if theyd like to add another subject. If not, stop reading input, else continue reading.
# 3. Save the input in a dictionary where the keys are subject names and the values are the time allocated
# 4. Handle input type validation for allocated time. If not an integer prompt for a new input with reason
#    as to why


def main():

    # Dict that will hold info about all the subjects of our study plan
    subjects = {}
    study_plan = """\nYour study plan: \n"""
    total_study_time = 0
    time_spent_studying = 0

    # Loop that will continuously prompt for a new subject until the flag is set to False, breaking the
    # loop.
    flag = True
    while flag:
        # Input prompts for a subject and time allotted for studying said subject.
        subject = input("""Enter subject name: """)

        if subject == "":
            if subjects:
                print(study_plan)
                break
            else:
                break
        integer_input_given = False
        while not integer_input_given:
            allotted_time_for_subject = input(f"Enter time allocated for {subject}: ")

            if allotted_time_for_subject.isdigit():
                # Save subject in subjects dictionary
                subjects[subject] = int(allotted_time_for_subject)
                integer_input_given = True


        total_study_time = 0
        study_time_including_breaks = 0
        study_plan = """\nYour study plan: \n"""

        # Loop through subjects dictionary full of users subject data
        for i, subject in enumerate(subjects):

            # Check if last subject in dict. If so, add last subject's info to study_plan as well
            # as total study time and study time with breaks.
            if i == len(subjects) - 1:
                total_study_time += int(subjects[subject])
                study_time_including_breaks = total_study_time + (total_study_time // 45) * 15
                study_plan += f"{subject}: {subjects[subject]} minutes\n"
                study_plan += f"Total study time: {total_study_time} minutes\n"
                study_plan += f"Total time including breaks: {study_time_including_breaks} minutes\n"

            else:
                total_study_time += int(subjects[subject])
                study_plan += f"{subject}: {subjects[subject]} minutes\n"

        print(study_plan)

    if total_study_time > 1:
        time_spent_studying = int(input("Enter time spent studying: "))
        print(f"You have completed {((time_spent_studying / total_study_time) * 100) if time_spent_studying <= total_study_time else 100.00:.2f}% of your planned study time.\n")

if __name__ == "__main__":
    main()