#space between first name and last name
First = "Faridah"
Last = "Dada"
print(First + " " + Last)

#list constructor vs just typing a list
#name = [First, Last]
#name = list ((First ,Last))
name = ["Faridah", "Dada"]
print(name)

#converting list to dictonary
dict = ["First", " Last" ]

#namedict = dict(zip(name,dict))
#namedict = dict.fromkeys(name, dict)
#print(namedict)

#converting list to dictonary
keys = {'a', 'e', 'i'}
vowels = dict.fromkeys(keys)
print(vowels)
