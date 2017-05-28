#Setup
from pyvt import Timetable
timetable = Timetable()

#Tests
git_sec = timetable.crn_lookup('17583', term_year='201701', open_only=False)
# print('GitHub test code: ' + str(git_sec) + '\n')

test1_sec = timetable.class_lookup(subject_code='CS', class_number='2506', term_year='201709')
# print('test1_sec CS 2506 False: ' + str(test1_sec) + '\n')

test2_sec = timetable.subject_lookup(subject_code='CS', term_year='201709')
# print('test2_sec CS False: ' + str(test2_sec) + '\n')

test3_sec = timetable.cle_lookup(cle_code='AR01', term_year='201709')
# print('test3_sec AR01 False: '+ str(test3_sec) + '\n')

test4_sec = timetable.class_lookup(subject_code='CS', class_number='2114', term_year='201709')
# print('test4_sec CS 2114 False: ' + str(test4_sec) + '\n')

test5_sec = timetable.crn_lookup(crn_code='82538', term_year='201709', open_only=False)
# print('test5_sec 82538 (A 2114 class) 2017 Fall False: ' + str(test5_sec) + '\n')

test6_sec = timetable.class_lookup(subject_code='MATH', class_number='2114', term_year='201709', open_only=False)
print('test6_sec MATH 2114 False: '  + str(test6_sec) + '\n')

test7_sec = timetable.subject_lookup(subject_code='MATH', term_year='201709', open_only=True)
print('test7_sec MATH True: ' + str(test7_sec) + '\n')
