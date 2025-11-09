print('Encyclopedia'.count('c')) # count function

# to find the count of all the vowels in the string
vowels='AEIOUaeiou'
vowelsCount=0
for ch in vowels:
    vowelsCount=vowelsCount+'Encyclopedia'.count(ch)
print(vowelsCount)    

colors='green, red, blue, red, red, green'
print(colors.find('red')) # find function -> argument me jo string pass
 #krte h woh first time main string me kahan se start ho rha hota h uska index return krta h

print(colors.find('orange')) # returns -1 if the argumented string is not in the main string

print(colors.rfind('red')) # rfind function-> find starting index of the last occurence of a
 # string in another string

# capitalize function -> converts the first letter of a string to uppercase character and
 # converts the remainig letter to lowercase(if not already so)
print('python IS a Language'.capitalize()) 

# title function -> capitalize the first letter of each word in a string and converts the remaining
 # letters to lowercase(if not already so)
print('python IS a PROGRAMMING Language'.title())  

# upper function -> converts all letters in a string to uppercase
print('python IS A programming Language'.upper())

# lower function
print('PYTHON IS A Programming Language'.lower())

emailId1='satyamraj5926@gmail.com'
emailId2='Satyamraj5926@gmail.com'
print(emailId1==emailId2)
print(emailId1.lower()==emailId2.lower())
print(emailId1.upper()==emailId2.upper())

# swapcase function -> converts lowercase letters to uppercase letters in a string and vice-versa
print('pYTHON iS A PROGRAMMING lANGUAGE'.swapcase())

# isupper function -> checks if all letters in a string are in uppercase
print('Python'.isupper())

# islower function ->checks if all letters in a string are in lowercase
print('python'.islower())
print()

# istitle function -> returns true if a string S(comprising atleast one alphabet) is in title case
print('Basic Python Programming'.istitle())
print('Basic PYTHON Programming'.istitle())
print('123'.istitle())
print('Book 123'.istitle()) 
print()

message='satyam my friend,satyam my guide'
print(message)
print(message.replace('satyam','Arya'))
print(message)

# lstrip,rstrip and strip function

# lstrip function -> removes whitespace or given characters from the left(beginning) side
s='  hello world  '
print(s.lstrip()) # right sides ke spaces abhi bhi hai
s='##python##'
print(s.lstrip('#'))
# rstrip function -> removes whitespace or given characters from the right side
s='  hello world  '
print(s.rstrip()) # left sides ke spaces ab bhi hai
s='@@python@@'
print(s.rstrip('@'))
# strip function -> removes whitespace or given characters from both end(start and end)
s='  hello world  '
print(s.strip()) # beech ke spaces nhi htaata hai
s='&&python&&'
print(s.strip('&'))

# split function -> split a string into a list of strings based on delimiter(seperator) passed,
 # if no seperator is passed,python uses whitespaces as the default delimiter(seperator)

s=' I love Python programming'
print(s.split()) # default case-> spaces se split
s='apple,bannana,grapes'
print(s.split(',')) # seperator=,

# join function -> joins elements of an iterable(like a list
#  ,tuple or set) into a single string using a seperator


words=['i','love','python']
print(words)
print(' '.join(words)) # output- i love python
 #                      # ''(space) is used as a seperator
print('-'.join(['A','B','C'])) #output- A-B-C
#                       # '-' is used as a seperator
print('>'.join(['I','am','ok']))

# isalpha function -> checks if all characters in a string are alphabet
 # letters(A-Z,a-z)
s1="python"
s2="python5"
name='satyam singh'
print(s1.isalpha())
print(s2.isalpha()) #False (beacuse of '5')
print(name.isalpha()) #False (because whitespace is not considered as alphabets)
print()

# isdigit function -> checks if all characters in a string are digits(0-9)
s1='12345'
print(s1.isdigit())
s2='123a'
print(s2.isdigit()) 

# isspace function -> checks if all characters in a string are whitespace
 # characters(space,tab \t,newline \n)
s1="   "
print(s1.isspace())
s2="python"
print(s2.isspace())
s3=" \n \t "
print(s3.isspace())
print()

# isalnum function -> checks if all characters in a string are alphanumeric(letters or digits)
s1="python3"
print(s1.isalnum())
s2='12345'
print(s2.isalnum())
# startswith function -> checks whether a string starts with a particular string
name='Satyam Kumar Singh'
print(name.startswith('Satyam'))
print(name.startswith('kumar'))

print(name.endswith('Singh')) # endswith function