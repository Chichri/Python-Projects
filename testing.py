def get_fullname(first, last):
    fullname = first + ' ' + last
    return fullname.title()

print("Enter 'q' to stop")

while True:
    first = input("What's your first name\n")
    if first == 'q':
        break
    last = input("What's your last name\n")
    if last == 'q':
        break
    fullname = get_fullname(first, last)
    print('Your full name is ' + fullname)
#Testing is an important part of writing good code. Lets practice it!
#the code above does nothing new. Lets try to modify it to allow middle names

print('\n')

import unittest

class NamesTestCase1(unittest.TestCase):
    def test_first_last_name(self):
        testname = get_fullname('janis', 'joplin')
        self.assertEqual(testname, 'Janis Joplin')


#This is a basic unit test that uses the module unittest
#For this, we need a class to contain that unit test, and others that may follow
#You'll notice that our class here inherites from unittest.TestCase. This is -
#- mandatory, a class imported from unittest
#You'll also notice that the first method defined in our NamesTestCase starts -
#- with 'test' at the beginning. This is also necessary, it tells Python to -
#- to run the method automatically without being called.
#Within first_last_name, one of unittests most useful features; an assert method
#Assert method verify whether a result you get was what you expected
#This one takes the result you get and the expected result as arguements

class NamesTestCase2(unittest.TestCase):
    def test_fail_first_last_name(self):
        testname = get_fullname('david', 'lee', 'roth')
        self.assertEqual(testname, 'David Lee Roth')
#This is an example of a failing test
#Since we haven't modified get_fullname() to allow middle names, this test fails
#This produces a detailed report on the error in the traceback, as well as an E
#When a test fails, when debugging, don't change the test, change the function
#Changing the test will only ignore error, changing the function will fix it

def get_fullname(first, last, middle = ''):
    if middle:
        fullname = first + ' ' + middle + ' ' + last
    else:
        fullname = first + ' ' + last
    return fullname.title()

class NamesTestCase3(unittest.TestCase):
    def test_success_first_last_name(self):
        testname = get_fullname('david', 'roth', 'lee')
        self.assertEqual(testname, 'David Lee Roth')
#Now this test passes!

#Here's a list of the assert methods you get in unittest

#   Method                     Use
#   -------------------------------------------------------------
#   assertEqual(a, b)          Verify that a == b
#   assertNotEqual(a, b)       Verify that a != b
#   assertTrue(x)              Verify that x is True
#   assertFalse(x)             Verify that x is False
#   assertIn(item, list)       Verify that item is in list
#   assertNotIn(item, list)    Verify that item is not in list

class AnoymousSurvey():
    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(question)

    def store_responses(self, new_responses):
        self.responses.append(new_responses)

    def show_results(self):
        print('The results are: ')
        for response in self.responses:
            print('-' + response)

question = 'What was your first language'
language_survey = AnoymousSurvey(question)
language_survey.show_question()

while True:
    response = input('Enter q to quit')
    if response == 'q':
        break
    language_survey.store_responses(response)

language_survey.show_results()

class TestAnoymousSurvey(unittest.TestCase):
    def test_show_question(self):
        language_survey.responses = ['English', 'French', 'Mandarin']
        self.assertIn('English', language_survey.responses)
#unit tests aren't restricted to functions, methods can also be tested as well
#note that an instance of the class is needed to work with the class here
#What if that process could be streamlined?

class TestAnoymousSurvey(unittest.TestCase):
    def setUp(self):
        question = 'Where do you come from'
        self.place_survey = AnoymousSurvey(question)
        self.responses = ['America', 'France', 'U.K']

    def test_store_single_response(self):
        self.place_survey.store_responses(self.responses[0])
        self.assertIn(self.responses[0], self.place_survey.responses)

    def test_store_three_responses(self):
        for response in self.responses:
            self.place_survey.store_responses(response)
        for response in self.responses:
            self.assertIn(response, self.place_survey.responses)

unittest.main()
#unittest.TestCase contains the method setUp(), which is special within Python
#setUp() will run before anything method starting with test
#Therefore, objects created in setUp() are available to all other test methods
#And finally, unittest.main() runs each test in the file
