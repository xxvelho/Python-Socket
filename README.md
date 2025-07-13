# Sala de Bate-Papo (Chat Room)

## 📚 Descrição

Projeto para implementar uma **Sala de Bate-Papo** segundo o paradigma **cliente-servidor**, utilizando a API de sockets.

Uma sala de bate-papo é um ambiente virtual onde múltiplos usuários podem se conectar com o intuito de trocar mensagens entre si. A sala deve permitir **comunicação síncrona**, ou seja, os usuários precisam estar online para conversar.

---

## 🎯 Objetivos

- Suportar até **10 clientes simultâneos**.
- Usuário deve informar:
  - `usuário/senha`
  - `hostname` do servidor no início da conexão.
- Mensagens enviadas para o servidor são **replicadas para todos os clientes conectados**.
- Comandos especiais:
  - `exit` / `quit`: cliente sai da sala e servidor informa a todos.
  - `shutdown`: administrador encerra o servidor avisando com 10 segundos de antecedência.
- Threads no cliente e no servidor:
  - Uma thread para **receber mensagens**.
  - Outra thread para **enviar mensagens**.
- **Desafio opcional**: permitir **envio de arquivos (ex: imagens)** entre clientes.

---
