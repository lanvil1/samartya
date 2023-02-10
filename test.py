class Person:
 def __init__(self,name,age):
   self.name=name
   self.age=age
 
 def func(self):
   print("Hello my name is "+self.name)

 def __str__(self):
   return "Name:"+self.name+",Age:"+str(self.age)
      

p1= Person("John",36)
p1.func()
print(p1)