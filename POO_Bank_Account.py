class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True
    def deposit(self, amount): #Depositar
        if self.is_active:
            self.balance += amount
            print(f"Se a depositado {amount} en la cuenta de {self.account_holder}. \nSaldo actual es: {self.balance}")
        else:
            print(f"No se puede depositar, cuenta de {self.account_holder} está inactiva")
    def withdraw(self, amount): #Retirar
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                print (f"Se ha retirado {amount} de la cuenta de {self.account_holder}. \n Saldo actual es: {self.balance}")
            else:
                print(f"Saldo insuficiente para retirar, su saldo actual es {self.balance} bs.")
        else:
            print(f"La cuenta de {self.account_holder} esta desactivada \nNo se puede retirar")        
    def desactive_account(self): 
        self.is_active = False
        print("Cuenta desactivada")

    def active_account(self):
        self.is_active = True
        print("Cuenta Activada Correctamente")

# Llamada a los OBJETOS
# Nombre = Clase (Parametro1, Parametro2, ParametroN)
account1 = BankAccount("Ana", 500)
account2 = BankAccount("Luis", 1000)


# Llamada a los métodos
account1.deposit(200)
account2.deposit(100)
account1.desactive_account()
account1.deposit(50)
account1.active_account()
account1.deposit(50)
account2.desactive_account()
account2.withdraw(1800)

# ```class BankAccount:    def \_\_init\_\_(self, account\_holder, balance):        self.account\_holder = account\_holder        self.balance = balance        self.is\_active = True    def deposit(self, amount): #Depositar        if self.is\_active:            self.balance += amount            print(f"Se a depositado {amount} en la cuenta de {self.account\_holder}. \nSaldo actual es: {self.balance}")        else:            print(f"No se puede depositar, cuenta de {self.account\_holder} está inactiva")    def withdraw(self, amount): #Retirar        if self.is\_active:            if amount <= self.balance:                self.balance -= amount                print (f"Se ha retirado {amount} de la cuenta de {self.account\_holder}. \n Saldo actual es: {self.balance}")            else:                print(f"Saldo insuficiente para retirar, su saldo actual es {self.balance} bs.")        else:            print(f"La cuenta de {self.account\_holder} esta desactivada \nNo se puede retirar")            def desactive\_account(self):         self.is\_active = False        print("Cuenta desactivada")
#     def active\_account(self):        self.is\_active = True        print("Cuenta Activada Correctamente")account1 = BankAccount("Ana", 500)account2 = BankAccount("Luis", 1000)
# \#Llamada a los métodos
# account1.deposit(200)account2.deposit(100)
# account1.desactive\_account()account1.deposit(50)
# account1.active\_account()account1.deposit(50)
# account2.desactive\_account()account2.withdraw(1800)