import tkinter as tk
from tkinter import messagebox
import abc


class Interface:
    def __init__(self):
        self.saldo = Saldo()
        self.extrato = Extrato()
        self.deposito = Deposito()
        self.saque = Saque()
        self.transferencia = Transferencia()
     
    def imprimir_interface(self):
        root = tk.Tk()
        frame = tk.Frame(root)
        frame.pack()

        b_saldo = tk.Button(frame, text = "Saldo", command = self.saldo.resposta)
        b_saldo.pack(side=tk.LEFT)
        
        b_extrato = tk.Button(frame, text = "Extrato", command = self.extrato.resposta)
        b_extrato.pack(side=tk.LEFT)
        
        b_deposito =  tk.Button(frame, text = "Deposito", command = self.deposito.resposta)
        b_deposito.pack(side=tk.LEFT)

        b_saldo = tk.Button(frame, text = "Saldo", command = self.saldo.resposta)
        b_saldo.pack(side=tk.LEFT)

        b_saque =  tk.Button(frame, text = "Saque", command = self.saque.resposta)
        b_saque.pack(side=tk.LEFT)
      
        b_transferencia =  tk.Button(frame, text = "Transferencia", command = self.transferencia.resposta)
        b_transferencia.pack(side=tk.LEFT)
    
        b_sair = tk.Button(frame, text = "Sair", command = frame.quit)
        b_sair.pack(side=tk.LEFT)
        
        root.mainloop()

    
class Comando():
        
    @abc.abstractmethod
    def resposta(self):
        pass

class Saldo(Comando):
    def resposta(self):
        msg = messagebox.showinfo("Saldo","Seu saldo é R$ (buscar no banco de dados)")    
        
class Extrato(Comando):
    def resposta(self):
        msg = messagebox.showinfo("Extrato","Seu extrato é: (buscar no banco de dados)")   
    

class Deposito(Comando):
    def resposta(self):
                msg = messagebox.showinfo("Deposito","Insira valor a ser depositado (remover valor na conta armazenada no banco de dados)")  
    
        
class Saque(Comando):
    def resposta(self):
        msg = messagebox.showinfo("Saque","Insira valor a ser sacado (remover valor na conta armazenada no banco de dados)")  
   
class Transferencia(Comando):
    def resposta(self):
        msg = messagebox.showinfo("Transferencia","Insira valor e conta de depósito (remover valor na conta do cliente e aumentar na do recebedor armazenadas no banco de dados)")  

banco = Interface()
banco.imprimir_interface()
