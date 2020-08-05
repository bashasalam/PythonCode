

print("Assalaamu alaikkum")

print('""')

print(" ' ")

##### Email text scrapper #### PATTERN CHECKER

import re

text = "A1rand omstring1971"

#pattern = re.compile("(A)")  ## I dont know why it is not matching with ABC

### YES IT IS NOT () IT IS [] . THAT IS  THE MISTAKE I DID

pattern = re.compile("[a-zA-Z0-9]+")  ##lOOKING FOR SINGLE A B OR C UPPERCASE

## it terminates when the first match fournd
result = pattern.search(text) ### [a-z] means for a to z
# hence r is the first match it creats the object r
print(result)

### If you give space in between []  then it will take the space also a charector.

## in this case if we give space then it will generate the object random string
## but if we give without space then it will create the object random
