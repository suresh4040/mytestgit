#inheriting the objects of parent to child class
#3 types -  single , mutilevel, multiple

# --------------------------------SIMGLE------------------------------------
class father():
	# p = 1
	def __init__(self,aname,aage):
	 	self.name = aname
	 	self.age = aage
	def ll(self):
	 	return f"name {self.name}"	

class son(father):  # son got all of father
	def __init__(self,aname,aage,lang):   # if we dont give constructor then it will find in parent class constructor
	 	self.name = aname
	 	self.age = aage
	 	self.lang = lang
	def pp(self):
		return f"your name is {self.name},{self.age},{self.lang}"

suresh = father("suresh",22)
skm = son("skm",33,["hh","mm"])
print(skm.pp())
print(skm.ll())

#----------------------------------MULTIPLE----------------------------------------------

class mother():
	p=2

class daughter(father,mother):  # daughter will check constructor 1st in father then in mother
	x = 30

	# def __init__(self,name,game):
	# 	self.name = name
	# 	self.game = game
	def pdetail(self):
			return f"your name is {self.name},{self.age}"
	
suresh = father("suresh",22)

sarmi = daughter("sarmi",30) # so this class is usong constructor of father class.
print(sarmi.name)
print(sarmi.age)
print(sarmi.p)


#-----------------------------------MULTI-LEVEL-----------------------------------------


class dad():
	baskball = 1

class son(dad):
	dance = 1
	baskball = 3
	def isdance(self):
		return f"yea i dance cool {self.dance} number of times"	

class grandson(son):
	
	dance = 6
	def isdance(self):
		return f"yea i dance awesome {self.dance} number of times"	

dadi = dad()
lar = son()
gson = grandson()

print(gson.isdance())
print(gson.baskball)  # 3

