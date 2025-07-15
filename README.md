# 💬 Sala de Bate-Papo (Chat Room)

**Trabalho de Redes de Computadores II - UFMA**  
**Professor:** Mário Meireles Teixeira

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://python.org)
[![Sockets](https://img.shields.io/badge/Sockets-TCP-green.svg)](https://docs.python.org/3/library/socket.html)
[![Threading](https://img.shields.io/badge/Threading-Multithreaded-orange.svg)](https://docs.python.org/3/library/threading.html)

---

## 📚 **DESCRIÇÃO**

Sistema de **chat em tempo real** implementado com paradigma **cliente-servidor** usando API de sockets Python. Permite que múltiplos usuários (até 10) se conectem simultaneamente para trocar mensagens e arquivos.

### ✨ **Funcionalidades Principais:**

- 🔐 **Autenticação** de usuários com senha
- 💬 **Chat em tempo real** entre múltiplos clientes
- 📁 **Transferência de arquivos** (desafio opcional implementado!)
- 🚪 **Comando exit/quit** com notificação de saída
- 🔌 **Comando shutdown** administrativo com aviso de 10 segundos
- 🧵 **Multithreading** para recepção e envio simultâneos

---

## 🛠️ **REQUISITOS TÉCNICOS**

- **Python 3.x**
- **Bibliotecas padrão:** `socket`, `threading`, `base64`, `os`, `time`
- **Sistema operacional:** Windows, macOS, Linux
- **Rede:** Conexão TCP/IP (localhost ou rede local)

---

## 📁 **ESTRUTURA DO PROJETO**

```
Python-Socket/
├── servidor.py              # Servidor principal do chat
├── cliente.py               # Cliente do chat
├── arquivo_teste.txt        # Arquivo para testar transferências
├── demonstracao.py          # Script de demonstração
├── roteiro_testes.md        # Roteiro completo de testes
└── README.md               # Este arquivo
```

---

## 🚀 **COMO EXECUTAR O SISTEMA**

### **1. Preparação do Ambiente**

```bash
# Navegue para a pasta do projeto
cd "Python-Socket"

# Verifique se tem Python 3
python3 --version
```

### **2. Iniciar o Servidor**

```bash
# Terminal 1 - Servidor
python3 servidor.py
```

**✅ Deve aparecer:** `Servidor iniciado e aguardando conexões...`

### **3. Conectar Clientes**

```bash
# Terminal 2 - Cliente 1
python3 cliente.py

# Terminal 3 - Cliente 2
python3 cliente.py

# Terminal 4 - Cliente 3 (opcional)
python3 cliente.py
```

### **4. Fazer Login**

Para cada cliente, digite:

```
Digite o hostname/IP do servidor: 127.0.0.1
Digite seu nome de usuário: user1        # ou user2, user3, etc.
Digite sua senha: senha1                # ou senha2, senha3, etc.
```

---

## 👤 **USUÁRIOS DISPONÍVEIS**

| Usuário  | Senha     | Descrição     |
| -------- | --------- | ------------- |
| `admin`  | `admin`   | Administrador |
| `user1`  | `senha1`  | Usuário 1     |
| `user2`  | `senha2`  | Usuário 2     |
| `user3`  | `senha3`  | Usuário 3     |
| `user4`  | `senha4`  | Usuário 4     |
| `user5`  | `senha5`  | Usuário 5     |
| `user6`  | `senha6`  | Usuário 6     |
| `user7`  | `senha7`  | Usuário 7     |
| `user8`  | `senha8`  | Usuário 8     |
| `user9`  | `senha9`  | Usuário 9     |
| `user10` | `senha10` | Usuário 10    |

---

## 💻 **COMANDOS DISPONÍVEIS**

### **Para Clientes:**

- **Mensagem normal:** Digite qualquer texto e pressione Enter
- **Enviar arquivo:** `/send nome_arquivo.ext`
- **Sair do chat:** `exit` ou `quit`

### **Para Servidor (Administrador):**

- **Encerrar servidor:** `shutdown` (avisa clientes e aguarda 10s)

---

## 📁 **TRANSFERÊNCIA DE ARQUIVOS (Desafio Opcional)**

### **Como usar:**

1. **Enviar arquivo:** Digite `/send arquivo_teste.txt` no chat
2. **Receber arquivo:** Arquivos são automaticamente salvos na pasta `downloads/`
3. **Tipos suportados:** Qualquer tipo de arquivo (txt, jpg, png, pdf, etc.)

### **Protocolo implementado:**

- **Formato:** `FILE:nome_arquivo:dados_base64`
- **Codificação:** Base64 para transmissão segura
- **Buffer:** 4KB para suportar arquivos maiores

### **Exemplo prático:**

```
user1: /send arquivo_teste.txt
📤 Arquivo 'arquivo_teste.txt' enviado!

# Outros usuários veem:
📁 user1 enviou o arquivo: arquivo_teste.txt
📥 Arquivo recebido: arquivo_teste.txt (salvo em downloads/)
```

---

## 🧪 **COMO TESTAR O SISTEMA COMPLETO**

### **Teste Rápido (5 minutos):**

```bash
# 1. Execute o script de demonstração
python3 demonstracao.py

# 2. Siga os 7 testes básicos:
# ✅ Autenticação válida/inválida
# 💬 Troca de mensagens
# 👥 Múltiplos clientes
# 📁 Transferência de arquivos
# 🚪 Comando exit
# 🔌 Comando shutdown
```

### **Teste Detalhado:**

1. **Autenticação:**

   - ✅ Tente login com `user1/senha1` (deve funcionar)
   - ❌ Tente login com `user1/senha_errada` (deve falhar)

2. **Mensagens:**

   - Conecte 2+ clientes
   - Digite mensagens em um cliente
   - Verifique se aparecem em vermelho nos outros

3. **Transferência de Arquivos:**

   - Digite `/send arquivo_teste.txt`
   - Verifique se o arquivo aparece em `downloads/`

4. **Comandos Especiais:**
   - Digite `exit` em um cliente
   - Digite `shutdown` no servidor

---

## 🎯 **REQUISITOS ATENDIDOS**

### ✅ **Requisitos Obrigatórios:**

- [x] Paradigma cliente-servidor com sockets
- [x] Comunicação síncrona (usuários online)
- [x] Cliente fornece usuário/senha e hostname
- [x] Suporte para até 10 clientes simultâneos
- [x] Mensagens replicadas para todos os clientes
- [x] Comando exit/quit com notificação de saída
- [x] Comando shutdown com aviso de 10 segundos
- [x] Threads no servidor (uma por cliente)
- [x] Threads no cliente (recepção e envio)

### ✅ **Desafio Opcional:**

- [x] **Transferência de arquivos** entre clientes

---

## 🔧 **DETALHES TÉCNICOS**

### **Protocolo de Comunicação:**

- **Mensagens normais:** `texto_da_mensagem`
- **Arquivos:** `FILE:nome_arquivo:dados_base64`
- **Autenticação:** `usuario:senha`
- **Comando de saída:** `exit`

### **Threading:**

- **Servidor:** Thread principal + thread por cliente + thread admin
- **Cliente:** Thread para receber + thread para enviar

---

## 🐛 **SOLUÇÃO DE PROBLEMAS**

### **Erro: "Address already in use"**

```bash
# Mate processos Python em execução
pkill -f python3
# Aguarde alguns segundos e tente novamente
```

### **Arquivo não transfere:**

- Verifique se o arquivo existe na pasta
- Confirme que digitou `/send` antes do nome
- Arquivos grandes podem demorar mais

### **Cliente não conecta:**

- Verifique se o servidor está rodando
- Confirme o IP (use `127.0.0.1` para localhost)
- Verifique usuário/senha (case-sensitive)

---

## 📖 **DOCUMENTAÇÃO ADICIONAL**

- 📋 **Roteiro completo:** `roteiro_testes.md`
- 🎯 **Script de demo:** `python3 demonstracao.py`
- 📁 **Arquivo de teste:** `arquivo_teste.txt`

---

## 🎓 **INFORMAÇÕES ACADÊMICAS**

**Disciplina:** Redes de Computadores II  
**Instituição:** Universidade Federal do Maranhão (UFMA)  
**Professor:** Mário Meireles Teixeira  
**Paradigma:** Cliente-Servidor  
**Tecnologia:** Python Sockets + Threading

### **Critérios de Avaliação Atendidos:**

- ✅ Implementação correta do protocolo cliente-servidor
- ✅ Uso adequado de sockets TCP
- ✅ Implementação de threading para concorrência
- ✅ Autenticação de usuários
- ✅ Comandos especiais (exit, shutdown)
- ✅ Código organizado e comentado
- ✅ **Desafio opcional implementado** (transferência de arquivos)

---
