'''
Student Name: Hannouda Amal
Final Project: Result Evaluation Report
'''
# Import the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import os
import emoji

def grade_generator(scores): # Generator to get grades from a list of scores
    for score in scores: # yields corresponding grades based on score ranges.
        if score >= 94:
            yield 'A+'
        elif score >= 87:
            yield 'A'
        elif score >= 80:
            yield 'A-'
        elif score >= 77:
            yield 'B+'
        elif score >= 74:
            yield 'B'
        elif score >= 70:
            yield 'B-'
        elif score >= 67:
            yield 'C+'
        elif score >= 64:
            yield 'C'
        elif score >= 60:
            yield 'C-'
        else:
            yield 'F'

def final_score(scores): # calculates the average score from the provided scores
    final_score = sum(scores) / len(scores)
    return final_score

def final_grade(scores): # determines the overall grade based on the average score
    final_score = sum(scores) / len(scores)
    F_grade = None
    if final_score >= 94:
        F_grade = 'A+'
    elif final_score >= 87:
        F_grade = 'A'
    elif final_score >= 80:
        F_grade = 'A-'
    elif final_score >= 77:
        F_grade = 'B+'
    elif final_score >= 74:
        F_grade = 'B'
    elif final_score >= 70:
        F_grade = 'B-'
    elif final_score >= 67:
        F_grade = 'C+'
    elif final_score >= 64:
        F_grade = 'C'
    elif final_score >= 60:
        F_grade = 'C-'
    else:
        F_grade = 'F'
    return F_grade

def save_in_txt_file(scores,course): # saves the test scores and corresponding grades in a text file.
    grades = list(grade_generator(scores))
    df = {'Score': scores, 'Grade': grades}
    table = pd.DataFrame(df)
    MODE = 'w'
    filename = '{}_tests.txt'.format(course)
    filepath = os.path.join(os.getcwd(),filename)  # getcwd(): function to save the file in the same directory
    file_exist = os.path.exists(filepath)
    case_exist = (''' Test scores and corresponding grades have not be saved in a file named {},
    as a file with the same name already exists in this directory.
    ''').format(filename)
    case_not_exist = ("The test scores and corresponding grades have been saved in a txt file named '{}'").format(filename)
    if file_exist:
        print(case_exist)
    else:
        with open(filepath, MODE) as file:
            file.write(table.to_string(index=True)) # to include the index as column in the file text
            print(case_not_exist)

class StudentPerformance:
    def __init__(self, scores):
        self.scores = scores
    def tests_per_grade(self):
        A_tests = 0
        B_tests = 0
        C_tests = 0
        F_tests = 0
        for score in self.scores:
            if score >= 80:
                A_tests = A_tests + 1
            elif score >= 70:
                B_tests = B_tests + 1
            elif score >= 60:
                C_tests = C_tests + 1
            else:
                F_tests += 1
        return {'A_tests': A_tests, 'B_tests': B_tests, 'C_tests': C_tests, 'F_tests': F_tests}
    def plot_scores(self):
        total_test = self.tests_per_grade()
        grades_hist = ['A', 'B', 'C', 'F']
        frequencies = [total_test['A_tests'] / len(self.scores), total_test['B_tests'] / len(self.scores),
                       total_test['C_tests'] / len(self.scores), total_test['F_tests'] / len(self.scores)] # List of percentages of the number of tests for each degree
        colors = ['blue', 'green', 'orange', 'red']
        plt.bar(grades_hist, frequencies, color=colors) # plots a bar plot, we pass grades_hist to x axis, frequencies to y axis, and we define color for each grade bar by passing the colors list to color attribute
        plt.title('Tests per grades') # adds title to the plot
        plt.xlabel('Grades') # adds label to x axis
        plt.ylabel('Frequency') # adds label to y axis
        plt.grid(axis='y', linestyle='dashed')
        plt.show(block=False) # by passing False to attribute block, we allow the program to continue running without waiting for the user to close the bar plot
    def plot_analysis(self):
        total_test = self.tests_per_grade()
        print('You achieved "A" grade in {:.2f}% of tests.'.format(total_test['A_tests'] * 100 / len(self.scores)))
        print('You achieved "B" grade in {:.2f}% of tests.'.format(total_test['B_tests'] * 100 / len(self.scores)))
        print('You achieved "C" grade in {:.2f}% of tests.'.format(total_test['C_tests'] * 100 / len(self.scores)))
        print('you failed in {:.2f}% of tests.'.format(total_test['F_tests'] * 100 / len(self.scores)))

