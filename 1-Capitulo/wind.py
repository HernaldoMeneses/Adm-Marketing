import tkinter as tk

# Função para fechar a janela
def fechar_janela():
    root.destroy()

# Criação da janela principal
root = tk.Tk()
root.title("Janela Transparente")

# Define a transparência (0 = totalmente transparente, 1 = totalmente opaca)
root.attributes("-alpha", 0.8)

# Define a largura e altura da janela
largura = 400
altura = 300
root.geometry(f"{largura}x{altura}")


# Adiciona um botão para fechar a janela
btn_fechar = tk.Button(root, text="Fechar Janela", command=fechar_janela)
btn_fechar.pack(pady=20)

# Inicia o loop principal
root.mainloop()
