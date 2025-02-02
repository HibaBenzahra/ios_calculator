import customtkinter as ctk
import tkinter as tk

class My_Calculator():

    def __init__(self):
        self.window = ctk.CTk()
        
        self.window.geometry("400x550")
        self.window.wm_minsize(330, 450)
        self.window.title('Calculator')
        ctk.set_appearance_mode("dark")  # Set the appearance mode (optional)
        ctk.set_default_color_theme("dark-blue")# Set the default color theme (optional)
        


        self.buttonframe = ctk.CTkFrame(self.window, height=450, width= 400, fg_color='black', corner_radius=5)


        self.buttonframe.grid_columnconfigure(0, weight= 1)
        self.buttonframe.grid_columnconfigure(1, weight= 1)
        self.buttonframe.grid_columnconfigure(2, weight= 1)
        self.buttonframe.grid_columnconfigure(3, weight= 1)
        self.buttonframe.grid_rowconfigure(0, weight=1)
        self.buttonframe.grid_rowconfigure(1, weight=1)
        self.buttonframe.grid_rowconfigure(2, weight=1)
        self.buttonframe.grid_rowconfigure(3, weight=1)
        self.buttonframe.grid_rowconfigure(4, weight=1)
        self.buttonframe.grid_rowconfigure(5, weight=1)

        self.label = ctk.CTkLabel(self.buttonframe, text= "0", font =('ariel', 80))
        self.label.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
       
        self.but_C = ctk.CTkButton(self.buttonframe, text='C', font =('Arial', 30), command= self.update_text_C)
        self.but_C.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.but_negative = ctk.CTkButton(self.buttonframe, text='+/-', font =('Arial', 30), command=self.op_turn_negative)
        self.but_negative.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        self.but_percent = ctk.CTkButton(self.buttonframe, text='%', font =('Arial', 30), command=self.op_percent)
        self.but_percent.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")

        self.but_division = ctk.CTkButton(self.buttonframe, text='÷', font =('Arial', 30), command=self.op_divide)
        self.but_division.grid(row=1, column=3, padx=10, pady=10, sticky="nsew")

        self.but_7= ctk.CTkButton(self.buttonframe, text='7', font =('Arial', 30), command= self.update_text_7)
        self.but_7.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        self.but_8 = ctk.CTkButton(self.buttonframe, text='8', font =('Arial', 30), command= self.update_text_8)
        self.but_8.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

        self.but_9 = ctk.CTkButton(self.buttonframe, text='9', font =('Arial', 30), command= self.update_text_9)
        self.but_9.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")

        self.but_x = ctk.CTkButton(self.buttonframe, text='x', font =('Arial', 30), command=self.op_multiply)
        self.but_x.grid(row=2, column=3, padx=10, pady=10, sticky="nsew")

        self.but_4 = ctk.CTkButton(self.buttonframe, text='4', font =('Arial', 30), command= self.update_text_4)
        self.but_4.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

        self.but_5 = ctk.CTkButton(self.buttonframe, text='5', font =('Arial', 30), command= self.update_text_5)
        self.but_5.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")

        self.but_6 = ctk.CTkButton(self.buttonframe, text='6', font =('Arial', 30), command= self.update_text_6)
        self.but_6.grid(row=3, column=2, padx=10, pady=10, sticky="nsew")

        self.but_minus = ctk.CTkButton(self.buttonframe, text='-', font =('Arial', 30), command=self.op_substraction)
        self.but_minus.grid(row=3, column=3, padx=10, pady=10, sticky="nsew")

        self.but_1 = ctk.CTkButton(self.buttonframe, text='1', font =('Arial', 30), command= self.update_text_1)
        self.but_1.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")

        self.but_2 = ctk.CTkButton(self.buttonframe, text='2', font =('Arial', 30), command= self.update_text_2)
        self.but_2.grid(row=4, column=1, padx=10, pady=10, sticky="nsew")

        self.but_3 = ctk.CTkButton(self.buttonframe, text='3', font =('Arial', 30), command= self.update_text_3)
        self.but_3.grid(row=4, column=2, padx=10, pady=10, sticky="nsew")

        self.but_plus = ctk.CTkButton(self.buttonframe, text='+', font =('Arial', 30), command= self.op_addition)
        self.but_plus.grid(row=4, column=3, padx=10, pady=10, sticky="nsew")

        self.but_0 = ctk.CTkButton(self.buttonframe, text='0', font =('Arial', 30), command= self.update_text_0)
        self.but_0.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.but_dot = ctk.CTkButton(self.buttonframe, text='.', font =('Arial', 30), command= self.update_text_dot)
        self.but_dot.grid(row=5, column=2, padx=10, pady=10, sticky="nsew")

        self.but_equal = ctk.CTkButton(self.buttonframe, text='=', font =('Arial', 30), command=self.equal)
        self.but_equal.grid(row=5, column=3, padx=10, pady=10, sticky="nsew")

        self.buttonframe.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.window.mainloop()

    old_text_list =[]
    addd = False
    subss= False
    multt = False
    divv= False

    def num_repeated(self):
        global addd
        global subss
        global multt
        global divv
        global old_text

        self.old_text = self.label.cget("text")

        if self.add > self.old_add:
            self.old_text_list.append(self.old_text)
            self.old_text = ''
            self.old_add = self.add 
            self.addd = True 

        if self.subs > self.old_subs:
            self.old_text_list.append(self.old_text)
            self.old_text = ''
            self.old_subs = self.subs 
            self.subss = True

        if self.div > self.old_div:
            self.old_text_list.append(self.old_text)
            self.old_text = ''
            self.old_div = self.div  
            self.divv = True


        if self.mult > self.old_mult:
            self.old_text_list.append(self.old_text)
            self.old_text = ''
            self.old_mult = self.mult
            self.multt = True   
               
              
        if self.old_text == '0':
            self.old_text = ''

    def update_text_C(self):
        self.label.configure(text= "0")
        self.old_text_list =[]
        self.addition= False
        self.substraction= False
        self.division = False
        self.multiplication =False
        self.addd = False
        self.subss= False
        self.multt = False
        self.divv= False

    def update_text_1(self):
        self.num_repeated()
        self.label.configure(text= self.old_text + "1")

    def update_text_2(self):
        self.num_repeated()
        self.label.configure(text= self.old_text + "2")

    def update_text_3(self):
        self.num_repeated()
        self.label.configure(text= self.old_text + "3")

    def update_text_4(self):
        self.num_repeated()
        self.label.configure(text= self.old_text + "4")

    def update_text_5(self):
        self.num_repeated()
        self.label.configure(text= self.old_text + "5")

    def update_text_6(self):
        self.num_repeated()
        self.label.configure(text= self.old_text + "6")

    def update_text_7(self):
        self.num_repeated()
        self.label.configure(text= self.old_text + "7")

    def update_text_8(self):
        self.num_repeated()
        self.label.configure(text= self.old_text + "8")
    
    def update_text_9(self):
        self.num_repeated()
        self.label.configure(text= self.old_text + "9")

    def update_text_0(self):
        self.num_repeated()
        self.label.configure(text= self.old_text + "0")

    def update_text_dot(self):
        self.old_text = self.label.cget("text")
        self.label.configure(text= self.old_text + ".")
    
    def check_type(self):
                self.old_text = self.label.cget("text")
                if type(self.old_text) == str:
                    if '.' in self.old_text:
                        self.old_text = float(self.old_text)
                    else:
                        self.old_text = int(self.old_text) 
                else:
                    pass
                if type(self.old_text_list[0]) == str:
                    if '.' in self.old_text_list[0]:
                        self.old_text_list[0] = float(self.old_text_list[0])
                    else:
                        self.old_text_list[0] = int(self.old_text_list[0])
                else:
                    pass
        
    
    def op_repeated(self):

        if self.addd:
            if len(self.old_text_list) == 1:
                self.check_type()
                self.result = self.old_text_list[0] + self.old_text
                self.label.configure(text= self.result)
                self.old_text_list = []
                self.addd = False

        if self.subss:
            if len(self.old_text_list) == 1:
                self.check_type()
                self.result = self.old_text_list[0] - self.old_text
                self.label.configure(text= self.result)
                self.old_text_list = []
                self.subss = False

        if self.multt:
            if len(self.old_text_list) == 1:
                self.check_type()
                self.result = self.old_text_list[0] * self.old_text
                self.label.configure(text= self.result)
                self.old_text_list = []
                self.multt = False

        if self.divv:
            if len(self.old_text_list) == 1:
                self.check_type()
                self.result = self.old_text_list[0] / self.old_text
                self.label.configure(text= self.result)
                self.old_text_list = []
                self.divv = False
    
    add=0
    old_add=0
    addition = False
    def op_addition(self):
        global add 
        global old_add
        global addition

        if self.add >= 0:
            self.old_add = self.add  #optional coz already declerad
            self.add = self.add +1   

        self.op_repeated()

        self.substraction,self.multiplication,self.division = False, False, False
        self.addition = True
            
    subs=0
    old_subs=0
    substraction = False
    def op_substraction(self):
        global subs 
        global old_subs
        global substraction

        if self.subs >= 0:
            self.old_subs = self.subs  #optional coz already declerad
            self.subs = self.subs +1   

        self.op_repeated()

        self.addition,self.multiplication,self.division = False, False, False
        self.substraction = True

    mult=0
    old_mult=0
    multiplication = False
    def op_multiply(self):
        global mult 
        global old_mult
        global multiplication

        if self.mult >= 0:
            self.old_mult = self.mult  #optional coz already declerad
            self.mult = self.mult +1   

        self.op_repeated()
   
        self.addition,self.substraction,self.division = False, False, False
        self.multiplication = True

    div=0
    old_div=0
    division = False
    def op_divide(self):
        global div 
        global old_div
        global division

        if self.div >= 0:
            self.old_div = self.div  #optional coz already declerad
            self.div = self.div +1   

        self.op_repeated()

        self.addition,self.multiplication,self.substraction = False, False, False
        self.division = True

    def op_percent(self):
        self.old_text = self.label.cget("text")
        if type(self.old_text) == str:
            if '.' in self.old_text:
                self.result = float(self.old_text) / 100
            else:
                self.result = int(self.old_text) / 100
        self.label.configure(text= self.result)

    def op_turn_negative(self):
        self.old_text = self.label.cget("text")
        if type(self.old_text) == str:
            if '.' in self.old_text:
                self.result = float(self.old_text) * -1
            else:
                self.result = int(self.old_text) * -1
        self.label.configure(text= self.result)
    
    def equal(self):
        self.old_text = self.label.cget("text")
        if type(self.old_text) == str:
            if '.' in self.old_text:
                self.old_text = float(self.old_text)
            else:
                self.old_text = int(self.old_text) 
        else:
            pass
        
        if type(self.old_text_list[0]) == str:
            if '.' in self.old_text_list[0]:
                self.old_text_list[0] = float(self.old_text_list[0])
            else:
                self.old_text_list[0] = int(self.old_text_list[0])
        else:
            pass


        if self.addition:
            self.result= self.old_text_list[0] + self.old_text
            self.addition = False
        
        if self.substraction:
            self.result= self.old_text_list[0] - self.old_text
            self.substraction = False

        if self.multiplication:
            self.result= self.old_text_list[0] * self.old_text
            self.multiplication = False
                
        if self.division:
            self.result= self.old_text_list[0] / self.old_text
            self.division = False

        self.label.configure(text= self.result)
        self.old_text_list= []

        self.addd = False
        self.multt = False
        self.divv = False
        self.subss = False



My_Calculator()
