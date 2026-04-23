def funcionalidade(nome):
    
    print(f"\n>>> {nome} em desenvolvimento...")
    input("Pressione ENTER para continuar...")

#-----------------------------------------------------------------------------

def ler_opcao(opcoes_validas):
    
    opcao = input("Escolha uma opção: ")
    while opcao not in opcoes_validas:
        print("Opção inválida!")
        opcao = input("Escolha uma opção: ")
    return opcao

#----------------------------------------------------------------------------

import os

def limpar_tela():
    
    os.system("cls" if os.name == "nt" else "clear")

#----------------------------------------------------------------------------

from menus.menu_gerenciamento import menu_gerenciamento
from menus.menu_votacao import menu_votacao
from utils.input_utils import ler_opcao
from utils.tela import limpar_tela

def menu_principal():
    
    opcao = ""
    while opcao != "0":
        limpar_tela()
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Gerenciamento")
        print("2 - Votação")
        print("0 - Sair")

        opcao = ler_opcao(["1", "2", "0"])

        if opcao == "1":
            menu_gerenciamento()
        elif opcao == "2":
            menu_votacao()

    print("Encerrando sistema...")

#--------------------------------------------------------------------

from utils.input_utils import ler_opcao
from utils.tela import limpar_tela
from utils.geral import funcionalidade
from database.eleitor_db import inserir_eleitor, listar_eleitores, buscar_eleitor

def menu_gerenciamento():
    opcao = ""
    while opcao != "0":
        limpar_tela()
        print("\n=== GERENCIAMENTO ===")
        print("1 - Eleitores")
        print("2 - Candidatos")
        print("0 - Voltar")

        opcao = ler_opcao(["1", "2", "0"])

        if opcao == "1":
            menu_eleitores()
        elif opcao == "2":
            menu_candidatos()

def menu_eleitores():
    opcao = ""
    while opcao != "0":
        limpar_tela()
        print("\n--- ELEITORES ---")
        print("1 - Cadastrar")
        print("2 - Editar")
        print("3 - Remover")
        print("4 - Buscar")
        print("5 - Listar")
        print("0 - Voltar")

        opcao = ler_opcao(["1","2","3","4","5","0"])

        if opcao == "1":
            inserir_eleitor()
        elif opcao == "5":
            listar_eleitores()
        elif opcao == "4":
            buscar_eleitor()
        elif opcao != "0":
            funcionalidade("Função ainda não implementada")

def menu_candidatos():
    opcao = ""
    while opcao != "0":
        limpar_tela()
        print("\n--- CANDIDATOS ---")
        print("1 - Listar")
        print("0 - Voltar")

        opcao = ler_opcao(["1","0"])
        if opcao == "1":
           listar_candidatos()

#----------------------------------------------------------------------------

from utils.input_utils import ler_opcao
from utils.tela import limpar_tela
from utils.geral import funcionalidade

def menu_votacao():
    opcao = ""
    while opcao != "0":
        limpar_tela()
        print("\n=== VOTAÇÃO ===")
        print("1 - Abrir Sistema de Votação")
        print("2 - Auditoria")
        print("3 - Resultados")
        print("0 - Voltar")

        opcao = ler_opcao(["1","2","3","0"])

        if opcao != "0":
            funcionalidade("Votação")

from menus.menu_principal import menu_principal

#----------------------------------------------------------------------------

if __name__ == "__main__":
    menu_principal()
