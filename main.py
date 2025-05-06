import os
from portScanner import run_port_scanner

print("""
Bem-Vindo ao App de Reconhecimento de Alvo \n
1.Escaneamento de Portas
2.Verificação de Firewall
3.Escaneamento de Vulnerabilidades
4.Enumeração de Subdomínios
5.Análise da Infraestrutura
6.Sair \n
Escolha uma opção:""")

opcao = None
while opcao is None:
    try:
        opcao = int(input())
        if opcao < 1 or opcao > 6:
            print("Erro: A opção deve ser um número entre 1 e 6")
            print("\nEscolha uma opção:")
            opcao = None
    except (TypeError, ValueError):
        print("Erro: A opção deve ser um número entre 1 e 6")
        print("\nEscolha uma opção:")

if opcao == 1:
    run_port_scanner()

elif opcao == 2:
    print("Digite a URL que deseja verificar:")
    url = input()
    os.system(f"wafw00f {url}") # https://

elif opcao == 3:
    print("Digite o domínio que deseja verificar:")
    dominio = input()
    os.system(f"nmap -sV --script vuln {dominio}") # site sem www ou ip

elif opcao == 4:
    print("Digite o domínio que deseja verificar:")
    dominio = input()
    os.system(f"dnsenum --enum {dominio}") # site com www ou ip

elif opcao == 5:
    print("Digite o domínio que deseja verificar:")
    dominio = input()
    os.system(f"nikto -h {dominio}")

elif opcao == 6:
    print("Fechando aplicativo")
