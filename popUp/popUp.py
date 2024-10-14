import tkinter as tk
from tkinter import simpledialog, messagebox, ttk

class PopUp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()

    def run(self):
        print('me tocó quitar el while por tu culpa y tu bullying')


    def display_results(self, message='Mensaje') -> None:
        messagebox.showinfo('Mensaje', message)

    def read_yes_or_no(self, question='Desea continuar?') -> bool:
        return messagebox.askyesno("Pregunta", question)
    
    def read_double(self, prompt='Ingrese un número decimal:') -> float:
        while True:
            try:
                user_input = simpledialog.askfloat('Input', prompt)
                if user_input is None:
                    return 0.0
            except ValueError:
                messagebox.showerror('Error', 'Por favor, ingrese un número decimal válido')
    
    def read_int_greater_than(self, prompt= 'Ingrese un número: ', min_value = 0) -> int:
        while True:
            try:
                user_input = simpledialog.askinteger('Input', f'{prompt} (Mayor que {min_value})')
                if user_input is None:
                    return min_value
                if user_input > min_value:
                    return user_input
                else:
                    messagebox.showerror('Error', f'El número debe ser mayor que {min_value}')
            except ValueError:
                messagebox.showerror('Error', 'ingrese un número entero válido')

    def read_menu_choice_buttons(self, prompt='Seleccione una opción', options=[]) -> int:
        selected_option = simpledialog.askstring('Input', f'{prompt}\nOpciones: {', '.join(options)}')
        if selected_option in options:
            return options.index(selected_option)
        return -1  

    def read_menu_choice_index(self, prompt='Seleccione una opción', options=[]) -> int:
        selection = simpledialog.askinteger('Input', f'{prompt}\nSeleccione un número entre 1 y {len(options)}')
        if selection is not None and 1 <= selection <= len(options):
            return selection - 1
        return -1

    def read_menu_choice_string(self, prompt='Seleccione una opción', options=[]) -> str:
        selected_option = simpledialog.askstring('Input', f'{prompt}\nOpciones: {', '.join(options)}')
        if selected_option in options:
            return selected_option
        return "" 

    def __del__(self):
        self.root.destroy()