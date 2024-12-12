import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
import re
import json
import os
import sys  
import shutil




def obtener_ruta_datos(nombre_archivo):
    carpeta_datos = os.path.join(os.path.expanduser("~"), "Datos_plantas")
    os.makedirs(carpeta_datos, exist_ok=True)
    return os.path.join(carpeta_datos, nombre_archivo)

def inicializar_archivo_datos_plantas():
    ruta_destino = obtener_ruta_datos("plantas.txt")
    if not os.path.exists(ruta_destino):
        with open(ruta_destino, "w") as f:
            f.write("")  # Crear archivo vacío

def cargar_plantas():
    try:
        with open(ruta_archivo, "r") as f:
            for linea in f:
                if linea.strip():
                    plantas.append(json.loads(linea.strip()))
    except Exception as e:
        print(f"Error al cargar plantas: {e}")
    return plantas

def guardar_planta(planta):
    ruta_archivo = obtener_ruta_datos("plantas.txt")
    try:
        with open(ruta_archivo, "a") as f:
            f.write(json.dumps(planta) + "\n")
    except Exception as e:
        print(f"Error al guardar la planta: {e}")

plantas = []
inicializar_archivo_datos_plantas()
ruta_archivo = obtener_ruta_datos("plantas.txt")


USER_DATA_FILE = "users.json"

# Cargar usuarios existentes
if not os.path.exists(USER_DATA_FILE):
    with open(USER_DATA_FILE, "w") as f:
        json.dump([], f)

def load_users():
    with open(USER_DATA_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USER_DATA_FILE, "w") as f:
        json.dump(users, f)

def validate_email(email):
    # Validar formato del correo electrónico
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email)

