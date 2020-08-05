

#####Mutable = Changable
#### Immutable == Uncahangable


#### LIST ARE MUTABLE
list1 = [12,5,7,68,1,5,3,2,'fkajh','afa']

# Ordered list
# dictionaries
#


#### TUPLE ARE IMMUTABLE
### INTS ARE IMMUTABLE
# FLOATS
# BOOLEANS


t1 = (1,2,3, [1,2,3], (45,34,23))

#t1[0] = 2   ## this is an error

t1[3][0] = 0  ### A LIst inside a tuple is still mutable

print(t1)   ### here the location of the list can't change.

t1[3].append(5)  ### It is denoting the list which is  inside the t1 tuple
print(t1)   ## Still i can do all the list operations on a list inside tuple

#  t1[4][0] = 65   This is an error bcz it is tuple inside a tuple

# True = False  Booleans are immutable

## 5 = 6  Integer
