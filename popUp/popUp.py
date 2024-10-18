import tkinter as tk
from tkinter import simpledialog, messagebox, ttk

class PopUp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()

    def display_results(self, message='Mensaje') -> None:
        """Function that displays a result to the user."""
        messagebox.showinfo('Resultado', message)

    def read_double(self, prompt='Ingrese un número decimal:') -> float:
        """Function that asks the user for a double value."""
        while True:
            user_input = simpledialog.askstring("Input", prompt)
            try:
                return float(user_input)
            except (TypeError, ValueError):
                messagebox.showerror('Error', 'Por favor, ingrese un número decimal válido')

    def read_int_greater_than(self, prompt='Ingrese un número: ', min_value=0, default_value=1) -> int:
        while True:
            try:
                user_input = simpledialog.askinteger('Input', f'{prompt} (Mayor que {min_value})', initialvalue=default_value)
                if user_input is None:
                    return default_value 
                if user_input > min_value:
                    return user_input
                else:
                    messagebox.showerror('Error', f'El número debe ser mayor que {min_value}')
            except ValueError:
                messagebox.showerror('Error', 'Ingrese un número entero válido')

    def yes_or_no(self, prompt='Desea continuar?') -> bool:
        """Function that asks the user a Yes or No question."""
        choice = messagebox.askyesno("Confirmación", prompt)
        return choice

    def read_menu_choice_buttons(self, prompt='Seleccione una opción', options=[]) -> int:
        """Function that presents a set of options and returns the index of the selected option."""
        choice = messagebox.askquestion(prompt, '\n'.join(options), icon='question')
        if choice in options:
            return options.index(choice)
        return -1 

    def read_menu_choice_index(self, prompt='Seleccione una opción', options=[]) -> int:
        """Function that presents a set of options and returns the index of the selected option using a combobox."""
        combo = ttk.Combobox(self.root, values=options)
        result = messagebox.askokcancel(prompt, combo)
        if result:
            return combo.current()
        return -1

    def read_menu_choice_string(self, prompt='Seleccione una opción', options=[]) -> str:
        """Function that returns the string of the selected option using a combobox."""

        window = tk.Toplevel(self.root)
        window.title(prompt)

        combo = ttk.Combobox(window, values=options, state="readonly")
        combo.set("Seleccione una opción")  
        combo.grid(column=0, row=0, padx=10, pady=10)

        selected_option = tk.StringVar()

        def confirm_selection():
            selected_option.set(combo.get())
            window.destroy()  

        confirm_button = tk.Button(window, text="Confirmar", command=confirm_selection)
        confirm_button.grid(column=0, row=1, padx=10, pady=10)

        window.wait_window()  

        return selected_option.get() if selected_option.get() != "Seleccione una opción" else ""


    def __del__(self):
        self.root.destroy()
