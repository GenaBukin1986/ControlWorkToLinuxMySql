class Commands():
    def __init__(self):
        self._command_list = {
            1:'Ко мне',2:'Лежать',3:'Апорт',
            4:'Бежать',5:'Прыгать',6:'Кувырок',
            7:'Охранять',8:'Рядом',9:'Нести',
            10: 'Бежать на двух лапах',11:'Играть',12:'Галоп',
            13:'Крутиться',14:'Голос',15:'Петь'}
        
    def get_List_command(self):
        print()
        for i,j in self._command_list.items():
            print(f"\t{i} {j}")
            
    def add_command(self,command):
        ch = len(self._command_list)
        self._command_list[ch] = command
        print(f"\tКоманда {command} успешно добавна в список комнад")
        
    def get_Id_command(self):
        return self._command_list.keys()
    
    def get_Command(self,id):
        return self._command_list[id]
        
        
