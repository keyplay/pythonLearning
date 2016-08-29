#! python2.7
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

'''
Here is what the program does:

    Creates 35 different quizzes.

    Creates 50 multiple-choice questions for each quiz, in random order.

    Provides the correct answer and three random wrong answers for each question, in random order.

    Writes the quizzes to 35 text files.

    Writes the answer keys to 35 text files.

This means the code will need to do the following:

    Store the states and their capitals in a dictionary.

    Call open(), write(), and close() for the quiz and answer key text files.

    Use random.shuffle() to randomize the order of the questions and multiple-choice options.
'''
