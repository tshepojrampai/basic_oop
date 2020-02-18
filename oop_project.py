
class Person:
    
    def __init__(self,first,age,sex,interest):
        self.first =first
        self.sex= sex
        self.age = age
        self.interest = ''.join(interest)
    
    def hello(self):
        return 'Hello, my name is {} and I am {} years old. My interests are {}'.format(self.first,self.age,self.interest)

person = Person('Ryan',30,'male',['being a hardarse', ' agile', ' ssd hard drives'] )
greeting = person.hello()
print(greeting)
