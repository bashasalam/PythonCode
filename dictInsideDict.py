
print("Assalaamu alaikkum")

tools = {"Spanner":5, "Screwdriver": 4,}
toolKit = {'microscrew' :10 , 'Bolts': 250, 'machinedriller':2}

print(tools["Screwdriver"])

print(toolKit['microscrew'])

contacts = {    ###   list inside a Dictionary
    'joe': [9788624518, 'joeser@gmail.com'],
    'jhon':[8745136628, 'jhoneter@gmail.com'],
    'sameer':[784563212, 'sameersrsfa@gmail.com'],
    'simon': [7151385632, 'simonsfder@gmail.com']
}

print(contacts['jhon'])  ### more than just a phone number

#### Remember String.split is the fucntion call which will make the string
## into list. Then we can iterate the list

#dict.items()
#dict.keys()
#dict.values()

print(tools.items())  # caseting into list

print((toolKit.keys()))
print(toolKit.values())

contacts.pop('simon')
print(contacts)

contacts.popitem()
print(contacts)

print(contacts.get('jhon'))
print(contacts.copy())

toolKit['screws'] = 50   ### Addding to dictionaries
print(toolKit)
toolKit.clear()   ### Clearing the dictionaries
print(toolKit)

## dictionaries are unorded. but there is an module which keep the dictionary as
# ordered one.  However in python 3.7 generally dictionaries are ordered only
from collections import  OrderedDict

###NO NEED TO IMPORT ORDEREDDICT

### afe









