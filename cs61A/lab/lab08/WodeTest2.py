class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Person('{self.name}')"

    def __str__(self):
        return f"Hello, I am {self.name}"
p=Person("kensho")
print(p)
class Student:
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def __str__(self):
        return '名字:{0}, 成绩:{1}'.format(self.name,self.score)
    
students = [Student("Tom", 80), Student("Jerry", 95)]

print(max(students, key=lambda s: s.score))
arr1=[1,2,3,4,5]
arr1.extend([1])
arr1.append([1])
print(arr1)