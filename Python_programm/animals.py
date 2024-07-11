class Animals:
    cht = 0
    """Абстрактный класс Животных"""
    def __init__(self,name,birthday):
        self._name = name
        self._birthday = birthday        
        Animals.cht += 1
        self._id = Animals.cht
        self._command_animals = []
        
    def get_All_command(self):
        return len(self._command_animals)    
    
    def get_Name(self):
        return self._name
    
    def get_Birthday(self):
        return self._birthday    
    
    def get_id(self):
        return self._id
    
    def commamd(self,command):
        if (command in self._command_animals):
            print(f"\t{self._name} уже обучен '{command}'")
            print(f"\t{self._name} начинает злиться!!!")
        else:    
            self._command_animals.append(command)
            print(f"\t{self._name} успешно обучен команде '{command}'")
        
    def get_Command(self):
        for i in range(len(self._command_animals)):
            print(f"\t{i+1}. {self._command_animals[i]}")
    
    def __str__(self) -> str:
        return f"{self._name} {self._birthday}"
    

    

    

    


    



# an = Animals("Bob",'2021-02-11',"Cat")
# print(an)

# an.get_Command()