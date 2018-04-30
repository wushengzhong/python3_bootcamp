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
popped_item=newlist.pop()

# pop via index
popped_item=newlist.pop(0)
newlist.pop(-1)

# sort & reverse methods
newlist.sort()

# none type return
my_sorted_list=newlist.sort()

newlist.sort()
my_sorted_list=newlist

newlist.reverse()


################################################################################################################################################
#																																			   #
#																																			   #
#																Python Dictionary															   #
#																																			   #
#																																			   #
################################################################################################################################################

dict={'key1':'value1','key2':'value2'}

newdic={'apple':2.4,'banana':2}

d={'key1':['a','b','c']}
d['key1'][2].upper()

# dictionary is mutable

d['key2']=[1,2,3]

d.keys()
d.values()
d.items()

################################################################################################################################################
#																																			   #
#																																			   #
#																Python Tuple															   #
#																																			   #
#																																			   #
################################################################################################################################################



t=(1,2,3)
type(t)

mylist=[1,2,3]
type(mylist)

len(t)
t=('one',2)
t[0]
t[-1]

t= ('a','a','b')
t.count()
t.index()

#immutatbility

mylist[0]='new'

# tuple is different from list
t[0]='new'
# returns error

myset=set()
myset.add(1)
myset.add(1)
myset.add(2)

set(mylist)

set('Mississipi')
#returns{ 'M','i','p','s'}


set({'key':'value','key1':'value'})
#returns {'key','key2'}

True

False

1>2

2>1

1==1
1==1.0


# %%writefile myfile.txt
# Hello this is a text file
# this is the second line
# this is the third line
myfile=open('myfile.txt')

myfile.read()

# run again, runs into ' '
myfile.read()
#returns ''

#reset cursor
myfile.seek(0)
myfile.read()


myfile.readline()
myfile.readlines()

with open("/Users/Wenyi/Documents/fredwu/jupyter notebook/myfile.txt") as my_file:
    contents=my_file.readlines()

# %%writefile myfile.txt
# one on first
# two on second
# three on third 

with open('myfile.txt',mode='r') as f:
    print(f.read())

with open('myfile.txt',mode='a') as f:
    f.write('\nfour on fourth')    

# one on first
# two on second
# three on third 
# four on fourth


