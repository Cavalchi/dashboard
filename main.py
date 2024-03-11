#http://http://127.0.0.1:8050
from tkinter import Tk, Label, Entry, Button, StringVar
import subprocess
import webbrowser

def submit_data():
    global stock_var, sold_per_day_var, sold_per_month_var
    stock = int(stock_var.get())
    sold_per_day = int(sold_per_day_var.get())
    sold_per_month = int(sold_per_month_var.get())
    with open('data.txt', 'w') as f:
        f.write(f'{stock},{sold_per_day},{sold_per_month}')

    # Inicia o script dash_app.py
    subprocess.Popen(["python", "dash_app.py"])

    # Abre o navegador no localhost na porta 8050
    webbrowser.open("http://127.0.0.1:8050")
root = Tk()

Label(root, text="Produtos em estoque:").grid(row=0, column=0)
stock_var = StringVar()
Entry(root, textvariable=stock_var).grid(row=0, column=1)

Label(root, text="Vendidos por dia:").grid(row=1, column=0)
sold_per_day_var = StringVar()
Entry(root, textvariable=sold_per_day_var).grid(row=1, column=1)

Label(root, text="Vendidos por mês:").grid(row=2, column=0)
sold_per_month_var = StringVar()
Entry(root, textvariable=sold_per_month_var).grid(row=2, column=1)

Button(root, text="Submit", command=submit_data).grid(row=3, column=0, columnspan=2)

root.mainloop()
