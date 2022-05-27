import time
from traceback import print_tb
from xml.etree.ElementTree import Element

class registroCliente:
    def __init__(self, nombre, usuario, telefono, nCedula, contra, estado):
        self.nombre=nombre
        self.usuario=usuario
        self.telefono=telefono
        self.nCedula=nCedula
        self.contra=contra
        self.estado=estado

    def registrarse(self, nombre, usuario, contra):
        nombre=str(input("Registre su nombre o apellido: " ))
        usuario=str(input("Cree un Usuario: " ))
        self.usuario=usuario
        contra=str(input("Cree una contrasena: " ))
        print("Registro completo, a continuacion sus datos")
        self.contra=contra
        lClientes.append(nombre)

    def iniciarSesion(self, usuario, contra):
        usuario=str(input("Usuario: "))
        contra=str(input("Contrasena: "))
        while self.usuario==usuario and self.contra==contra:
            print("Acceso concedido: ", nombre)
            break
    
    def registrarseTienda(self, nCedula, telefono):
        self.telefono=telefono
        self.nCedula=nCedula
        nCedula=str(input("Ingrese su num de cedula: "))
        telefono=str(input("ingrese su num celular: "))
        ltelefono.append(telefono)
        print("registro completo, gracias")

    def estadoCliente(self, estado):
        print("Para Estado tiene 3 opciones:")
        print("normal: Usted esta' libre de covid")
        print("cercano: Ha estado en contacto con un infectado")
        print("caso: Usted tiene covid-19")

        estado=str(input("Ingrese en que estado se encuentra: "))
        if estado=="normal":
            print("Estado registrado: ")
            lestado.append(estado)
        elif estado=="cercano":
            print("Estado registrado: ")
            lestado.append(estado)
        elif estado=="caso":
            print("Estado registrado: ")
            lestado.append(estado)
        else:
         print("No esta' entre las opciones lo que acaba de ingresar.")


class registroTienda:
    def __init__(self, nombreTienda, telefonoTienda, estadoTienda, gerente):
        self.nombreTienda=nombreTienda
        self.telefonoTienda=telefonoTienda
        self.estadoTienda=estadoTienda
        self.gerente=gerente

nombre=str
usuario=str
telefono=str
nCedula=str
contra=str
estado=str
cliente1=registroCliente(nombre, usuario, telefono, nCedula, contra, estado)

lClientes= []
lTienda=[]
lHora=[]
lfecha=[]
lGerente=[]
ltelefono=[]
ltelefonoT=[]
lestado=[]
lestadoT=[]

