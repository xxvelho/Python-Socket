#!/usr/bin/env python3
"""
🎯 SCRIPT DE DEMONSTRAÇÃO - TRABALHO DE REDES II
Sala de Bate-Papo com Transferência de Arquivos
UFMA - Prof. Mário Meireles Teixeira
"""

import os
import sys


def print_header():
    """Imprime cabeçalho da demonstração"""
    print("=" * 60)
    print("🎯 DEMONSTRAÇÃO - SALA DE BATE-PAPO")
    print("📚 Redes de Computadores II - UFMA")
    print("👨‍🏫 Prof. Mário Meireles Teixeira")
    print("=" * 60)


def print_usuarios():
    """Lista todos os usuários disponíveis"""
    print("\n👥 USUÁRIOS DISPONÍVEIS PARA TESTE:")
    print("-" * 40)
    usuarios = [
        ("admin", "admin"),
        ("user1", "senha1"),
        ("user2", "senha2"),
        ("user3", "senha3"),
        ("user4", "senha4"),
        ("user5", "senha5"),
        ("user6", "senha6"),
        ("user7", "senha7"),
        ("user8", "senha8"),
        ("user9", "senha9"),
        ("user10", "senha10"),
    ]

    for i, (usuario, senha) in enumerate(usuarios, 1):
        print(f"{i:2d}. 👤 {usuario:<8} | 🔑 {senha}")


def print_comandos():
    """Lista todos os comandos disponíveis"""
    print("\n💻 COMANDOS DISPONÍVEIS:")
    print("-" * 40)
    print("📝 Mensagens normais: Digite qualquer texto")
    print("📁 Enviar arquivo: /send nome_arquivo.ext")
    print("🚪 Sair do chat: exit ou quit")
    print("🔌 Encerrar servidor: shutdown (apenas no console do servidor)")


def print_testes():
    """Lista sequência de testes recomendados"""
    print("\n🧪 SEQUÊNCIA DE TESTES RECOMENDADOS:")
    print("-" * 40)
    testes = [
        "1. ✅ Testar login válido (user1/senha1)",
        "2. ❌ Testar login inválido (user1/senhaerrada)",
        "3. 💬 Conectar 2+ clientes e trocar mensagens",
        "4. 👥 Testar notificação de entrada de usuários",
        "5. 📁 Testar transferência de arquivo (/send arquivo_teste.txt)",
        "6. 🚪 Testar comando exit e notificação de saída",
        "7. 🔌 Testar comando shutdown do servidor",
    ]

    for teste in testes:
        print(teste)


def print_arquivos():
    """Lista arquivos disponíveis para teste"""
    print("\n📂 ARQUIVOS DISPONÍVEIS PARA TESTE:")
    print("-" * 40)

    arquivos_teste = ["arquivo_teste.txt", "README.md", "roteiro_testes.md"]
    for arquivo in arquivos_teste:
        if os.path.exists(arquivo):
            tamanho = os.path.getsize(arquivo)
            print(f"📄 {arquivo:<20} ({tamanho} bytes)")
        else:
            print(f"❌ {arquivo:<20} (não encontrado)")


def verificar_ambiente():
    """Verifica se o ambiente está pronto para demonstração"""
    print("\n🔍 VERIFICAÇÃO DO AMBIENTE:")
    print("-" * 40)

    arquivos_necessarios = ["servidor.py", "cliente.py"]
    todos_ok = True

    for arquivo in arquivos_necessarios:
        if os.path.exists(arquivo):
            print(f"✅ {arquivo} - OK")
        else:
            print(f"❌ {arquivo} - FALTANDO!")
            todos_ok = False

    if todos_ok:
        print("🎉 Ambiente pronto para demonstração!")
    else:
        print("⚠️  Alguns arquivos estão faltando!")

    return todos_ok


def main():
    """Função principal da demonstração"""
    print_header()

    if not verificar_ambiente():
        print("\n❌ Ambiente não está pronto. Verifique os arquivos!")
        sys.exit(1)

    print_usuarios()
    print_comandos()
    print_arquivos()
    print_testes()

    print("\n" + "=" * 60)
    print("🚀 COMO INICIAR A DEMONSTRAÇÃO:")
    print("=" * 60)
    print("1. 🖥️  Terminal 1: python3 servidor.py")
    print("2. 👤 Terminal 2: python3 cliente.py")
    print("3. 👤 Terminal 3: python3 cliente.py")
    print("4. 👤 Terminal 4: python3 cliente.py (opcional)")
    print()
    print("💡 Dica: Use usuários diferentes em cada terminal!")
    print("📖 Consulte: roteiro_testes.md para detalhes completos")
    print("=" * 60)


if __name__ == "__main__":
    main()
