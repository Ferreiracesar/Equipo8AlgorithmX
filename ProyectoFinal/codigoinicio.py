import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk


class PlantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Plantas")
        self.root.attributes("-fullscreen", True)

        self.plants = [] 

        self.list_frame = tk.Frame(root, bg="#829F4D")

        self.add_frame = tk.Frame(root, bg="#829F4D")

        self.reco_frame = tk.Frame(root, bg="#E3DAC9")

        self.info_frame = tk.Frame(root, bg="#829F4D")


        # Inicializar frames como un diccionario vacío
        self.frames = {}
        
        # Crear los frames principales
        self.create_frames()
        


        self.frames["default_frame"].pack(fill="both", expand=True)




    def create_frames(self):
        """Crear todos los frames necesarios para el flujo."""
        self.frames = {}
        self.frames["default_frame"] = tk.Frame(self.root, bg="#DECB76")  # Nuevo frame inicial
        self.frames["reco_frame"] = tk.Frame(self.root, bg="#E3DAC9")
        self.frames["clima_frame"] = tk.Frame(self.root, bg="#829F4D")
        self.frames["tempo_frame"] = tk.Frame(self.root, bg="#FFDAB9")
        self.frames["type_frame"] = tk.Frame(self.root, bg="#D8BFD8")
        self.frames["space_frame"] = tk.Frame(self.root, bg="#F5DEB3")
        self.frames["final_frame"] = tk.Frame(self.root, bg="#ADD8E6")

        # Crear contenido en cada frame
        self.create_main_menu()
        self.create_reco_frame()
        self.create_clima_frame()
        self.create_tempo_frame()
        self.create_type_frame()
        self.create_space_frame()
        self.create_final_frame()



    def showi_frame(self, frame):
        """Ocultar todos los frames y mostrar el frame seleccionado."""
        for widget in self.root.winfo_children():
            widget.pack_forget()
        frame.pack(fill="both", expand=True)

    
            




    def create_navigation(self, frame, title, back_to):
        header = tk.Frame(frame, bg="#DECB76")
        header.pack(fill="x")
        
        title_label = tk.Label(header, text=title, font=("Arial", 28, "bold"), bg="#DECB76")
        title_label.pack(side="left", padx=40, pady=40)

        ruta_imagen = "img/salir.png" 
        imagen = Image.open(ruta_imagen)
        imagen = imagen.resize((40, 40)) 
        salir_imagen_tk = ImageTk.PhotoImage(imagen)

        salir_button = tk.Button(header, image=salir_imagen_tk, command=self.root.destroy, bg="#DECB76", borderwidth=0)
        salir_button.image = salir_imagen_tk
        salir_button.pack(side="right", padx=10, pady=10)

        if frame != self.showi_frame(self.frames["default_frame"]):
            volver_button = tk.Button(header, text="Volver", command=lambda: self.showi_frame(self.frames["default_frame"]), bg="red", fg="white")
            volver_button.pack(side="right", padx=10, pady=10)


        if frame == self.reco_frame:
            header.config(bg="#E3DAC9")
            title_label.config(bg="#E3DAC9")
            salir_button.config(bg="#E3DAC9")

        if frame == self.list_frame:
            header.config(bg="#829F4D")
            title_label.config(bg="#829F4D")
            salir_button.config(bg="#829F4D")



    def show_frame(self, frame):
        for widget in self.root.winfo_children():
            widget.pack_forget()
        frame.pack(fill="both", expand=True)

    def create_main_menu(self):


        self.create_navigation(self.frames["default_frame"], "Menu Principal", self.frames["default_frame"])


        ruta_imagen = "img/logo.png" 
        imagen = Image.open(ruta_imagen)
        imagen = imagen.resize((200, 200))
        imagen_tk = ImageTk.PhotoImage(imagen)

        

        label_imagen = tk.Label(self.frames["default_frame"], image=imagen_tk, bg="#DECB76")
        label_imagen.image = imagen_tk
        label_imagen.pack(pady=20) 


        tk.Label(self.frames["default_frame"], text="Elige la opcion que desees ver o utilizar.", bg="#DECB76", fg="white", font=("Arial", 24, "bold")).pack(pady=20)

        tk.Button(self.frames["default_frame"], text="Listar Plantas", bg="#829F4D", font=("Arial", 16),
                  command=lambda: self.show_frame(self.list_frame)).pack(pady=10)

        tk.Button(self.frames["default_frame"], text="Agregar Planta", bg="#829F4D", font=("Arial", 16),
                  command=lambda: self.show_frame(self.add_frame)).pack(pady=10)
        
        tk.Button(self.frames["default_frame"], text="Recomendaciones", bg="#829F4D", font=("Arial", 16),
                  command=lambda: self.showi_frame(self.frames["reco_frame"])).pack(pady=10)

        self.create_list_frame()
        self.create_add_frame()
        self.create_reco_frame()

        


    def create_list_frame(self):
        self.create_navigation(self.list_frame, "Lista de Plantas", self.showi_frame(self.frames["default_frame"]))

        list_container = tk.Frame(self.list_frame, bg="#829F4D")
        list_container.pack(pady=20)

        def update_plant_list():
            for widget in list_container.winfo_children():
                widget.destroy()
            if self.plants:
                rows = len(self.plants) // 2 + (len(self.plants) % 2)
                for row in range(rows):
                    row_frame = tk.Frame(list_container, bg="#829F4D")
                    row_frame.pack(fill="x", pady=10)

                    if row * 2 < len(self.plants):
                        create_plant_widget(row_frame, self.plants[row * 2]).pack(side="left", padx=20)

                    if row * 2 + 1 < len(self.plants):
                        create_plant_widget(row_frame, self.plants[row * 2 + 1]).pack(side="left", padx=20)

            else:
                tk.Label(list_container, text="No hay plantas registradas", bg="#829F4D", font=("Arial", 14)).pack()

        def create_plant_widget(parent, plant):
            """Crea una tarjeta más grande con imagen y texto para una planta."""
            plant_frame = tk.Frame(parent, bd=2, relief="solid", padx=15, pady=15, width=400, height=200, bg="#829F4D")
            plant_frame.pack_propagate(False) 


            content_frame = tk.Frame(plant_frame, bg="#829F4D")
            content_frame.pack(fill="both", expand=True)

            if plant.get("image"):
                from PIL import Image, ImageTk
                try:
                    img = Image.open(plant["image"])
                    img = img.resize((150, 150)) 
                    photo = ImageTk.PhotoImage(img)
                    image_label = tk.Label(content_frame, image=photo, bg="#829F4D")
                    image_label.image = photo 
                    image_label.pack(side="left", padx=10, pady=10)
                except Exception as e:
                    tk.Label(content_frame, text="Img. no disponible",bg="#829F4D", font=("Arial", 10), fg="gray").pack(side="left", padx=10, pady=10)
            else:
                tk.Label(content_frame, text="Sin imagen", font=("Arial", 10), fg="gray").pack(side="left", padx=10, pady=10)

            text_frame = tk.Frame(content_frame, bg="#829F4D")
            text_frame.pack(side="left", fill="x", expand=True, padx=10)

            tk.Label(text_frame, text=plant["name"], bg="#829F4D", font=("Arial", 16), anchor="w").pack(pady=5)

            tk.Button(text_frame, text="Ver detalles", bg="#E3DAC9", font=("Arial", 12),
                    command=lambda p=plant: self.show_plant_info(p)).pack(pady=5)

            tk.Button(text_frame, text="Eliminar", bg="#E3DAC9", font=("Arial", 12), fg="red",
                    command=lambda p=plant: delete_plant(p)).pack(pady=5)

            return plant_frame
        

        def delete_plant(plant):
            """Elimina la planta seleccionada de la lista."""
            confirm = messagebox.askyesno("Confirmar", f"¿Estás seguro de que deseas eliminar '{plant['name']}'?")
            if confirm:
                self.plants.remove(plant) 
                update_plant_list() 
                messagebox.showinfo("Eliminada", f"La planta '{plant['name']}' ha sido eliminada.")

        def delete_plant(plant):
            """Elimina la planta seleccionada de la lista utilizando pantallas personalizadas."""

            def confirm_delete():
                """Confirma y elimina la planta."""
                self.plants.remove(plant) 
                update_plant_list() 
                confirm_window.destroy() 

                success_window = tk.Toplevel(self.root)
                success_window.title("Eliminada")
                success_window.geometry("700x300")
                success_window.configure(bg="#829F4D")

                success_label = tk.Label(
                    success_window,
                    text=f"La planta '{plant['name']}' fue eliminada :D",
                    font=("Arial", 16, "bold"),
                    bg="#829F4D",
                    fg="white",
                )
                success_label.pack(expand=True)

                tk.Button(
                    success_window,
                    text="Cerrar",
                    font=("Arial", 14),
                    bg="#E3DAC9",
                    command=success_window.destroy,
                ).pack(pady=20)

            confirm_window = tk.Toplevel(self.root)
            confirm_window.title("Confirmar Eliminación")
            confirm_window.geometry("700x300")
            confirm_window.configure(bg="#829F4D")

            confirm_frame = tk.Frame(confirm_window, bg="white", width=350, height=150)
            confirm_frame.place(relx=0.5, rely=0.5, anchor="center")

            confirm_label = tk.Label(
                confirm_frame,
                text="¿Seguro que quieres eliminar esta planta?",
                font=("Arial", 14),
                bg="white",
            )
            confirm_label.pack(pady=20)

            tk.Button(
                confirm_frame,
                text="Sí",
                font=("Arial", 14),
                bg="#E3DAC9",
                command=confirm_delete,
            ).pack(side="left", padx=20, pady=10)

            tk.Button(
                confirm_frame,
                text="No",
                font=("Arial", 14),
                bg="#E3DAC9",
                command=confirm_window.destroy,
            ).pack(side="right", padx=20, pady=10)


        update_plant_list()

        tk.Button(self.list_frame, text="Actualizar Lista", bg="#E3DAC9", font=("Arial", 14), command=update_plant_list).pack(pady=10)