menuPrincipal=int(input(" \n=============================== \n Menu Principal: \n=============================== \n 1-Cliente \n 2-Admin \n 3-Salir \n=============================== \n Por favor, ingrese una opcion: "))
while menuPrincipal != 3:
    
    if menuPrincipal ==1:
            subMenuClientes=int(input("\n=============================== \n Sub Menu Clientes: \n=============================== \n 1-Registrarse \n 2-Ingresar sesion \n 3-Regresar \n=============================== \n Ingrese una opcion: "))
            while subMenuClientes != 3:
                if subMenuClientes ==1:
                     print("\n=============================== \n REGISTRARSE \n===============================")
                     cliente1.registrarse(nombre, usuario, contra)

                elif subMenuClientes ==2:
                     print("------------------------------------------------------------")
                     print(" PARA INICIAR SESION, POR FAVOR LLENE LOS SIGUIENTES CAMPOS: ")
                     print("------------------------------------------------------------")
                     cliente1.iniciarSesion(usuario, contra)
                     subMenuClientes2=int(input("\n=============================== \n Sub Menu Clientes 2: \n===============================  \n 1-Registrarse en tienda \n 2- Historial \n 3-Estado \n 4-Regresar \n Ingrese una opcion: "))
                     while subMenuClientes2 != 4:
                            if subMenuClientes2 ==1:
                                estadoTienda="Normal"
                                tienda1=registroTienda("Marita", "0987734268", estadoTienda, "Gustavo")
                                tienda2=registroTienda("XYZ", "09999923331", estadoTienda, "Jhonson")
                                lTienda.append("Marita")
                                lTienda.append("XYZ")
                                ltelefonoT.append("0987734268")
                                ltelefonoT.append( "09999923331")
                                lestadoT.append(tienda1.estadoTienda)
                                lestadoT.append(tienda2.estadoTienda)
                                lGerente.append("Gustavo")
                                lGerente.append("Jhonson")
                                print("------------------------------------------------------------")
                                print("  USTED SE PUEDE REGISTRAR EN CUALQUIERA DE ESTAS TIENDAS:  ")
                                print("------------------------------------------------------------")
                                print("TIENDA 1: ", tienda1.nombreTienda)
                                print("TIENDA 2: ", tienda2.nombreTienda)
                                print("------------------------------------------------------------")
                                opcion=int(input("Ingrese el numero de tienda en la que se desea registrar: "))
                                print("------------------------------------------------------------")
                                if opcion==1:
                                    print("USTED SE HA REGISTRADO EN LA TIENDA", tienda1.nombreTienda)
                                    estadoTienda=estado
                                    cliente1.registrarseTienda(telefono, nCedula)
                                    lHora.append(time.strftime("%H:%M:%S"))
                                    lfecha.append(time.strftime("%d/%m/%y"))
                                elif opcion==2:
                                    print("USTED SE HA REGISTRADO EN LA TIENDA ", tienda2.nombreTienda)
                                    estadoTienda=estado
                                    cliente1.registrarseTienda(telefono, nCedula)
                                    lHora.append(time.strftime("%H:%M:%S"))
                                    lfecha.append(time.strftime("%d/%m/%y"))
                        


                            elif subMenuClientes2 ==2:
                                print("------------- HISTORIAL DE TIENDAS REGISTRADAS -------------")
                                print("------------------------------------------------------------")
                                print(" Nro.|  Fecha  |   Hora   | Cliente  | Tienda ")
                                print("------------------------------------------------------------") 
                                for i, element in enumerate(lClientes):
                                 print(" ", i+1,"  ",lfecha[i] ," ",lHora[i],"  ",lClientes[i],"  ",lTienda[i])
                                 print("-----------------------------------------------------------")

                            elif subMenuClientes2 ==3:
                                print("------------------------------------------------------------")
                                print("|                REGISTRAR ESTADO DEL CLIENTE              |")
                                print("------------------------------------------------------------")
                                cliente1.estadoCliente(estado)
                            elif subMenuClientes2 ==4:
                                print("Regresar ")
                            else:
                                    print("Por favor ingrese una opcion correcta: ")
                            subMenuClientes2=int(input("\n=============================== \n Sub Menu Clientes 2: \n===============================  \n 1-Registrarse en tienda \n 2- Historial \n 3-Estado \n 4-Regresar \n Ingrese una opcion: "))
                elif subMenuClientes ==3:
                     print("Regresar ")
                else:
                        print("Por favor ingrese una opcion correcta: ")
                subMenuClientes=int(input("\n=============================== \n Sub Menu Clientes: \n=============================== \n 1-Registrarse \n 2-Ingresar sesion \n 3-Regresar \n=============================== \n Ingrese una opcion: "))
                
    elif menuPrincipal ==2:
        print("ADMIN ")
        print("------------------- HISTORIAL DE VISITAS -------------------")
        print("------------------------------------------------------------")
        print(" Nro.|  Fecha  |  Hora  | Cliente  | Tienda ")
        print("------------------------------------------------------------") 
        for i, element in enumerate(lClientes):
            print(i+1,"  ",lfecha[i] ," ",lHora[i],"  ",lClientes[i],"  ",lTienda[i])
            print("-----------------------------------------------------------")
        print("\n")
        print("------------------- HISTORIAL DE CLIENTES -------------------")
        print("------------------------------------------------------------")
        print(" Nro.| Cliente | Telefono |  Estado ")
        print("------------------------------------------------------------") 
        for i, element in enumerate(lClientes):
            print(i+1,"  ",lClientes[i],"  ",ltelefono[i],"  ",lestado[i])
            print("-----------------------------------------------------------")
        print("\n")
        print("------------------- HISTORIAL DE TIENDAS -------------------")
        print("------------------------------------------------------------")
        print(" Nro.|  Nombre  |  Telefono | Gerente |  Estado ")
        print("------------------------------------------------------------") 
        for i, element in enumerate(lTienda):
            print(i+1, lTienda[i],"  ",ltelefonoT[i],"  ",lGerente[i],"  ",lestadoT[i])
            print("-----------------------------------------------------------")



    elif menuPrincipal ==3:
        print("GRACIAS POR SU VISITA ")

    else:
        print("Por favor ingrese una opcion correcta: ")
    menuPrincipal=int(input(" \n=============================== \n Menu Principal: \n=============================== \n 1-Cliente \n 2-Admin \n 3-Salir \n=============================== \n Por favor, ingrese una opcion: "))
