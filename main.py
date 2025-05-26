from rembg import remove
from PIL import Image, ImageTk
import io
import os
import threading
import tkinter as tk
from tkinter import filedialog, messagebox

selected_image_path = None
window = tk.Tk()
window.title("Removedor de Fundo")
window.geometry("600x400")
window.configure(bg="#fffcdd")

# Label do topo
label1 = tk.Label(window, text="Remover o fundo de uma imagem",
                  bg="#fffcdd", fg="#353130", font=("Arial", 16, "bold"))
label1.pack(pady=20)

# Label do caminho da imagem
label2 = tk.Label(window, text="Selecione uma imagem para remover o fundo",
                  bg="#414141", fg="white", font=("Arial", 12, "bold"),
                  wraplength=500, justify="center", relief="solid", padx=10, pady=10)
label2.pack(pady=10)

def selecionar_imagem():
    global selected_image_path
    file_path = filedialog.askopenfilename(filetypes=[("Imagens", "*.png *.jpg *.jpeg *.bmp")])
    if file_path:
        selected_image_path = file_path
        label2.config(text=file_path)
    else:
        selected_image_path = None
        label2.config(text="Selecione uma imagem para remover o fundo")

def remover_fundo():
    def processar():
        if not selected_image_path:
            messagebox.showwarning("Aviso", "Nenhum arquivo selecionado.")
            return

        carregando = tk.Toplevel(window)
        carregando.title("Processando...")
        carregando.geometry("300x80")
        carregando.transient(window)
        carregando.grab_set()
        tk.Label(carregando, text="Removendo fundo, aguarde...",
                 font=("Arial", 12)).pack(pady=20)

        try:
            with open(selected_image_path, "rb") as img:
                input_data = img.read()
                output_data = remove(input_data)

            result = Image.open(io.BytesIO(output_data)).convert("RGBA")

            base = os.path.splitext(os.path.basename(selected_image_path))[0]
            suggested_name = f"{base}-sem-fundo.png"

            save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                     filetypes=[("PNG Files", "*.png")],
                                                     initialfile=suggested_name,
                                                     title="Salvar imagem sem fundo")
            carregando.destroy()

            if save_path:
                result.save(save_path,"PNG")
                messagebox.showinfo("Sucesso", f"Fundo removido com sucesso!\nArquivo salvo como: {save_path}")
            else:
                messagebox.showwarning("Cancelado", "Operação cancelada pelo usuário.")

        except Exception as e:
            carregando.destroy()
            messagebox.showerror("Erro", f"Erro ao remover o fundo:\n{str(e)}")

    # Rodar em thread separada para evitar travar a interface
    threading.Thread(target=processar).start()

# Botões
botao1 = tk.Button(window, text="Selecionar Imagem", command=selecionar_imagem,
                   bg="#95c68f", fg="#353130", font=("Arial", 12, "bold"),
                   width=20, height=2, cursor="hand2")
botao1.pack(pady=10)

botao2 = tk.Button(window, text="Remover Fundo", command=remover_fundo,
                   bg="#95c68f", fg="#353130", font=("Arial", 12, "bold"),
                   width=20, height=2, cursor="hand2")
botao2.pack(pady=10)

window.mainloop()
