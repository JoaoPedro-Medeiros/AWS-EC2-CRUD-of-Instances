from .adm_instances.__create_instances import EC2_Instance
from .adm_instances.__update_instances import EC2_Update_Instance
from .adm_instances.__read_instances import EC2_Read_Instance
from .adm_instances.__delete_instances import EC2_Delete_Instance
from tkinter import *

class Menu():
    def __init__(self, menu_options:dict):
        self.__window = Tk()
        self.__window.title('Instances Controller')
        self.__window.geometry("250x100")
        self.__window.resizable(False, False)
        
        label1 = Label(self.__window, text='Selecione:')
        label1.grid(column=0, row=0)

        for key, opt in menu_options.items():
            match opt:
                case '__create':
                    b = Button(self.__window, text=f'{key}', command=self.__create)
                    b.grid(row=1,column=0, )
                case '__update':
                    b = Button(self.__window, text=f'{key}', command=self.__update)
                    b.grid(row=1,column=1)
                    b.size
                case '__read':
                    b = Button(self.__window, text=f'{key}', command=self.__read)
                    b.grid(row=2,column=0)
                case '__delete':
                    b = Button(self.__window, text=f'{key}', command=self.__delete)
                    b.grid(row=2,column=1)
        self.__show_window()

    def __create(self, stop:bool = True):
        new_instance = EC2_Instance()

    def __update(self, id:str):
        new_instance = EC2_Update_Instance(EC2_Instance(id).get_instance_id())

    def __read(self, id:str):
        new_instance = EC2_Read_Instance(EC2_Instance(id).get_instance_id())

    def __delete(self, id:str):
        new_instance = EC2_Delete_Instance(EC2_Instance(id).get_instance_id())
        new_instance.delete()

    def __show_window(self):
        self.__window.mainloop()
