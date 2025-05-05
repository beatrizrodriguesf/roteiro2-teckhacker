import os

os.system("python --version")

print("""
Bem-Vindo ao App de Reconhecimento de Alvo
1.PortScan
2.Wafw00f
3.Escaneamento de Vulnerabilidades
4.Enumeração de subdomínios
Escolha uma ferramenta:
""")

opcao = None
while opcao is None:
    try:
        opcao = int(input())
        if opcao < 1 or opcao > 4:
            print("A opção deve ser um número entre 1 e 4")
            opcao = None
    except (TypeError, ValueError):
        print("A opção deve ser um número entre 1 e 4")

if opcao == 2:
    print("Digite a URL que deseja verificar:")
    url = input()
    os.system(f"wafw00f {url}") # https:// ou ip

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
