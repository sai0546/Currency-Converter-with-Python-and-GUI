import tkinter as tk
from tkinter import messagebox


def open_signup():
    login_frame.pack_forget()
    signup_frame.pack()

 
def check_login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "password":
        messagebox.showinfo("Login", "Login successful!")
        login_frame.pack_forget()
        currency_converter_frame.pack()
    else:
        messagebox.showerror("Login", "Invalid credentials. Please try again.")

def open_login():
    signup_frame.pack_forget()
    login_frame.pack()

def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_var.get()
        to_currency = to_currency_var.get()

        exchange_rates = {
            "USD": {"EUR": 0.92, "INR": 82.74, "GBP": 0.76, "AUD": 1.43},
            "EUR": {"USD": 1.09, "INR": 89.76, "GBP": 0.83, "AUD": 1.55},
            "INR": {"USD": 0.012, "EUR": 0.011, "GBP": 0.0093, "AUD": 0.017},
            "GBP": {"USD": 1.31, "EUR": 1.20, "INR": 107.47, "AUD": 1.87},
            "AUD": {"USD": 0.70, "EUR": 0.65, "INR": 57.86, "GBP": 0.54},
        }

        if from_currency != to_currency:
            converted_amount = amount * exchange_rates[from_currency][to_currency]
            result_label.config(text=f"Converted Amount: {converted_amount:.2f} {to_currency}")
            history.append(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
        else:
            messagebox.showerror("Error", "From and To currencies cannot be the same.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")


def show_history():
    history_window = tk.Toplevel(root)
    history_window.title("Conversion History")
    history_window.geometry("400x300")
    tk.Label(history_window, text="Conversion History", font=("Arial", 14)).pack(pady=10)
    
    history_text = tk.Text(history_window, wrap=tk.WORD, width=50, height=15)
    history_text.pack(padx=10, pady=10)
    
    for entry in history:
        history_text.insert(tk.END, entry + "\n")
    history_text.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Login Page")
root.geometry("1300x600")
root.configure(bg="skyblue")
root.eval('tk::PlaceWindow . center')

# Login frame
login_frame = tk.Frame(root, width=500, height=800)
login_frame.pack_propagate(False)
login_frame.pack()

username_label = tk.Label(login_frame, text="Username:")
username_label.pack()
username_entry = tk.Entry(login_frame)
username_entry.pack()

password_label = tk.Label(login_frame, text="Password:")
password_label.pack()
password_entry = tk.Entry(login_frame, show="*")
password_entry.pack()

login_button = tk.Button(login_frame, text="Login", command=check_login)
login_button.pack()

signup_button = tk.Button(login_frame, text="Don't have an account? Sign up", command=open_signup)
signup_button.pack()

# Signup frame
signup_frame = tk.Frame(root, width=500, height=800)
signup_frame.pack_propagate(False)

signup_label = tk.Label(signup_frame, text="Signup Page")
signup_label.pack()

username_signup_label = tk.Label(signup_frame, text="Username:")
username_signup_label.pack()
username_signup_entry = tk.Entry(signup_frame)
username_signup_entry.pack()

password_signup_label = tk.Label(signup_frame, text="Password:")
password_signup_label.pack()
password_signup_entry = tk.Entry(signup_frame, show="*")
password_signup_entry.pack()

confirm_password_label = tk.Label(signup_frame, text="Confirm Password:")
confirm_password_label.pack()
confirm_password_entry = tk.Entry(signup_frame, show="*")
confirm_password_entry.pack()

signup_button_action = tk.Button(signup_frame, text="Sign Up", command=open_login)
signup_button_action.pack()

back_to_login_button = tk.Button(signup_frame, text="Back to Login", command=open_login)
back_to_login_button.pack()

# Currency Converter Frame
currency_converter_frame = tk.Frame(root, width=500, height=800)
currency_converter_frame.pack_propagate(False)

amount_label = tk.Label(currency_converter_frame, text="Amount:")
amount_label.pack()

amount_entry = tk.Entry(currency_converter_frame)
amount_entry.pack()

from_currency_label = tk.Label(currency_converter_frame, text="From Currency:")
from_currency_label.pack()
from_currency_var = tk.StringVar(currency_converter_frame)
from_currency_var.set("SELECT")
from_currency_menu = tk.OptionMenu(currency_converter_frame, from_currency_var, "USD", "EUR", "INR", "GBP", "AUD")
from_currency_menu.pack()

to_currency_label = tk.Label(currency_converter_frame, text="To Currency:")
to_currency_label.pack()
to_currency_var = tk.StringVar(currency_converter_frame)
to_currency_var.set("SELECT")
to_currency_menu = tk.OptionMenu(currency_converter_frame, to_currency_var, "USD", "EUR", "INR", "GBP", "AUD")
to_currency_menu.pack()

convert_button = tk.Button(currency_converter_frame, text="Convert", command=convert_currency)
convert_button.pack()

result_label = tk.Label(currency_converter_frame, text="Converted Amount: ")
result_label.pack()

history_button = tk.Button(currency_converter_frame, text="History", command=show_history)
history_button.pack()


history = []


root.mainloop()
