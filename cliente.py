import socket
from threading import Thread
import os

class Cliente:
    def __init__(self):
        host = input("Digite o hostname/IP do servidor: ")
        porta = 7632

        self.socket = socket.socket()
        self.socket.connect((host, porta))

        self.nome = input("Digite seu nome de usuário: ")
        self.senha = input("Digite sua senha: ")
        self.enviar_credenciais()

        Thread(target=self.receber_mensagens).start()
        self.enviar_mensagens()

    def enviar_credenciais(self):
        credenciais = f"{self.nome}:{self.senha}"
        self.socket.send(credenciais.encode())

    def enviar_mensagens(self):
        while True:
            mensagem = input()
            if mensagem.strip().lower() in ['exit', 'quit']:
                self.socket.send('exit'.encode())
                print("Você saiu da sala.")
                os._exit(0)
            self.socket.send(mensagem.encode())

    def receber_mensagens(self):
        while True:
            mensagem_servidor = self.socket.recv(1024).decode()
            if not mensagem_servidor.strip():
                os._exit(0)
            print(f"\033[1;31;40m{mensagem_servidor}\033[0m")

if __name__ == "__main__":
    Cliente()