class Login: 
    def __init__(self, root):
        self.root = root
        self.root.title("Login/Signup")
        self.root.attributes("-fullscreen", True)
        self.root.config(bg='#E3DAC9')  # Color de fondo

        self.create_login_frame()
        self.create_signup_frame()
        self.create_recover_frame()

        self.show_login_screen()

    def create_login_frame(self):
        self.frame_login = tk.Frame(self.root, bg='#E3DAC9', pady=30)
        self.frame_login.pack()

        tk.Label(self.frame_login, text="Bienvenido!", font=("Helvetica", 24, "bold"), bg='#E3DAC9').grid(row=0, columnspan=2)
        tk.Label(self.frame_login, text="👤", font=("Helvetica", 80), bg='#E3DAC9').grid(row=1, columnspan=2, pady=10)

        tk.Label(self.frame_login, text="Correo electrónico", font=("Arial", 10), bg='#E3DAC9').grid(row=2, column=0, pady=10, sticky="w")
        self.entry_email_login = tk.Entry(self.frame_login, font=("Arial", 12))
        self.entry_email_login.grid(row=2, column=1, pady=10, sticky="w")

        tk.Label(self.frame_login, text="Contraseña", font=("Arial", 10), bg='#E3DAC9').grid(row=3, column=0, pady=10, sticky="w")
        self.entry_password_login = tk.Entry(self.frame_login, show='*', font=("Arial", 12))
        self.entry_password_login.grid(row=3, column=1, pady=10, sticky="w")

        tk.Button(self.frame_login, text="Iniciar sesión", bg="#DECB76", font=("Arial", 12), command=self.login, relief="flat", width=20).grid(row=5, columnspan=2, pady=15)
        tk.Button(self.frame_login, text="Registrarse", bg="#DECB76", font=("Arial", 12), command=self.show_signup_screen, relief="flat", width=20).grid(row=6, columnspan=2)
        tk.Button(self.frame_login, text="Recuperar contraseña", bg="#DECB76", font=("Arial", 12), command=self.show_recover_screen, relief="flat", width=20).grid(row=7, columnspan=2)
        tk.Button(self.frame_login, text="Salir", bg="#DECB76", font=("Arial", 12), command=self.exit_application, relief="flat", width=20).grid(row=8, columnspan=2, pady=15)

    def create_signup_frame(self):
        self.frame_signup = tk.Frame(self.root, bg='#E3DAC9', pady=30)

        tk.Label(self.frame_signup, text="Registrarse", font=("Helvetica", 24, "bold"), bg='#E3DAC9').grid(row=0, columnspan=2)
        tk.Label(self.frame_signup, text="👤", font=("Helvetica", 80), bg='#E3DAC9').grid(row=1, columnspan=2, pady=10)

        tk.Label(self.frame_signup, text="Nombre", font=("Arial", 10), bg='#E3DAC9').grid(row=2, column=0, pady=10, sticky="w")
        self.entry_first_name = tk.Entry(self.frame_signup, font=("Arial", 12))
        self.entry_first_name.grid(row=2, column=1, pady=10, sticky="w")

        tk.Label(self.frame_signup, text="Apellido", font=("Arial", 10), bg='#E3DAC9').grid(row=3, column=0, pady=10, sticky="w")
        self.entry_last_name = tk.Entry(self.frame_signup, font=("Arial", 12))
        self.entry_last_name.grid(row=3, column=1, pady=10, sticky="w")

        tk.Label(self.frame_signup, text="Correo electrónico", font=("Arial", 10), bg='#E3DAC9').grid(row=4, column=0, pady=10, sticky="w")
        self.entry_email = tk.Entry(self.frame_signup, font=("Arial", 12))
        self.entry_email.grid(row=4, column=1, pady=10, sticky="w")

        tk.Label(self.frame_signup, text="Contraseña", font=("Arial", 10), bg='#E3DAC9').grid(row=5, column=0, pady=10, sticky="w")
        self.entry_password_signup = tk.Entry(self.frame_signup, show='*', font=("Arial", 12))
        self.entry_password_signup.grid(row=5, column=1, pady=10, sticky="w")

        tk.Button(self.frame_signup, text="Registrarse", bg="#DECB76", font=("Arial", 12), command=self.signup, relief="flat", width=20).grid(row=6, columnspan=2, pady=15)
        tk.Button(self.frame_signup, text="Volver", bg="#DECB76", font=("Arial", 12), command=self.show_login_screen, relief="flat", width=20).grid(row=7, columnspan=2)

    def create_recover_frame(self):
        self.frame_recover = tk.Frame(self.root, bg='#E3DAC9', pady=30)

        tk.Label(self.frame_recover, text="Recuperar Contraseña", font=("Helvetica", 24, "bold"), bg='#E3DAC9').grid(row=0, columnspan=2)
        tk.Label(self.frame_recover, text="📧", font=("Helvetica", 80), bg='#E3DAC9').grid(row=1, columnspan=2, pady=10)

        tk.Label(self.frame_recover, text="Correo electrónico", font=("Arial", 10), bg='#E3DAC9').grid(row=2, column=0, pady=10, sticky="w")
        self.entry_email_recover = tk.Entry(self.frame_recover, font=("Arial", 12))
        self.entry_email_recover.grid(row=2, column=1, pady=10, sticky="w")

        tk.Button(self.frame_recover, text="Recuperar", bg="#DECB76", font=("Arial", 12), command=self.recover_password, relief="flat", width=20).grid(row=3, columnspan=2, pady=15)
        tk.Button(self.frame_recover, text="Volver", bg="#DECB76", font=("Arial", 12), command=self.show_login_screen, relief="flat", width=20).grid(row=4, columnspan=2)

    def show_login_screen(self):
        self.frame_signup.pack_forget()
        self.frame_recover.pack_forget()
        self.frame_login.pack()

    def show_signup_screen(self):
        self.frame_login.pack_forget()
        self.frame_recover.pack_forget()
        self.frame_signup.pack()

    def show_recover_screen(self):
        self.frame_login.pack_forget()
        self.frame_recover.pack()

    def exit_application(self):
        self.root.destroy()

    def login(self): 
        email = self.entry_email_login.get() 
        password = self.entry_password_login.get() 
        users = load_users() 

        for user in users: 
            if user["email"] == email and user["password"] == password: 
                messagebox.showinfo("Éxito", f"¡Bienvenido {user['first_name']}!") 
                self.root.destroy()  # Cerrar la ventana de inicio de sesión 
                # Crear una nueva ventana para PlantApp
                new_root = tk.Tk()  # Crear una nueva instancia de Tk
                app = PlantApp(new_root)  # Iniciar la clase PlantApp
                new_root.mainloop()  # Iniciar el bucle principal de la nueva ventana
                return 

        messagebox.showerror("Error", "¡Correo o contraseña incorrectos!") 

    def signup(self):
        first_name = self.entry_first_name.get()
        last_name = self.entry_last_name.get()
        email = self.entry_email.get()
        password = self.entry_password_signup.get()
        users = load_users()

        if not first_name or not last_name or not email or not password:
            messagebox.showerror("Error", "¡Todos los campos son obligatorios!")
            return

        if not validate_email(email):
            messagebox.showerror("Error", "¡Correo electrónico no válido!")
            return

        for user in users:
            if user["email"] == email:
                messagebox.showerror("Error", "¡El correo ya está registrado!")
                return

        users.append({"first_name": first_name, "last_name": last_name, "email": email, "password": password})
        save_users(users)
        messagebox.showinfo("Éxito", "¡Registro exitoso!")
        self.show_login_screen()

    def recover_password(self):
        email = self.entry_email_recover.get()
        users = load_users()

        for user in users:
            if user["email"] == email:
                messagebox.showinfo("Recuperación de contraseña", f"Tu contraseña es: {user['password']}")
                return

        messagebox.showerror("Error", "¡Correo no encontrado!")

class PlantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Plantas")
        self.root.attributes("-fullscreen", True)

        self.plants = cargar_plantas()

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
        self.frames["info_frame"] = tk.Frame(self.root, bg="#ADD8E6")
        
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
            volver_button = tk.Button(header, text="Volver", command=lambda: self.showi_frame(self.frames["default_frame"]), bg="#FFA500", fg="white", font=("Arial", 16), width=15, height=2)
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
        
        tk.Button(
    self.frames["default_frame"],
    text="Recomendaciones",
    bg="#829F4D",
    font=("Arial", 16),
    command=lambda: iniciar_cuestionario(self)  # Pasar la instancia actual
).pack(pady=10)

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






    def create_add_frame(self):
        self.image_path = None 

        self.create_navigation(self.add_frame, "Agregar Planta", self.showi_frame(self.frames["default_frame"]))

        canvas = tk.Canvas(self.add_frame, bg="#DECB76")
        scroll_frame = tk.Frame(canvas, bg="#DECB76")
        scrollbar = tk.Scrollbar(self.add_frame, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")

        def configure_scroll(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        scroll_frame.bind("<Configure>", configure_scroll)

        center_container = tk.Frame(scroll_frame, bg="#DECB76")
        center_container.pack(expand=True, anchor="c", fill="both") 


        center_container = tk.Frame(scroll_frame, bg="#DECB76")
        center_container.pack(expand=True, fill="both", anchor="center") 

        name_label = tk.Label(center_container, text="Nombre de la Planta:", font=("Arial", 14), bg="#DECB76")
        name_label.pack(pady=5, anchor="w", padx=10)
        name_entry = tk.Entry(center_container, font=("Arial", 14), bg="#E3DAC9")
        name_entry.pack(pady=5, fill="x", padx=10)

        tipo_label = tk.Label(center_container, text="Tipo (Verdura/Fruta):", font=("Arial", 14), bg="#DECB76")
        tipo_label.pack(pady=5, anchor="w", padx=10)
        tipo_var = tk.StringVar(value="Verdura")
        tipo_menu = tk.OptionMenu(center_container, tipo_var, "Verdura", "Fruta")
        tipo_menu.pack(pady=5, fill="x", padx=10)
        tipo_menu.config(bg="#E3DAC9")

        vendidos_label = tk.Label(center_container, text="Kilos Vendidos:", font=("Arial", 14), bg="#DECB76")
        vendidos_label.pack(pady=5, anchor="w", padx=10)
        vendidos_entry = tk.Entry(center_container, font=("Arial", 14), bg="#E3DAC9")
        vendidos_entry.pack(pady=5, fill="x", padx=10)

        comprados_label = tk.Label(center_container, text="Kilos Comprados:", font=("Arial", 14), bg="#DECB76")
        comprados_label.pack(pady=5, anchor="w", padx=10)
        comprados_entry = tk.Entry(center_container, font=("Arial", 14), bg="#E3DAC9")
        comprados_entry.pack(pady=5, fill="x", padx=10)

        frecuencia_label = tk.Label(center_container, text="Frecuencia de Compra:", font=("Arial", 14), bg="#DECB76")
        frecuencia_label.pack(pady=5, anchor="w", padx=10)
        frecuencia_var = tk.StringVar(value="Semanal")
        frecuencia_menu = tk.OptionMenu(center_container, frecuencia_var, "Semanal", "Mensual", "Anual")
        frecuencia_menu.pack(pady=5, fill="x", padx=10)
        frecuencia_menu.config(bg="#E3DAC9")

        estado_label = tk.Label(center_container, text="Estado Actual:", font=("Arial", 14), bg="#DECB76")
        estado_label.pack(pady=5, anchor="w", padx=10)
        estado_var = tk.StringVar(value="Activo")  
        estado_menu = tk.OptionMenu(center_container, estado_var, "Activo", "Inactivo", "En Mantenimiento")
        estado_menu.pack(pady=5, fill="x", padx=10)
        estado_menu.config(bg="#E3DAC9")

        fecha_label = tk.Label(center_container, text="Fecha de Registro (YYYY-MM-DD):", font=("Arial", 14), bg="#DECB76")
        fecha_label.pack(pady=5, anchor="w", padx=10)
        fecha_entry = tk.Entry(center_container, font=("Arial", 14), bg="#E3DAC9")
        fecha_entry.pack(pady=5, fill="x", padx=10)

        def seleccionar_imagen():
            self.image_path = filedialog.askopenfilename(title='Seleccionar imagen',
                                                        filetypes=[('Imágenes', '*.jpg *.jpeg *.png')])
            if self.image_path:
                img = Image.open(self.image_path)
                img = img.resize((200, 200))  
                photo = ImageTk.PhotoImage(img)
                self.image_label.config(image=photo)
                self.image_label.image = photo 

        imagen_button = tk.Button(center_container, text="Seleccionar Imagen", font=("Arial", 14),
                                command=seleccionar_imagen, bg="#E3DAC9")
        imagen_button.pack(pady=10, fill="x", padx=10)

        self.image_label = tk.Label(center_container, bg="#DECB76")
        self.image_label.pack(pady=10, fill="x", padx=10)


        def save_plant():
            name = name_entry.get()
            tipo = tipo_var.get()
            vendidos = vendidos_entry.get()
            comprados = comprados_entry.get()
            frecuencia = frecuencia_var.get()
            estado = estado_var.get()
            fecha = fecha_entry.get()

            if name and tipo and vendidos and comprados and frecuencia and estado and fecha and self.image_path:
                try:
                    kilos_vendidos = float(vendidos)  
                    kilos_comprados = float(comprados)  
                    planta ={
                        "name": name,
                        "type": tipo,
                        "sold": kilos_vendidos,
                        "bought": kilos_comprados,
                        "frequency": frecuencia,
                        "status": estado,
                        "date": fecha,
                        "image": self.image_path
                    }
                    self.plants.append(planta)
                    guardar_planta(planta)
                    messagebox.showinfo("Éxito", f"Planta '{name}' guardada correctamente")
                    name_entry.delete(0, tk.END)
                    vendidos_entry.delete(0, tk.END)
                    comprados_entry.delete(0, tk.END)
                    fecha_entry.delete(0, tk.END)
                    self.image_label.config(image=None)
                    self.image_label.image = None
                    self.image_path = None
                except ValueError:
                    messagebox.showwarning("Error", "Por favor ingresa valores numéricos válidos para los kilos")
            else:
                messagebox.showwarning("Error", "Por favor completa todos los campos e incluye una imagen")

        guardar_button = tk.Button(center_container, text="Guardar Planta", font=("Arial", 14), command=save_plant, bg="#E3DAC9")
        guardar_button.pack(pady=20, fill="x", padx=10)

        






    def show_plant_info(self, plant):
        self.create_navigation(self.info_frame, "Información de la Planta", self.list_frame)

        for widget in self.info_frame.winfo_children():
            widget.destroy()

        self.info_frame.configure(bg="#759CA6") 
        content_frame = tk.Frame(self.info_frame, bg="#D9D2C1", width=600, height=400) 
        content_frame.pack(expand=True, fill="both", padx=100, pady=100)
        content_frame.pack_propagate(False)

        tk.Button(self.info_frame, text="Atrás", font=("Arial", 14), bg="#FFD966",
                command=lambda: self.show_frame(self.list_frame)).place(x=20, y=20)
        tk.Button(self.info_frame, text="Menú principal", font=("Arial", 14), bg="#FFD966",
                command=lambda: self.showi_frame(self.frames["default_frame"])).place(x=1100, y=20)

        left_frame = tk.Frame(content_frame, bg="#D9D2C1")
        left_frame.pack(side="left", padx=20, pady=20)

        right_frame = tk.Frame(content_frame, bg="#D9D2C1")
        right_frame.pack(side="left", padx=20, pady=20, fill="both", expand=True)

        if plant.get('image'):
            from PIL import Image, ImageTk
            try:
                img = Image.open(plant['image'])
                img = img.resize((350, 350)) 
                photo = ImageTk.PhotoImage(img)
                image_label = tk.Label(left_frame, image=photo, bg="#D9D2C1")
                image_label.image = photo  
                image_label.pack()
            except Exception as e:
                tk.Label(left_frame, text="Error al cargar la imagen.", font=("Arial", 12), fg="red", bg="#D9D2C1").pack()
        else:
            tk.Label(left_frame, text="Sin imagen", font=("Arial", 12), bg="#D9D2C1").pack()

        tk.Label(right_frame, text=plant['name'], font=("Arial", 20, "bold"), bg="#D9D2C1").pack(pady=(40, 10))
        details = [
            f"Tipo de Producto: {plant.get('type', 'Desconocido')}",
            f"Kilos Comprados: {plant.get('bought', '0')}",
            f"Kilos Vendidos: {plant.get('sold', '0')}",
            f"Frecuencia de Compra: {plant.get('frequency', 'No definida')}",
            f"Estado Actual: {plant.get('status', 'No definido')}",
            f"Fecha de Registro: {plant.get('date', 'No registrada')}",
        ]
        for detail in details:
            tk.Label(right_frame, text=detail, font=("Arial", 14), bg="#D9D2C1", anchor="w", justify="center").pack(pady=5)

        right_frame.pack_propagate(False)
        spacer = tk.Frame(right_frame, bg="#D9D2C1")
        spacer.pack(expand=True, fill="y")

        self.show_frame(self.info_frame)




    def create_reco_frame(self):
        """Crear el marco de recomendaciones con un contenedor centrado."""
        # Frame base
        frame = self.frames["reco_frame"]
        
        # Crear navegación
        self.create_navigation(self.frames["reco_frame"], "Recomendaciones", self.frames["default_frame"])


        # Evitar duplicados: eliminar widgets si ya existen
        for widget in self.frames["reco_frame"].winfo_children():
            widget.destroy()

        # Contenedor principal
        reco_container = tk.Frame(self.frames["reco_frame"], bg="#E3DAC9")
        reco_container.pack(fill="both", expand=True)

        # Subcontenedor blanco
        reco_co_container = tk.Frame(reco_container, bg="white", width=700, height=400)  
        reco_co_container.place(relx=0.5, rely=0.5, anchor="center")  

        # Contenedor centrado
        centered_container = tk.Frame(reco_co_container, bg="white", width=400, height=200)  
        centered_container.place(relx=0.5, rely=0.5, anchor="center")  

        # Botón para iniciar formulario
        tk.Button(
            centered_container,
            text="Iniciar formulario",
            bg="#DECB76",
            font=("Arial", 14),
            command=lambda: self.showi_frame(self.frames["clima_frame"])
        ).pack(pady=20)

        # Mensaje de instrucciones
        tk.Label(
            centered_container,
            text="Tendrá que llenar el siguiente formulario con los datos solicitados.",
            bg="white",
            font=("Arial", 12),
            wraplength=300,
            justify="center"
        ).pack(pady=20)

    
    def create_clima_frame(self):
        """Pantalla para elegir el clima."""
        frame = self.frames["clima_frame"]

        tk.Label(
            frame,
            text="Selecciona el clima preferido:",
            bg="#829F4D",
            font=("Arial", 14),
            fg="white"
        ).pack(pady=20)

        self.clima_var = tk.StringVar(value="")  # Guardar selección

        options = ["Cálido", "Templado", "Frío"]
        for option in options:
            tk.Radiobutton(
                frame,
                text=option,
                variable=self.clima_var,
                value=option,
                bg="#829F4D",
                font=("Arial", 12),
                fg="white",
                anchor="w"
            ).pack(anchor="w", padx=20, pady=5)

        # Botones
        button_frame = tk.Frame(frame, bg="#829F4D")
        button_frame.pack(pady=20)

        tk.Button(
            button_frame,
            text="Guardar",
            bg="#A4C639",
            font=("Arial", 12),
            command=lambda: print(f"Clima seleccionado: {self.clima_var.get()}")
        ).pack(side="left", padx=10)

        tk.Button(
            button_frame,
            text="Siguiente",
            bg="#DECB76",
            font=("Arial", 12),
            command=lambda: self.showi_frame(self.frames["tempo_frame"])
        ).pack(side="left", padx=10)

    def create_tempo_frame(self):
        """Pantalla para elegir la temporada del año."""
        frame = self.frames["tempo_frame"]

        tk.Label(
            frame,
            text="Selecciona la temporada del año:",
            bg="#FFDAB9",
            font=("Arial", 14),
        ).pack(pady=20)

        self.tempo_var = tk.StringVar(value="")  # Guardar selección

        options = ["Primavera", "Verano", "Otoño", "Invierno"]
        for option in options:
            tk.Radiobutton(
                frame,
                text=option,
                variable=self.tempo_var,
                value=option,
                bg="#FFDAB9",
                font=("Arial", 12),
                anchor="w"
            ).pack(anchor="w", padx=20, pady=5)

        # Botones
        button_frame = tk.Frame(frame, bg="#FFDAB9")
        button_frame.pack(pady=20)

        tk.Button(
            button_frame,
            text="Guardar",
            bg="#A4C639",
            font=("Arial", 12),
            command=lambda: print(f"Temporada seleccionada: {self.tempo_var.get()}")
        ).pack(side="left", padx=10)

        tk.Button(
            button_frame,
            text="Siguiente",
            bg="#DECB76",
            font=("Arial", 12),
            command=lambda: self.showi_frame(self.frames["type_frame"])
        ).pack(side="left", padx=10)

    def create_type_frame(self):
        """Pantalla para elegir entre fruta o verdura."""
        frame = self.frames["type_frame"]

        tk.Label(
            frame,
            text="¿Qué prefieres?",
            bg="#D8BFD8",
            font=("Arial", 14),
        ).pack(pady=20)

        self.type_var = tk.StringVar(value="")  # Guardar selección

        options = ["Fruta", "Verdura"]
        for option in options:
            tk.Radiobutton(
                frame,
                text=option,
                variable=self.type_var,
                value=option,
                bg="#D8BFD8",
                font=("Arial", 12),
                anchor="w"
            ).pack(anchor="w", padx=20, pady=5)

        # Botones
        button_frame = tk.Frame(frame, bg="#D8BFD8")
        button_frame.pack(pady=20)

        tk.Button(
            button_frame,
            text="Guardar",
            bg="#A4C639",
            font=("Arial", 12),
            command=lambda: print(f"Tipo seleccionado: {self.type_var.get()}")
        ).pack(side="left", padx=10)

        tk.Button(
            button_frame,
            text="Siguiente",
            bg="#DECB76",
            font=("Arial", 12),
            command=lambda: self.showi_frame(self.frames["space_frame"])
        ).pack(side="left", padx=10)

    def create_space_frame(self):
        """Pantalla para cantidad de plantas y espacio disponible."""
        frame = self.frames["space_frame"]

        tk.Label(
            frame,
            text="Ingresa la cantidad de plantas y espacio disponible:",
            bg="#F5DEB3",
            font=("Arial", 14),
        ).pack(pady=20)

        self.cantidad_var = tk.IntVar(value=1)
        self.espacio_var = tk.DoubleVar(value=0.0)

        tk.Label(frame, text="Cantidad de plantas:", bg="#F5DEB3").pack(pady=5)
        tk.Entry(frame, textvariable=self.cantidad_var).pack(pady=5)

        tk.Label(frame, text="Espacio disponible (m²):", bg="#F5DEB3").pack(pady=5)
        tk.Entry(frame, textvariable=self.espacio_var).pack(pady=5)

        # Botones
        button_frame = tk.Frame(frame, bg="#F5DEB3")
        button_frame.pack(pady=20)

        tk.Button(
            button_frame,
            text="Guardar",
            bg="#A4C639",
            font=("Arial", 12),
            command=lambda: print(
                f"Cantidad: {self.cantidad_var.get()}, Espacio: {self.espacio_var.get()} m²"
            )
        ).pack(side="left", padx=10)

        tk.Button(
            button_frame,
            text="Siguiente",
            bg="#DECB76",
            font=("Arial", 12),
            command=lambda: self.showi_frame(self.frames["final_frame"])
        ).pack(side="left", padx=10)



    def create_final_frame(self):
        """Pantalla final con recomendaciones de plantas en tarjetas con desplazamiento."""
        frame = self.frames["final_frame"]

        # Limpiar el frame antes de agregar contenido
        for widget in frame.winfo_children():
            widget.destroy()

        tk.Label(
            frame,
            text="Basándonos en tus respuestas, estas son nuestras recomendaciones:",
            bg="#ADD8E6",
            font=("Arial", 14),
            wraplength=400,
            justify="center"
        ).pack(pady=10)

        # Frame contenedor para Canvas y Scrollbar
        container = tk.Frame(frame, bg="#ADD8E6")
        container.pack(fill="both", expand=True)

        # Canvas para las tarjetas
        canvas = tk.Canvas(container, bg="#ADD8E6")
        canvas.pack(side="left", fill="both", expand=True)

        # Barra de desplazamiento
        scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        # Configuración del Canvas con la Scrollbar
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        # Frame interno para colocar las tarjetas
        cards_frame = tk.Frame(canvas, bg="#ADD8E6")
        canvas.create_window((0, 0), window=cards_frame, anchor="nw")

        # Definimos las plantas como lista de diccionarios
        plantas = [
            {
            "nombre": "Rábanos",
            "tipo": "Verdura",
            "clima": "Templado",
            "estacion": "Primavera y otoño",
            "espacio": "Muy poco",
            "tiempo": "Rápido"
            },
            {
            "nombre": "Lechuga",
            "tipo": "Verdura",
            "clima": "Fresco",
            "estacion": "Primavera",
            "espacio": "Poco",
            "tiempo": "Rápido"
            },
            {
            "nombre": "Espinaca",
            "tipo": "Verdura",
            "clima": "Frío o templado",
            "estacion": "Otoño",
            "espacio": "Poco",
            "tiempo": "Rápido"
            },
            {
            "nombre": "Fresas",
            "tipo": "Fruta",
            "clima": "Templado",
            "estacion": "Primavera y verano",
            "espacio": "Poco",
            "tiempo": "Medio"
            },
            {
            "nombre": "Tomates cherry",
            "tipo": "Fruta",
            "clima": "Cálido",
            "estacion": "Primavera y verano",
            "espacio": "Poco",
            "tiempo": "Medio"
            },
            {
            "nombre": "Zanahorias",
            "tipo": "Verdura",
            "clima": "Templado",
            "estacion": "Primavera y otoño",
            "espacio": "Moderado",
            "tiempo": "Medio"
            },
            {
            "nombre": "Pimientos",
            "tipo": "Fruta",
            "clima": "Cálido",
            "estacion": "Primavera y verano",
            "espacio": "Moderado",
            "tiempo": "Medio"
            },
            {
            "nombre": "Cebollín",
            "tipo": "Verdura",
            "clima": "Templado o cálido",
            "estacion": "Todo el año",
            "espacio": "Muy poco",
            "tiempo": "Rápido"
            },
            {
            "nombre": "Albahaca",
            "tipo": "Verdura",
            "clima": "Cálido",
            "estacion": "Primavera y verano",
            "espacio": "Muy poco",
            "tiempo": "Rápido"
            },
            {
            "nombre": "Pepinos",
            "tipo": "Verdura",
            "clima": "Cálido",
            "estacion": "Primavera y verano",
            "espacio": "Poco",
            "tiempo": "Medio"
            },
            {
            "nombre": "Remolacha",
            "tipo": "Verdura",
            "clima": "Fresco o templado",
            "estacion": "Primavera y otoño",
            "espacio": "Moderado",
            "tiempo": "Medio"
            },
            {
            "nombre": "Acelga",
            "tipo": "Verdura",
            "clima": "Templado",
            "estacion": "Todo el año",
            "espacio": "Poco",
            "tiempo": "Rápido"
            },
            {
            "nombre": "Cilantro",
            "tipo": "Verdura",
            "clima": "Templado",
            "estacion": "Primavera y otoño",
            "espacio": "Muy poco",
            "tiempo": "Rápido"
            },
            {
            "nombre": "Frijoles enanos",
            "tipo": "Verdura",
            "clima": "Cálido",
            "estacion": "Primavera y verano",
            "espacio": "Moderado",
            "tiempo": "Medio"
            },
            {
            "nombre": "Limón enano",
            "tipo": "Fruta",
            "clima": "Cálido",
            "estacion": "Todo el año",
            "espacio": "Moderado",
            "tiempo": "Lento"
            }
            # Agregar más plantas aquí...
        ]

        # Crear las tarjetas en dos columnas
        for i, planta in enumerate(plantas):
            column = i % 2  # Columna (0 o 1)
            row = i // 2  # Fila

            # Marco individual para cada tarjeta
            card_frame = tk.Frame(
                cards_frame,
                bg="#FFFDD0",
                bd=2,
                relief="groove",
                width=300, 
                height=200,  
                padx=10,
                pady=10
            )
            card_frame.grid(row=row, column=column, padx=10, pady=10, sticky="n")

            # Contenido de la tarjeta
            tk.Label(
                card_frame,
                text=planta["nombre"],
                font=("Arial", 12, "bold"),
                bg="#FFFDD0"
            ).pack(anchor="w")

            tk.Label(
                card_frame,
                text=f"• Tipo: {planta['tipo']}",
                font=("Arial", 10),
                bg="#FFFDD0",
                justify="left"
            ).pack(anchor="w")

            tk.Label(
                card_frame,
                text=f"• Clima: {planta['clima']}",
                font=("Arial", 10),
                bg="#FFFDD0",
                justify="left"
            ).pack(anchor="w")

            tk.Label(
                card_frame,
                text=f"• Estación: {planta['estacion']}",
                font=("Arial", 10),
                bg="#FFFDD0",
                justify="left"
            ).pack(anchor="w")

            tk.Label(
                card_frame,
                text=f"• Espacio: {planta['espacio']}",
                font=("Arial", 10),
                bg="#FFFDD0",
                justify="left"
            ).pack(anchor="w")

            tk.Label(
                card_frame,
                text=f"• Tiempo: {planta['tiempo']}",
                font=("Arial", 10),
                bg="#FFFDD0",
                justify="left"
            ).pack(anchor="w")

        tk.Button(
            frame,
            text="Volver al inicio",
            bg="#DECB76",
            font=("Arial", 14),
            command=lambda: self.show_frame(self.frames["default_frame"])
        ).pack(pady=20)

def iniciar_cuestionario(app):
    """Configura el frame de recomendaciones con preguntas del cuestionario."""
    app.show_frame(app.frames["reco_frame"])  # Mostrar el frame de recomendaciones

    # Limpiar el frame antes de agregar contenido
    for widget in app.frames["reco_frame"].winfo_children():
        widget.destroy()

    # Preguntas del cuestionario
    tk.Label(app.frames["reco_frame"], text="Responde el cuestionario para recibir recomendaciones",
            bg="#E3DAC9", font=("Arial", 20, "bold")).pack(pady=20)

    tipo_var = tk.StringVar(value="Verdura")
    clima_var = tk.StringVar(value="Templado")
    espacio_var = tk.StringVar(value="Pequeño")
    estacion_var = tk.StringVar(value="Primavera")

    # Pregunta 1: Tipo de planta
    tk.Label(app.frames["reco_frame"], text="¿Qué tipo de planta prefieres?", font=("Arial", 16), bg="#E3DAC9").pack(pady=5)
    tk.OptionMenu(app.frames["reco_frame"], tipo_var, "Verdura", "Fruta").pack(pady=5)

    # Pregunta 2: Clima
    tk.Label(app.frames["reco_frame"], text="¿En qué clima se encuentra?", font=("Arial", 16), bg="#E3DAC9").pack(pady=5)
    tk.OptionMenu(app.frames["reco_frame"], clima_var, "Templado", "Tropical", "Árido", "Fresco").pack(pady=5)


    # Pregunta 3: Espacio disponible
    tk.Label(app.frames["reco_frame"], text="¿Cuánto espacio tienes disponible?", font=("Arial", 16), bg="#E3DAC9").pack(pady=5)
    tk.OptionMenu(app.frames["reco_frame"], espacio_var, "Pequeño", "Mediano", "Grande").pack(pady=5)

    # Pregunta 4: Estación del año
    tk.Label(app.frames["reco_frame"], text="¿En qué estación del año estás?", font=("Arial", 16), bg="#E3DAC9").pack(pady=5)
    tk.OptionMenu(app.frames["reco_frame"], estacion_var, "Primavera", "Verano", "Otoño", "Invierno").pack(pady=5)

    # Base de datos de plantas
    plantas = [
        {
            "nombre": "Rábanos",
            "tipo": "Verdura",
            "clima": "Templado",
            "espacio": "Pequeño",
            "estacion": "Primavera",
            "descripcion": """El rábano es una hortaliza de raíz conocida por su crecimiento ultrarrápido y su capacidad para prosperar en pequeños espacios. Se cosecha en tan solo 25 a 30 días. Los rábanos prefieren un suelo suelto, ligero y bien drenado, con un pH ligeramente ácido (6.0-7.0). Es ideal sembrarlos directamente en el lugar definitivo porque no les gusta el trasplante.
•Luz: Requieren 4-6 horas de luz solar directa diaria.
•Riego: El suelo debe mantenerse constantemente húmedo, pero sin encharcar. La falta de agua puede hacer que las raíces sean pequeñas o picantes.
•Beneficios: Además de ser una opción rápida y económica, los rábanos son ricos en fibra y vitamina C.
•Problemas comunes: Si no se cosechan a tiempo, pueden volverse leñosos o amargos."""
        },
        {
        "nombre": "Lechuga",
        "tipo": "Verdura",
        "clima": "Fresco",
        "espacio": "Pequeño",
        "estacion": "Primavera",
        "descripcion": """La lechuga es un cultivo versátil que se adapta muy bien a macetas o jardineras. Es perfecta para climas frescos...
• Luz: Necesita entre 3-5 horas de luz directa o luz filtrada en climas cálidos.
• Riego: Riego frecuente, preferiblemente por la mañana, manteniendo el suelo húmedo pero no empapado..."""
    },
        {
        "nombre": "Espinaca",
        "tipo": "Verdura",
        "clima": "Fresco",
        "espacio": "Pequeño",
        "estacion": "Otoño",
        "descripcion": "Esta planta de hojas verdes prefiere climas frescos y suele sembrarse a finales del verano o principios de otoño para cosechas continuas en invierno. La espinaca es rica en hierro y antioxidantes, siendo una opción muy nutritiva para el huerto.\n•Luz: Necesita 4-6 horas de luz solar directa, pero tolera sombra parcial.\n•Riego: Requiere riego constante para mantener el suelo húmedo. La falta de agua puede provocar que florezca antes de tiempo.\n•Suelo: Prefiere suelos arcillosos, bien drenados y con alto contenido de materia orgánica, con un pH entre 6.5 y 7.0.\n•Problemas comunes: Las altas temperaturas pueden provocar que las plantas espiguen y dejen de producir hojas comestibles."
    },
    {
        "nombre": "Fresas",
        "tipo": "Fruta",
        "clima": "Cálido",
        "espacio": "Pequeño",
        "estacion": "Primavera",
        "descripcion": "Las fresas son ideales para espacios reducidos y se adaptan a macetas colgantes o jardineras profundas. Producen frutos dulces y jugosos durante la primavera y el verano.\n•Luz: Necesitan al menos 6-8 horas de luz solar directa al día.\n•Riego: Riego moderado; el suelo debe estar húmedo pero bien drenado. La acumulación de agua puede pudrir las raíces.\n•Suelo: Prefieren un suelo ácido con un pH de 5.5-6.5. Se recomienda usar sustrato específico para fresas o añadir materia orgánica.\n•Problemas comunes: Las plagas, como los pulgones, y enfermedades fúngicas pueden ser un problema en condiciones de alta humedad."
    },
        
        # Agregar más plantas aquí...
    ]
    # Botón para volver al menú principal
    # Botón para volver al menú principal
    tk.Button(app.frames["reco_frame"], text="Volver", bg="#FFD966", font=("Arial", 14),
        command=lambda: app.show_frame(app.frames["default_frame"])).pack(side="left", padx=20, pady=20)

# Botón para salir de la aplicación
    tk.Button(app.frames["reco_frame"], text="Salir", bg="red", font=("Arial", 14),
        command=app.root.destroy).pack(side="right", padx=20, pady=20)


    def recomendar():
        """Filtrar y mostrar recomendaciones según las respuestas."""
        recomendaciones = [
            planta for planta in plantas
            if planta["tipo"] == tipo_var.get() and
            planta["clima"] == clima_var.get() and
            planta["espacio"] == espacio_var.get() and
            planta["estacion"] == estacion_var.get()
        ]

        # Frame para resultados
        for widget in resultados_frame.winfo_children():
            widget.destroy()

        if recomendaciones:
            tk.Label(resultados_frame, text="Plantas recomendadas:", font=("Arial", 16), bg="#E3DAC9").pack(pady=10)
            for planta in recomendaciones:
                tk.Button(resultados_frame, text=planta["nombre"], bg="#E3DAC9", font=("Arial", 14),
                        command=lambda p=planta: mostrar_info_planta(p)).pack(pady=5)
        else:
            tk.Label(resultados_frame, text="No hay plantas que coincidan con las preferencias seleccionadas.",
                    font=("Arial", 14), bg="#E3DAC9").pack(pady=10)

    # Mostrar la información de una planta en otro frame
    def mostrar_info_planta(planta):
        app.show_frame(app.frames["info_frame"])

        for widget in app.frames["info_frame"].winfo_children():
            widget.destroy()

        tk.Label(app.frames["info_frame"], text=planta["nombre"], font=("Arial", 20, "bold"),
                bg="#ADD8E6").pack(pady=20)
        tk.Label(app.frames["info_frame"], text=planta["descripcion"], font=("Arial", 14),
                bg="#ADD8E6", justify="left", wraplength=800).pack(pady=10)

        # Botones para volver y salir
        tk.Button(app.frames["info_frame"], text="Volver", bg="#FFD966", font=("Arial", 14),
                command=lambda: app.show_frame(app.frames["reco_frame"])).pack(side="left", padx=20, pady=20)
        tk.Button(app.frames["info_frame"], text="Salir", bg="red", font=("Arial", 14),
                command=app.root.destroy).pack(side="right", padx=20, pady=20)

    # Botón para generar recomendaciones
    tk.Button(app.frames["reco_frame"], text="Recomendar", bg="#829F4D", font=("Arial", 16),
            command=recomendar).pack(pady=20)

    # Frame para resultados
    resultados_frame = tk.Frame(app.frames["reco_frame"], bg="#E3DAC9")
    resultados_frame.pack(pady=10, fill="both", expand=True)
    





if __name__ == "__main__":
    root = tk.Tk()
    login_window = Login(root)  # Inicia la clase Login
    root.mainloop()