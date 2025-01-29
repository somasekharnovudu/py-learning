# complex data structures
# create persons list
persons = [{'name': 'max', 'age': 30, 'hobbies': ['reading', 'cycling']},
           {'name': 'micheal', 'age': 19, 'hobbies': ['writing', 'walking']},
           {'name': 'john', 'age': 30, 'hobbies': ['talking', 'running']}]


# print names arr
print([person['name'] for person in persons])

# checks age>20 for all
print(all([person['age'] > 20 for person in persons]))

# create deep clone of things
copied_persons = []

for person in persons:
    copied_persons.append(person.copy())
copied_persons[0]['name'] = 'new name'

print(copied_persons)
print(persons)

# unpacking
[person1, person2, person3] = persons

print('== person1', person1)
print('== person2', person2)
print('== person3', person3)
