class Student:
    print("HI")
    
    cout_of_student = 0
    
    def __init__(self, height = 160,name = ""):
        self.height = height
        self.name = name
        Student.cout_of_student += 1
        print("Hi! I`m Student")
    
    def grow_up(self,grow):
        if self.height += grow < 220
            self.height += grow
            
    def info(self):
        print(f"Name    :{self.name}")
        print(f"Height  :{self.height}")
        
    def __str__(self):
        return f"Name    :{self.name}\nHeight :{self.height"}
        
    def __del__(self):
        print(f"{self.name} is dead")
        
    def __len__(self):
        return self.height


    
student1 = Student(name="Artem")
#print(student1.name)
student1.grow_up(50)
#print(student1.height)
student1.info()

print(Student.cout_of_student)

student2 = Student(height = 170,name="andriy")
#student2.height = 170
#print(student2.name)
#print(student2.height)
student2.info()

print(Student.cout_of_student)
