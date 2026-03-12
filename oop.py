# class human:
#     def __init__(self,name,age):
#         self.name=name
#         self.age =age
    
#     def display(self):
#         print(f"name={self.name},age={self.age}")
        
# kishan = human("kishan",20)
# kishan.display()


class car:
    def __init__(self,boy,girl):
        print("car object created")
        self.boy=boy
        self.girl=girl
h1 = car("kishan","ff")

class person:
    def __init__(self,name):
        self.name=name
        
    def greet(self):
        print(f"my name is {self.name}")
        
        
k = person("name")
k.greet()

class employee:
    def __init__(self,name,designation,salary=30000):
        self.name=name
        self.designation=designation
        self.salary=salary
        
    def gr(self):
        print(f"name={self.name} and designation = {self.designation} and salary = {self.salary}")

p =employee("kishna","software engineer",450000)


l=[1,2,3]
l.append(4)
print(type(l))
print(l)


class database:
    def __init__(self):
       
        self.__storage={}
    
    def write(self,key,value):
        self.__storage[key]=value
        
    def read(self,key):
        if key in self.__storage:
            print (self.__storage[key])
        else:
            print("db not available")
                
db = database()
db.write("subscribers","100k")
db.read("subscribers")   
db.write("name","EIK")
db.read("name")

    
    
    