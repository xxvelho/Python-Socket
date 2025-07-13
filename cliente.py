import socket
from threading import Thread
import os

class Cliente:
    def __init__(self):
        # Solicita o IP/hostname do servidor e define porta fixa
        host = input("Digite o hostname/IP do servidor: ")
        porta = 7632

        # Cria socket TCP e conecta no servidor
        self.socket = socket.socket()
        self.socket.connect((host, porta))

        # Pega credenciais do usuário
        self.nome = input("Digite seu nome de usuário: ")
        self.senha = input("Digite sua senha: ")
        self.enviar_credenciais()

        # Inicia thread para receber mensagens enquanto envia no thread principal
        Thread(target=self.receber_mensagens).start()
        self.enviar_mensagens()

    def enviar_credenciais(self):
        # Envia nome e senha concatenados para o servidor
        credenciais = f"{self.nome}:{self.senha}"
        self.socket.send(credenciais.encode())

    def enviar_mensagens(self):
        # Loop para ler input do usuário e enviar mensagens
        while True:
            mensagem = input()
            if mensagem.strip().lower() in ['exit', 'quit']:
                # Se usuário digitar 'exit' ou 'quit', encerra a conexão
                self.socket.send('exit'.encode())
                print("Você saiu da sala.")
                os._exit(0)
            self.socket.send(mensagem.encode())

    def receber_mensagens(self):
        # Loop para receber e imprimir mensagens do servidor
        while True:
            mensagem_servidor = self.socket.recv(1024).decode()
            if not mensagem_servidor.strip():
                os._exit(0)
            # Exibe mensagem recebida em destaque (vermelho)
            print(f"\033[1;31;40m{mensagem_servidor}\033[0m")

if __name__ == "__main__":
    Cliente()
