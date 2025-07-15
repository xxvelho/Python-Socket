import socket
from threading import Thread
import os
import base64


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

        # Aguarda resposta de autenticação do servidor
        resposta = self.socket.recv(1024).decode()
        if "falhou" in resposta.lower():
            print("❌ Autenticação falhou! Conexão encerrada.")
            self.socket.close()
            os._exit(0)
        print("✅ Conectado com sucesso!")

        # Inicia thread para receber mensagens enquanto envia no thread principal
        Thread(target=self.receber_mensagens).start()
        self.enviar_mensagens()

    def enviar_credenciais(self):
        # Envia nome e senha concatenados para o servidor
        credenciais = f"{self.nome}:{self.senha}"
        self.socket.send(credenciais.encode())

    def enviar_arquivo(self, nome_arquivo):
        # Envia arquivo para o servidor
        try:
            if not os.path.exists(nome_arquivo):
                print(f"❌ Arquivo '{nome_arquivo}' não encontrado!")
                return

            with open(nome_arquivo, "rb") as arquivo:
                dados_arquivo = arquivo.read()
                dados_base64 = base64.b64encode(dados_arquivo).decode()

            # Protocolo: FILE:nome_arquivo:dados_base64
            mensagem_arquivo = f"FILE:{nome_arquivo}:{dados_base64}"
            self.socket.send(mensagem_arquivo.encode())
            print(f"Arquivo '{nome_arquivo}' enviado!")

        except Exception as e:
            print(f"❌ Erro ao enviar arquivo: {e}")

    def enviar_mensagens(self):
        # Loop para ler input do usuário e enviar mensagens
        print(
            "Digite suas mensagens ou use '/send nome_arquivo.ext' para enviar arquivos:"
        )
        while True:
            mensagem = input()
            if mensagem.strip().lower() in ["exit", "quit"]:
                # Se usuário digitar 'exit' ou 'quit', encerra a conexão
                self.socket.send("exit".encode())
                print("Você saiu da sala.")
                os._exit(0)
            elif mensagem.startswith("/send "):
                # Comando para enviar arquivo
                nome_arquivo = mensagem[6:].strip()  # Remove '/send '
                self.enviar_arquivo(nome_arquivo)
            else:
                self.socket.send(mensagem.encode())

    def receber_mensagens(self):
        # Loop para receber e imprimir mensagens do servidor
        while True:
            mensagem_servidor = self.socket.recv(
                4096
            ).decode()  # Buffer maior para arquivos
            if not mensagem_servidor.strip():
                os._exit(0)

            if mensagem_servidor.startswith("FILE:"):
                # Arquivo recebido
                self.processar_arquivo_recebido(mensagem_servidor)
            else:
                # Mensagem normal - exibe em destaque (vermelho)
                print(f"\033[1;31;40m{mensagem_servidor}\033[0m")

    def processar_arquivo_recebido(self, mensagem_arquivo):
        # Processa arquivo recebido do servidor
        try:
            partes = mensagem_arquivo.split(":", 2)
            nome_arquivo = partes[1]
            dados_base64 = partes[2]

            # Decodifica os dados
            dados_arquivo = base64.b64decode(dados_base64)

            # Salva na pasta 'downloads'
            pasta_downloads = "downloads"
            if not os.path.exists(pasta_downloads):
                os.makedirs(pasta_downloads)

            caminho_arquivo = os.path.join(pasta_downloads, nome_arquivo)
            with open(caminho_arquivo, "wb") as arquivo:
                arquivo.write(dados_arquivo)

            print(
                f"\033[1;32;40mArquivo recebido: {nome_arquivo} (salvo em downloads/)\033[0m"
            )

        except Exception as e:
            print(f"❌ Erro ao processar arquivo recebido: {e}")


if __name__ == "__main__":
    Cliente()
