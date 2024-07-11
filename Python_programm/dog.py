from animals import Animals

class Dog(Animals):
    d_cht = 0
    def __init__(self,name,birthday):
        super().__init__(name,birthday)
        self._class_animals = "Собака"
        self.__Group = "Домашнее животное"
        Dog.d_cht += 1
        self._id_dog = Dog.d_cht
        
    def get_Id_dog(self):
        return self._id_dog
    def get_Class_animals(self):
        return self._class_animals
        
    def get__Group(self):
        return self.__Group
        
    def __str__(self):
        return f"{self._name} {self._birthday} {self._class_animals} {self.__Group}"
    
