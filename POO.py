class Usuario:
    def __init__(self,nombre,email,contraseña):
        self.nombre = nombre
        self.email = email
        self._contraseña = contraseña

    def iniciar_sesion(self,email,contraseña):
        if self.email == email and self._contraseña == contraseña:
            print(f"Bienvenido {self.nombre}")
        else:
            print("Email o contraseña incorrectas.")


    def cambiar_contraseña(self,nueva_contraseña):
        print("la contraseña debe tener al menos 8 caracteres")
        if len(nueva_contraseña) >= 8:
            self._contraseña = nueva_contraseña
            print("Contraseña cambiada con exito")
        else:
            print("la contraseña debe tener al menos 8 caracteres")

    def __str__(self):
        return f"Usuario(nombre={self.nombre}, email={self.email})"



class UsuarioPremium(Usuario):
    def __init__(self,nombre,email,contraseña,plan):
        super().__init__(nombre,email,contraseña)
        self.plan = plan

    def iniciar_sesion(self,email,contraseña):
        if self.email == email and self._contraseña == contraseña:
            print(f"Bienvenido {self.nombre}, tu plan es {self.plan}")
        else:
            print("Email o contraseña incorrectas.")
    

class UsuarioBasico(Usuario):
    def __init__(self,nombre,email):
        super().__init__(nombre,email)

    def iniciar_sesion_sin_password(self, nombre,email):
        if self.nombre == nombre and self.email == email:
            print(f"Bienvenido {self.nombre}, no es necesario contraseña para iniciar sesion en cuenta basica.")

    def cambio_email(self,nuevo_email):
        self.email = nuevo_email
        print(f"Email cambiado a {self.email}")
        




usuario1 = Usuario("juan cruz", "juancruz@gmail.com", "olamanola123")

print(usuario1)  # Imprime la representación del objeto Usuario

usuario1.iniciar_sesion("juancruz@gmail.com", "olamanola123")

user_premium1 = UsuarioPremium("leandro", "leandro@gmail.com", "leandro123", "premium")

print(user_premium1)  # Imprime la representación del objeto UsuarioPremium

user_premium1.iniciar_sesion("leandro@gmail.com", "leandro123")

