import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class TamagotchiPixelArt:
    def __init__(self, root):
        self.root = root
        self.root.title("Tamagotchi Pixel Art")
        self.root.geometry("400x600")
        
        # Variables de la mascota
        self.nombre = ""
        self.hambre = 50
        self.felicidad = 50
        self.energia = 100
        self.salud = 100
        self.edad = 0
        self.esta_vivo = True
        self.ultima_actualizacion = datetime.now()
        
        # Canvas para el pixel art
        self.canvas = tk.Canvas(root, width=200, height=200, bg='white')
        self.canvas.pack(pady=20)
        
        # Crear interfaz
        self.crear_widgets()
        
        # Estado actual de la animación
        self.estado_actual = "normal"
        self.dibujar_mascota("normal")
        
        # Actualizar estados cada segundo
        self.root.after(1000, self.actualizar_estados)
        
    def dibujar_mascota(self, estado):
        self.canvas.delete("all")  # Limpiar canvas
        
        if not self.nombre:  # Si aún no se inicia el juego
            return
            
        # Colores base
        color_principal = "#FFB6C1"  # Rosa claro
        color_secundario = "#FF69B4"  # Rosa más oscuro
        
        if estado == "normal":
            # Cuerpo base (forma de huevo)
            self.canvas.create_oval(50, 50, 150, 170, fill=color_principal, outline=color_secundario, width=2)
            
            # Ojos
            self.canvas.create_oval(80, 90, 95, 105, fill="black")
            self.canvas.create_oval(105, 90, 120, 105, fill="black")
            
            # Brillo en los ojos
            self.canvas.create_oval(83, 93, 87, 97, fill="white")
            self.canvas.create_oval(108, 93, 112, 97, fill="white")
            
            # Boca feliz
            self.canvas.create_arc(85, 110, 115, 130, start=0, extent=-180, fill=color_secundario)
            
        elif estado == "comiendo":
            # Cuerpo base
            self.canvas.create_oval(50, 50, 150, 170, fill=color_principal, outline=color_secundario, width=2)
            
            # Ojos contentos (cerrados)
            self.canvas.create_arc(80, 90, 95, 105, start=0, extent=-180, fill="black")
            self.canvas.create_arc(105, 90, 120, 105, start=0, extent=-180, fill="black")
            
            # Boca comiendo
            self.canvas.create_oval(85, 110, 115, 140, fill=color_secundario)
            
        elif estado == "durmiendo":
            # Cuerpo base
            self.canvas.create_oval(50, 50, 150, 170, fill=color_principal, outline=color_secundario, width=2)
            
            # Ojos dormidos (Z's)
            self.canvas.create_text(130, 70, text="Z", font=("Arial", 20), fill=color_secundario)
            self.canvas.create_text(140, 85, text="Z", font=("Arial", 15), fill=color_secundario)
            self.canvas.create_text(150, 100, text="Z", font=("Arial", 10), fill=color_secundario)
            
            # Boca durmiendo
            self.canvas.create_arc(85, 120, 115, 130, start=0, extent=180, fill=color_secundario)
            
        elif estado == "jugando":
            # Cuerpo base saltando
            self.canvas.create_oval(50, 40, 150, 160, fill=color_principal, outline=color_secundario, width=2)
            
            # Ojos emocionados
            self.canvas.create_oval(80, 80, 95, 95, fill="black")
            self.canvas.create_oval(105, 80, 120, 95, fill="black")
            
            # Brillo en los ojos
            self.canvas.create_oval(83, 83, 87, 87, fill="white")
            self.canvas.create_oval(108, 83, 112, 87, fill="white")
            
            # Boca muy feliz
            self.canvas.create_arc(85, 100, 115, 130, start=0, extent=-180, fill=color_secundario)
            
        elif estado == "triste":
            # Cuerpo base
            self.canvas.create_oval(50, 50, 150, 170, fill=color_principal, outline=color_secundario, width=2)
            
            # Ojos tristes
            self.canvas.create_oval(80, 90, 95, 105, fill="black")
            self.canvas.create_oval(105, 90, 120, 105, fill="black")
            
            # Boca triste
            self.canvas.create_arc(85, 120, 115, 140, start=0, extent=180, fill=color_secundario)

    def crear_widgets(self):
        # Frame principal
        self.frame_principal = tk.Frame(self.root, padx=20, pady=20)
        self.frame_principal.pack(expand=True, fill='both')
        
        # Entrada del nombre
        self.label_nombre = tk.Label(self.frame_principal, text="Nombre de tu mascota:")
        self.label_nombre.pack()
        self.entry_nombre = tk.Entry(self.frame_principal)
        self.entry_nombre.pack()
        self.btn_empezar = tk.Button(self.frame_principal, text="¡Comenzar!", command=self.iniciar_juego)
        self.btn_empezar.pack(pady=10)
        
        # Estados (inicialmente ocultos)
        self.frame_estados = tk.Frame(self.frame_principal)
        self.labels_estados = {}
        for estado in ['Nombre', 'Edad', 'Salud', 'Hambre', 'Felicidad', 'Energía']:
            lbl = tk.Label(self.frame_estados, text=f"{estado}: 0")
            lbl.pack(pady=5)
            self.labels_estados[estado.lower()] = lbl
        
        # Botones de acción
        self.frame_botones = tk.Frame(self.frame_principal)
        tk.Button(self.frame_botones, text="Alimentar", command=self.alimentar).pack(side=tk.LEFT, padx=5)
        tk.Button(self.frame_botones, text="Jugar", command=self.jugar).pack(side=tk.LEFT, padx=5)
        tk.Button(self.frame_botones, text="Dormir", command=self.dormir).pack(side=tk.LEFT, padx=5)
    
    def iniciar_juego(self):
        if not self.entry_nombre.get():
            messagebox.showwarning("Error", "¡Por favor ingresa un nombre!")
            return
            
        self.nombre = self.entry_nombre.get()
        self.label_nombre.destroy()
        self.entry_nombre.destroy()
        self.btn_empezar.destroy()
        
        self.frame_estados.pack(pady=20)
        self.frame_botones.pack(pady=20)
        self.actualizar_display()
        messagebox.showinfo("¡Bienvenido!", f"¡{self.nombre} ha nacido! Cuídalo bien.")
        self.dibujar_mascota("normal")
    
    def actualizar_estados(self):
        if not self.esta_vivo or not self.nombre:
            return
            
        tiempo_actual = datetime.now()
        tiempo_pasado = (tiempo_actual - self.ultima_actualizacion).total_seconds()
        
        if tiempo_pasado >= 60:
            minutos = int(tiempo_pasado / 60)
            self.hambre = min(100, self.hambre + minutos * 2)
            self.felicidad = max(0, self.felicidad - minutos)
            self.energia = max(0, self.energia - minutos)
            self.edad += minutos // 10
            
            if self.hambre >= 100 or self.felicidad <= 0 or self.energia <= 0:
                self.salud = max(0, self.salud - 5)
                self.dibujar_mascota("triste")
            else:
                self.dibujar_mascota("normal")
            
            if self.salud <= 0:
                self.esta_vivo = False
                messagebox.showwarning("😢", f"{self.nombre} ha fallecido...")
                return
            
            self.ultima_actualizacion = tiempo_actual
            self.actualizar_display()
        
        self.root.after(1000, self.actualizar_estados)
    
    def actualizar_display(self):
        estados = {
            'nombre': f"Nombre: {self.nombre}",
            'edad': f"Edad: {self.edad} días",
            'salud': f"Salud: {self.salud}%",
            'hambre': f"Hambre: {self.hambre}%",
            'felicidad': f"Felicidad: {self.felicidad}%",
            'energía': f"Energía: {self.energia}%"
        }
        for estado, texto in estados.items():
            self.labels_estados[estado].config(text=texto)
    
    def alimentar(self):
        if self.hambre < 20:
            messagebox.showinfo("🍎", f"¡{self.nombre} no tiene hambre!")
            return
        self.hambre = max(0, self.hambre - 30)
        self.felicidad = min(100, self.felicidad + 10)
        self.dibujar_mascota("comiendo")
        self.root.after(2000, lambda: self.dibujar_mascota("normal"))
        self.actualizar_display()
        messagebox.showinfo("🍎", f"¡Has alimentado a {self.nombre}!")
    
    def jugar(self):
        if self.energia < 20:
            messagebox.showinfo("🎾", f"¡{self.nombre} está muy cansado para jugar!")
            return
        self.felicidad = min(100, self.felicidad + 20)
        self.energia = max(0, self.energia - 20)
        self.hambre = min(100, self.hambre + 10)
        self.dibujar_mascota("jugando")
        self.root.after(2000, lambda: self.dibujar_mascota("normal"))
        self.actualizar_display()
        messagebox.showinfo("🎾", f"¡Has jugado con {self.nombre}!")
    
    def dormir(self):
        if self.energia > 80:
            messagebox.showinfo("😴", f"¡{self.nombre} no está cansado!")
            return
        self.energia = 100
        self.hambre = min(100, self.hambre + 20)
        self.dibujar_mascota("durmiendo")
        self.root.after(2000, lambda: self.dibujar_mascota("normal"))
        self.actualizar_display()
        messagebox.showinfo("😴", f"¡{self.nombre} ha descansado bien!")

if __name__ == "__main__":
    root = tk.Tk()
    app = TamagotchiPixelArt(root)
    root.mainloop()