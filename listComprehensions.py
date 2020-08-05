names = ['nicy ', 'nancy', 'ashrin' , 'haajira', 'fadheela', 'jesica' ]

l = []

for eachperson in names:
    l.append(eachperson)

print(l)

print([personsLovingMe for personsLovingMe in names])
print([personsLovingMe + ' Loves me 'for personsLovingMe in names])


##########DUCTIONARY COMPREHENSION

studentsRatinngs = {'Abdhul':8.9, 'basith':9.2, 'john':9.2, 'shankar':9.0,
                    'saleem':8.5, 'simon':6.7}
#print(studentsRatinngs)
ratingList=[]

for student in studentsRatinngs:
    if studentsRatinngs[student]>=9:
        ratingList.append(student)
print(ratingList)

## List comprehention for dictionaries
print([studentList for studentList in studentsRatinngs if studentsRatinngs[studentList]>=9])




print([studentLi for studentLi in studentsRatinngs if studentsRatinngs[studentLi]>=9])