def print_comment(scores):
    grade = final_grade(scores)
    a = '\U0001F929''\U0001F4AF''\U0001F44F'
    b = '\U0001F929''\U0001F44F''\U0001F929'
    c = '\U0001F44F''\U0001F44C''\U0001F44F'
    f = '\U0001F4AA''\U0001F44F''\U0001F4AA'
    A_comment = ('''
    Congratulations on your "{}" grade! {}
    Your hard work and commitment have paid off. 
    Keep up the fantastic work and let this result inspire you to achieve excellent grades in other courses too. 
    You're doing amazing!''').format(grade,a)
    B_comment = ('''
    Fantastic job on earning a "{}" grade! Your efforts  have truly paid off. {}
    Remember, success comes in many forms, and this is a testament to your abilities to excellence. 
    There's no limit to what you can achieve. Keep embracing the journey of learning and growth.
    Well done!''').format(grade,b)
    C_comment = ('''
    Congratulations on your "{}" grade! {}
    Every step forward is a victory, and your perseverance have brought you to this point.
    Remember, success is not always measured by grades alone. 
    It's about the progress you've made and the knowledge you've gained along the way.
    Stay focused, you have the ability to achieve great and better result. ''').format(grade,c)
    F_comment = ('''
    Though you received an "F" grade, remember that grades do not define your potential. {}
    This setback is an opportunity for growth and learning. Mistakes and challenges are part of the journey towards success.
    Believe in yourself and your abilities, for you are capable of incredible things. 
    Take this as a valuable lesson and let it inspire you to rise above. I believe in you!''').format(f)
    if grade in ['A+', 'A', 'A-']:
        return A_comment
    if grade in ['B+', 'B', 'B-']:
        return B_comment
    if grade in ['C+', 'C', 'C-']:
        return C_comment
    if grade == 'F':
        return F_comment
    
def main():
    # Ask user for course name
    course = input('Please enter the Course Name:\n')
    # Constants
    max_attempts = 3  # maximum number of attempts possible for each score and for total number of tests
    num_of_tests = None
    # Ask the user how many tests have been performed
    for attempt in range(max_attempts):
        try:
            total_number = input('Please enter the Number of Tests:\n')
            temporary_num_of_tests = int(
                total_number)  # used to ensure that num_of_tests only receives a valid input (strictly positive integer)
            if temporary_num_of_tests <= 0:
                raise ValueError
            num_of_tests = temporary_num_of_tests
            break  # beaks out of the code when the value of temp_num_of_tests is assigned to num_of_tests
        except ValueError:
            print('Invalid input! Please enter a strictly positive integer.')
    if num_of_tests is None:
        print('Exceeded maximum attempts. Exiting program.')
        exit()  # used to immediately terminate the program if the maximum number of attempts is reached.
    # Ask user for test scores
    scores = []
    for i in range(1,
                   num_of_tests + 1):  # I use num_of_tests + 1  to ask user num_of_tests  times (the range function doesn't include the stop)
        valid_score = False
        for attempt in range(max_attempts):
            try:
                i_test_score = input('Enter the score of the test {}:\n'.format(i))
                temporary_test_score = float(i_test_score)
                if (temporary_test_score < 0) or (temporary_test_score > 100):
                    raise ValueError
                scores.append(temporary_test_score)
                valid_score = True
                break  # beaks out of the code when True is assigned to valid_score
            except ValueError:
                print('Invalid score! Please enter a number between 0 and 100.')
        if valid_score == False:
            print('Exceeded maximum attempts. Exiting program.')
            exit()  # used to immediately terminate the program if the valid_score variable is still False, indicating that the user has not provided valid input within three attempts for a test
    grades = list(grade_generator(scores))
    # Print line of "-"
    print('-' * 100)
    # Print the report header
    print(('{} Evaluation Report'.format(course.title())).center(100))
    # Print line of "-"
    print('-' * 100)
    print()
    print('Scores and Grades for each test:')
    print()
    # Create a table
    df = {'Score': scores, 'Grade': grades}
    table = pd.DataFrame(df) # create a DataFrame using the dictionary df. This DataFrame is a table with two columns Score and Grade.
    table = table.transpose() # swaps the columns with rows, resulting in a new DataFrame.
    table.columns = ['Test {}'.format(i) for i in range(1, len(scores) + 1)] # column names
    print(table)
    print()
    save_in_txt_file(scores, course)
    print()
    print('Histogram of Test Results:')
    print()
    print('If you run the code in PyCharm, the histogram will be displayed in a new window.')
    student = StudentPerformance(scores) # student is an instance of a StudentPerformance class
    student.plot_scores() # invoke the plot_scores() method on the student instance.
    print()
    print('Overview of Results:')
    print()
    student.plot_analysis() # invoke the plot_analysis() method on the student instance.
    print()
    print('Final Results:')
    print()
    print('Your Final score is {:.2f}.'.format(final_score(scores)))
    print('Your Final grade is {}.'.format(final_grade(scores)))
    print()
    print('Final Result Evaluation:')
    comment = print_comment(scores)
    print(comment)
    while plt.get_fignums(): # function that returns a list of active figure.
        plt.pause(0.1) # function that pauses the execution of the program for a specified duration (0.1 seconds).
    # the while loop will keep iterating and pausing for 0.1 seconds until there are no more active figures.
if __name__ == '__main__': main()
