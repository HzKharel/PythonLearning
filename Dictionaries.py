import RockPaperScissors as RPS
#Dictionary (hash map) in python
# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is

# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

student = {'name' : 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
student.update({'name': 'Mike','age': '23'})
#del student['age']
#age = student.pop('age')
print(student.items())

for key in student:
    print(student.get(key))

if __name__ == '__main__':
    game = RPS
