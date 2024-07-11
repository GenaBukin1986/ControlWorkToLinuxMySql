from animals import Animals

class Camel(Animals):
    c_cht = 0
    def __init__(self,name,birthday):
        
        super().__init__(name,birthday)
        self.__Group = "Вьючное животное"
        self._class_animals = "Верблюд"
        Camel.c_cht += 1
        self._id_camel = Camel.c_cht
        
    def get_Id_camel(self):
        return self._id_camel
    def get_Class_animals(self):
        return self._class_animals
        
    def get__Group(self):
        return self.__Group
        
    def __str__(self):
        return f"{self._name} {self._birthday} {self._class_animals} {self.__Group}"