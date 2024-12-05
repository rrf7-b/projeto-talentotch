import tkinter as tk

# Funções para as operações matemáticas
def adicionar():
    try:
        resultado = float(entry_num1.get()) + float(entry_num2.get())
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        label_resultado.config(text="Erro! Digite números válidos.")

def subtrair():
    try:
        resultado = float(entry_num1.get()) - float(entry_num2.get())
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        label_resultado.config(text="Erro! Digite números válidos.")

def multiplicar():
    try:
        resultado = float(entry_num1.get()) * float(entry_num2.get())
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        label_resultado.config(text="Erro! Digite números válidos.")

def dividir():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        if num2 == 0:
            label_resultado.config(text="Erro! Divisão por zero.")
        else:
            resultado = num1 / num2
            label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        label_resultado.config(text="Erro! Digite números válidos.")

# Criando a janela principal
root = tk.Tk()
root.title("Calculadora Simples")

# Labels
label_num1 = tk.Label(root, text="Digite o primeiro número:")
label_num1.pack()

entry_num1 = tk.Entry(root)
entry_num1.pack()

label_num2 = tk.Label(root, text="Digite o segundo número:")
label_num2.pack()

entry_num2 = tk.Entry(root)
entry_num2.pack()

label_resultado = tk.Label(root, text="Resultado:")
label_resultado.pack()

# Botões para as operações
btn_adicionar = tk.Button(root, text="Adicionar", command=adicionar)
btn_adicionar.pack()

btn_subtrair = tk.Button(root, text="Subtrair", command=subtrair)
btn_subtrair.pack()

btn_multiplicar = tk.Button(root, text="Multiplicar", command=multiplicar)
btn_multiplicar.pack()

btn_dividir = tk.Button(root, text="Dividir", command=dividir)
btn_dividir.pack()

# Rodando a interface gráfica
root.mainloop()
