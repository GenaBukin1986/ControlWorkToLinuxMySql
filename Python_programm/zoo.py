class Zoo():
    cht = 0        
    def __init__(self):
        self.box = {}
        self.counter = 0
        self.box_animals = {
            1:'Кошка',
            2:'Собака',
            3:"Хомяк",
            4:"Лошадь",
            5:"Осел",
            6:"Верблюд"
        }
        
    def get_Box_animals(self):
        return len(self.get_Box_animals)
    def get_Zoo_id(self):
        return self.box.keys()
    
    def get_animal(self,id):
        return self.box[id]
    
    def get_animal_command(self, id):
        if self.box[id].get_All_command() == 0:
            print(f"\n\tК сожалению, {self.box[id].get_Class_animals()} {self.box[id].get_Name()} ничего не умеет((")
            print(f"\tНо вы можете обучить командам {self.box[id].get_Class_animals()} {self.box[id].get_Name()} в пункте 5 Меню.")
        else:
            print(f"\n\t{self.box[id].get_Class_animals()} {self.box[id].get_Name()} умеет: ")
            self.box[id].get_Command()
        
            
    
    def del_Zoo(self,number):
        del self.box[number]
        print("""
        Животное успешно удалено из Зоопарка!
        Оно нисколько не обижается на Вас!""")
        
    def add(self,animal):        
        Zoo.cht += 1
        self.counter = Zoo.cht
        self.box[self.counter] = animal
        
    def show_animals(self):
        for i,j in self.box.items():
            print(i,j)
            
    def show_pets(self):
        for i,j in self.box.items():
            if j.get__Group() == "Домашнее животное":
                print(i,j)
                
    def show_pack_animals(self):
        for i,j in self.box.items():
            if j.get__Group() == "Вьючное животное":
                print(i,j)

    def get_Counter(self):
        return self.counter
    
    def show_pet(self):
        print("""
            Список живоных, которых можно завести в нашем Зоопарке:
            """)
        for i,j in self.box_animals.items():
            print('\t',i,j)
            
    def show_pets_id(self):
        return self.box_animals.keys()