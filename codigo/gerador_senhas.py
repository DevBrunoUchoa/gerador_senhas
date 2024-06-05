import tkinter as tk
from tkinter import messagebox
import random
import string


def gerar_senhas(n):
    if n < 4:
        return None
    caracteres = string.ascii_letters + string.digits + "!@#$%&*()-_=+[]{}|;:,.<>?/"
    senha = [random.choice(string.ascii_lowercase),
             random.choice(string.ascii_uppercase),
             random.choice(string.digits),
             random.choice("!@#$%&*()-_=+[]{}|;:,.<>?/")]
    senha += random.choices(caracteres, k=n - 4)
    random.shuffle(senha)
    return ''.join(senha)


def exibir_senha():
    try:
        num_caracteres = int(entrada.get())
        if 8 <= num_caracteres <= 25:
            senha = gerar_senhas(num_caracteres)
            janela.clipboard_clear()
            janela.clipboard_append(senha)
            messagebox.showinfo("Senha Gerada",
                                f"Sua senha é: {senha}\nA senha foi copiada para a área de transferência.")
        else:
            messagebox.showwarning("Erro ao gerar senha", "Por favor, insira um número entre 8 e 25.")
    except ValueError:
        messagebox.showwarning("Erro ao gerar senha", "Por favor, insira um número válido.")


janela = tk.Tk()
janela.title('Gerador de Senhas')
janela.geometry('300x200')

tk.Label(janela, text='Digite o número de caracteres para sua senha (8-25)').pack(pady=10)
entrada = tk.Entry(janela, width=30)
entrada.pack(pady=10)
tk.Button(janela, text='Gerar Senha', command=exibir_senha).pack(pady=10)

janela.mainloop()
