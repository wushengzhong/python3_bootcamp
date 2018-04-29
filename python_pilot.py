# string
# just retun the value
'hello'
'this is also a string'
# only the last result was displayed

# print() method return all value
print('hello')
print('this is also a string')
# screen result hello rather than 'hello'


# escape sequence
print('hello\nwrold')
print("I'm a double-quotted string here")

# tab escape sequence
print("hello\ttab")

# indexing
len('hello')
len("I'm hungry")

mystring="Hello World"
mystring

mystring[0]
mystring[8]

mystring[-2]==mystring[9]

mystring='abcdefghijk'
mystring[0:]

# retrun the value of string
print(mystring[0:2])

print(mystring[2:8:2])


# string properties
# immutatble
newstring=mystring[1:]

# need to use + sign to concatenate
newstring='s'+newstring

letter='z'
print(letter*10)

'2'+'3'
#'23'

x='Hi This is a string'
x.split('i')

print('This is a string {}'.format('INSERTED'))
print('The{1}{2}{0}'.format('fox','quick','brown'))
print('The {f} {q} {b}'.format(f='fox',q='quick',b='brown'))



result=100/777
print('The reuslt is {r:2.3 f}'.format(r=result))

name=raw_input("What's you name")
print('His name is {}'.format(name))
print(f'His name is {name}')

print('His name is {n}, his age is {age}, his height is {h}. David is {age} as well'.format(n='Fred',age='32',h='5 feet 8 inches'))
print('His name is %s and his age is %s' %('Michael','65\n\thappy'))



################################################################################################################################################
#																																			   #
#																																			   #
#																Python List																	   #
#																																			   #
#																																			   #
################################################################################################################################################


mylist=['one','two','three']
mylist[:1]

another_list=["four","five"]

# list concatenation
mylist+another_list
newlist=mylist+another_list
newlist[0]="one new item"

# list appendment

newlist.append('six')
newlist.remove('six')
newlist.pop()
