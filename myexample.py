def twoSums(lst,target):
	tmp={}
	for k,v in enumerate(lst):
		if target-v in tmp:
			return[tmp[target-v],k+1]
		else:
			tmp[v]=k+1

print(twoSums([2,3,5,9,7,8],11))


sets([1,2,3,4,5,4,3,5])

knights = {'gallahad': 'the pure', 'robin': 'the brave'}

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for k,v in zip(questions,answers):
	print("The %s is %s" %(k,v))

name = raw_input("who are you?")
print "hello %s" % (name,)

