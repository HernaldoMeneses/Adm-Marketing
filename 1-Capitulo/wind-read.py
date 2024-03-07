import tkinter as tk

def mostrar_conteudo(arquivo):
    try:
        with open(arquivo, 'r') as f:
            conteudo = f.read()
            texto.delete(1.0, tk.END)  # Limpa o conteúdo existente
            texto.insert(tk.END, conteudo)  # Insere o novo conteúdo
    except FileNotFoundError:
        texto.delete(1.0, tk.END)
        texto.insert(tk.END, f'O arquivo {arquivo} não foi encontrado.')
    except Exception as e:
        texto.delete(1.0, tk.END)
        texto.insert(tk.END, f'Ocorreu um erro: {e}')

# Criação da janela principal
root = tk.Tk()
root.title("Visualizador de Arquivos")

# Define a transparência (opcional)
root.attributes("-alpha", 0.85)

# Frame para organizar widgets
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Lista de arquivos
file_names = [
    '1.1-importância.txt',
    '1.2-Escopo.txt']

# Combobox para selecionar o arquivo
combo_arquivos = tk.StringVar(value=file_names[0])
menu_arquivos = tk.OptionMenu(frame, combo_arquivos, *file_names)
menu_arquivos.grid(row=0, column=0, padx=5, pady=5)

# Botão para exibir o conteúdo do arquivo selecionado
btn_mostrar = tk.Button(frame, text="Mostrar Conteúdo", command=lambda: mostrar_conteudo(combo_arquivos.get()))
btn_mostrar.grid(row=0, column=1, padx=5, pady=5)

# Texto para exibir o conteúdo do arquivo
texto = tk.Text(root, wrap=tk.WORD, width=100, height=80)
texto.pack(pady=10)

# Inicia o loop principal
root.mainloop()
