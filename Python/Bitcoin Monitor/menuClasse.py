import tkinter
import customtkinter


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

class menu(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("400x400")
        self.title("Criptcoin Monitor")

    # FRAMES SECTION
        #FRAMES DECLARATIONS
        self.master_frame = customtkinter.CTkFrame(
            master=self, width=800, height=400)
        
        self.options_frame = customtkinter.CTkFrame(
            master=self.master_frame, width=10, height=10)
        
        self.textbox_frame = customtkinter.CTkFrame(
            master=self.master_frame, width=200, height=100)


        #FRAMES PLACES
        self.master_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        self.options_frame.grid(row=0, column=1, padx=10, pady=10)
    #-------------------------------------------------------------------------------------------------------------

    # WIDGET SECTION
        # WIDGETS VARIABLES
        self.radio_button_var = customtkinter.IntVar()
       

        #WIDGETS DECLARATIONS
        self.label = customtkinter.CTkLabel(
            master=self,font=customtkinter.CTkFont(size=22), text="Bem vindo ao Criptocoin Monitor!")

        self.currency_option = customtkinter.CTkComboBox(
            master=self.options_frame, values=["BTC"])
        
        self.day_entry = customtkinter.CTkEntry(
            master=self.options_frame, placeholder_text="Qtd. de dias")

        self.radio_button_1 = customtkinter.CTkRadioButton(
            master=self.options_frame, value=1, variable=self.radio_button_var, command=self.radio_button_function, text="Cotação atual")
        self.radio_button_2 = customtkinter.CTkRadioButton(
            master=self.options_frame, value=2, variable=self.radio_button_var, command=self.radio_button_function, text="Cotação por dias")
        self.radio_button_1.select()
        
        self.button = customtkinter.CTkButton(
            master=self, command=self.exec, text="Concluir")
        
        self.textbox = customtkinter.CTkTextbox(
            master=self.textbox_frame, font=("Fira Mono", 12))


        #WIDGETS PLACES
        self.label.place(
            relx=0.5, rely=0.1, anchor=tkinter.CENTER)
        
        self.button.place(
            relx=0.5, rely=0.9, anchor=tkinter.CENTER)
        
        self.currency_option.grid(
            row=1, column=0, padx=10, pady=10)
        
        self.radio_button_1.grid(
            row=2, column=0, padx=10, pady=10)
        
        self.radio_button_2.grid(
            row=3, column=0, padx=10, pady=10)
        
        
        #-------------------------------------------------------------------------------------------------------------

    def radio_button_function(self):
        if self.radio_button_var.get() == 1:
            print("Radio Button value: {}".format(self.radio_button_var.get()))
            self.day_entry.grid_remove()

            
        elif self.radio_button_var.get() == 2:
            print("Radio Button value: {}".format(self.radio_button_var.get()))

            self.day_entry.grid(
            row=4, column=0, padx=10, pady=10)

            
    def grid_textbox(self):
        
        self.geometry("700x500")

        self.textbox_frame.grid(
            row=0, column=0, padx=10, pady=10)

        self.textbox.grid(
            row=0, column=0, padx=10, pady=10, ipadx=80, ipady=50)

    def exec(self):


        self.grid_textbox()

        if (self.radio_button_var.get() == 1):
            import get_current_exchange
            get_current_exchange.get_currency_exchange(self, self.currency_option.get())

        elif (self.radio_button_var.get() == 2):
            import get_exchange_by_days
            get_exchange_by_days.get_currency_exchange(self, self.currency_option.get(), int(self.day_entry.get()))

        else:
            print("OPÇÃO INVÁLIDA")

    def insert_text(self, string):
        
        self.textbox.insert(tkinter.INSERT, "{}".format(string))
