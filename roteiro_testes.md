# 🧪 ROTEIRO COMPLETO DE TESTES

**Trabalho: Sala de Bate-Papo - Redes de Computadores II - UFMA**

## 📋 PREPARAÇÃO DOS TESTES

### 1. Abrir terminais necessários:

- **Terminal 1**: Servidor
- **Terminal 2**: Cliente 1
- **Terminal 3**: Cliente 2
- **Terminal 4**: Cliente 3 (opcional para teste de múltiplos clientes)

### 2. Comandos iniciais:

```bash
cd "Python-Socket"
python3 servidor.py    # Terminal 1
python3 cliente.py     # Terminais 2, 3, 4
```

---

## ✅ TESTE 1: AUTENTICAÇÃO DE USUÁRIOS

### Teste 1.1: Login válido ✅

**Terminal 2 (Cliente 1):**

```
Digite o hostname/IP do servidor: 127.0.0.1
Digite seu nome de usuário: user1
Digite sua senha: senha1
```

**Resultado esperado:** ✅ Conectado com sucesso!

### Teste 1.2: Login inválido ❌

**Terminal 3 (Cliente 2):**

```
Digite o hostname/IP do servidor: 127.0.0.1
Digite seu nome de usuário: user1
Digite sua senha: senha_errada
```

**Resultado esperado:** ❌ Autenticação falhou! Conexão encerrada.

### Teste 1.3: Login válido alternativo ✅

**Terminal 3 (Cliente 2 - segundo teste):**

```
Digite o hostname/IP do servidor: 127.0.0.1
Digite seu nome de usuário: user2
Digite sua senha: senha2
```

**Resultado esperado:** ✅ Conectado com sucesso!

---

## ✅ TESTE 2: COMUNICAÇÃO ENTRE CLIENTES

### Teste 2.1: Mensagem do Cliente 1 para todos

**Terminal 2 (user1):**

```
Olá pessoal, este é o user1!
```

**Resultado esperado:**

- **Terminal 3 (user2):** Recebe "user1: Olá pessoal, este é o user1!" em vermelho

### Teste 2.2: Mensagem do Cliente 2 para todos

**Terminal 3 (user2):**

```
Oi user1! Aqui é o user2 respondendo!
```

**Resultado esperado:**

- **Terminal 2 (user1):** Recebe "user2: Oi user1! Aqui é o user2 respondendo!" em vermelho

---

## ✅ TESTE 3: MÚLTIPLOS CLIENTES (ATÉ 10)

### Teste 3.1: Conectar 3º cliente

**Terminal 4 (Cliente 3):**

```
Digite o hostname/IP do servidor: 127.0.0.1
Digite seu nome de usuário: user3
Digite sua senha: senha3
```

### Teste 3.2: Mensagem com 3 clientes conectados

**Terminal 4 (user3):**

```
Chegou o user3! Todos me ouvem?
```

**Resultado esperado:**

- **Terminal 2 (user1):** Recebe a mensagem
- **Terminal 3 (user2):** Recebe a mensagem
- **Terminal 1 (Servidor):** Mostra notificação de entrada

---

## ✅ TESTE 4: COMANDO EXIT/QUIT

### Teste 4.1: Cliente sai voluntariamente

**Terminal 4 (user3):**

```
exit
```

**Resultado esperado:**

- **Terminal 4:** "Você saiu da sala."
- **Terminal 2,3:** "user3 saiu da sala." em vermelho
- **Terminal 1:** Log da desconexão

---

## ✅ TESTE 5: TRANSFERÊNCIA DE ARQUIVOS (DESAFIO OPCIONAL)

### Teste 5.1: Criar arquivo de teste

**Terminal 1 (Servidor):**

```bash
echo "📁 Arquivo de teste para demonstração!" > arquivo_teste.txt
```

### Teste 5.2: Enviar arquivo

**Terminal 2 (user1):**

```
/send arquivo_teste.txt
```

**Resultado esperado:**

- **Terminal 2:** "📤 Arquivo 'arquivo_teste.txt' enviado!"
- **Terminal 3:** "📁 user1 enviou o arquivo: arquivo_teste.txt"
- **Terminal 3:** "📥 Arquivo recebido: arquivo_teste.txt (salvo em downloads/)"

### Teste 5.3: Verificar arquivo recebido

**Terminal 3:**

```bash
ls downloads/
cat downloads/arquivo_teste.txt
```

**Resultado esperado:** Arquivo transferido corretamente

---

## ✅ TESTE 6: COMANDO SHUTDOWN (ADMINISTRADOR)

### Teste 6.1: Shutdown do servidor

**Terminal 1 (Servidor):**

```
shutdown
```

**Resultado esperado:**

- **Terminal 1:** "Servidor será desligado em 10 segundos..."
- **Terminal 2,3:** "Servidor será desligado em 10 segundos..."
- Aguarda 10 segundos
- **Terminal 1:** "Servidor encerrado."
- **Terminal 2,3:** "Servidor encerrando conexão."

---

## 📸 DOCUMENTAÇÃO DOS TESTES

### Screenshots necessários:

1. ✅ Login bem-sucedido
2. ❌ Login com falha
3. 💬 Troca de mensagens entre clientes
4. 👥 Múltiplos clientes conectados
5. 🚪 Notificação de saída de cliente
6. 📁 Transferência de arquivo
7. 🔌 Shutdown do servidor

### Relatório final:

- [ ] Todos os requisitos obrigatórios testados ✅
- [ ] Desafio opcional (arquivos) testado ✅
- [ ] Screenshots capturados 📸
- [ ] Funcionamento conforme especificação ✅

---

## 🎯 CRITÉRIOS DE SUCESSO

✅ **APROVADO** se todos os testes passarem:

- Autenticação funciona (válida/inválida)
- Mensagens são replicadas para todos
- Suporte a múltiplos clientes (testado com 3+)
- Comando exit funciona com notificação
- Comando shutdown funciona com aviso
- Transferência de arquivos funciona (opcional)
- Threads funcionam corretamente (recepção simultânea)

**🏆 TRABALHO COMPLETO E FUNCIONANDO!**
