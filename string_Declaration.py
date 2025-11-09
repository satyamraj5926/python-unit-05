message='Hello Satyam'
print(len(message)) #len function

print(message[0]) # indexing
print(message[6])
index=len(message)-1
print(index)

print(message[-1]) # negative indexing
print(message[-12])
# print(message[-13]) # index out of range,it gives eror

# message[6]=0  # string are immutable,it give error

print('Computer'+' Science') # string concatination using + operator
print('Hi'*5) # string repetition using * operator

print(max('AZ','C','BD','BT')) # max function
print(min('BD','AZ','Z'))      # min function
print(max('hello','how','are','you','sir'))

message2='Hello Sita'
print(message[0:5])    # string slicing
print(message[-10:-5]) # start:end
# Note-> start value is included,and end value is excluded


print(message[:5])
print(message[5:])   
print(message[:5]+message[5:])  
print(message[:15]) # python automatically assign the end value to length of string
#if the end value is out of range
print(message[15:]) # print ''

print(message[0:len(message):2]) # start:end:increment
print(message[0:8:2])

print('h' in 'hello')  # Membership Operator in
print('ell' in 'hello')
print('h' in 'Hello')

# printing 'h e l l o' from 'hello'
helloSpaced=''
for ch in 'hello':
    helloSpaced=helloSpaced+ch+' '
print(helloSpaced)    