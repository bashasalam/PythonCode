print("Assalaamu alaiikum")

print("'")

print('"')

import re

text = "random string jsdfl Myname123@website.com somewhere randim text jjgjsgfj" \
       " Yourname4646@website.com ljsgl;js  " \
       "salambashaeee@gmail.com alfasjf;k;af"


pattern = re.compile("[a-zA-Z0-9]+[@]+[a-zA-Z0-9]+\.+[a-zA-Z]+")

### Seriously I've to say Alhamdhulillaahi rabbil aalameen as this code i found by using some
## useless voice with useless screenvideo.

result = pattern.search(text)

result2 = pattern.findall(text)

print(result)
print()
print(result2)