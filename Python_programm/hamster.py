from animals import Animals

class Hamster(Animals):
    h_cht = 0
    def __init__(self,name,birthday):
        super().__init__(name,birthday)
        self.__Group = "Домашнее животное"
        self._class_animals = "Хомяк"
        Hamster.h_cht += 1
        self._id_hamster = Hamster.h_cht
        
    def get_Id_hamster(self):
        return self._id_hamster
    
    def get_Class_animals(self):
        return self._class_animals    
        
    def get__Group(self):
        return self.__Group
        
    def __str__(self):
        return f"{self._name} {self._birthday} {self._class_animals} {self.__Group}"