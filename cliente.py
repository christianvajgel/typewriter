# typewriter
# PROJETO DE BLOCO - Arquitetura de Computadores, Sistemas Operacionais e Redes [18E4-19E1] - Instituto Infnet.
# Christian Vajgel - 29/03/2019 - Thonny IDE - Conceito DML (10/10).
# cliente
#
# Camila Costa
# Christian Vajgel - christian.vajgel@al.infnet.edu.br | linkedin.com/in/christianvajgel/
# Christian Tavares
# Thiago Rios
#
# All Rights Reserved.

import cpuinfo, datetime, time, platform, os, nmap, subprocess, socket, pickle

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = socket.gethostname() 
PORT = 12345
HP = (HOST, PORT)
quant = 32768

def menu():

    print('==============================')
    print('1- Processador')
    print('2- Memória')
    print('3- Armazenamento')
    print('4- Arquivos e diretórios')
    print('5- Processos | PID')
    print('6- Rede')
    print('7- Nmap')
    print('==============================')

try:
    cliente.connect(HP)
    req = " "
    cliente.send(req.encode('utf-8'))
    
    while True:
        menu()
        req = input('Digite a opção desejada:')
        
        if (req == "1") | (req == "2") | (req == "3") | (req == "4") | (req == "5") | (req == "6"): #| (req == "7"): 
            cliente.send(req.encode('utf-8'))
            bytes_resp = cliente.recv(quant)
            resposta = pickle.loads(bytes_resp)
            
            if req == "1":
                print("\n1- Processador:\n")
                legenda_processador = ['Modelo:', 'Arquitetura:', 'Palavra (bits):', 'Frequência Base:', 'Frequência média (GHz):', 'Uso (%):', 'Uso núcleos (%):', 'Núcleos Lógicos:', 'Núcleos Físicos:', 'Troca de contexto (boot):', 'Interrupções (boot):', 'Chamadas de sistema (boot):']
                var=' | '.join(map(str,resposta[6]))
                valor_processador = [resposta[0], resposta[1], resposta[2], resposta[3], resposta[4], resposta[5], var, resposta[7], resposta[8]]
                for x,y in zip(legenda_processador,valor_processador):
                    print ('{:30}{:30}'.format(x,y))
                time.sleep(10)
                os.system('cls')
            
            elif req == "2":
                print("\n2- Memória\n")
                legenda_memoria = ['RAM total (GB):', 'RAM livre (GB):', 'RAM uso (%):', 'Swap total (GB):', 'Swap livre (GB):']
                for x,y in zip(legenda_memoria,resposta):
                    print ('{:30}{:30}'.format(x,y))
                time.sleep(10)
                os.system('cls')
            
            elif req == "3":
                print("\n3- Armazenamento\n")
                legenda_armazenamento = ['Total (GB):', 'Livre (GB):', 'Utilizado (%):']
                for x,y in zip(legenda_armazenamento,resposta):
                    print ('{:30}{:30}'.format(x,y))
                time.sleep(10)
                os.system('cls')
                
            elif req == "4":
                
                print("\n4- Arquivos e Diretórios\n")
                print("")
                print("\nDiretórios\n")
                
                for diretorio in resposta[0]:
                    print(diretorio)
                
                print("")
                print("\nArquivos\n")
                d1 = resposta[1]
                for key, d1 in d1.items():
                    print(key)
                    for attribute,value in d1.items():
                        print('{}: {}'.format(attribute,value))
                    print("")
                
                time.sleep(10)
                os.system('cls')
                
            elif req == "5":
                print("\n5- Processos | PID\n")
                legenda_pid = ['Nome:', 'PID:', 'Executável:', 'CPU (s):', 'Memória (MB):']
                
                i = 0
                
                while i <= len(resposta):
                    valor_pid = [resposta[i][0], resposta[i][1], resposta[i][2], resposta[i][3], resposta[i][4]]
                    i = i + 1
                    
                    for x,y in zip(legenda_pid,valor_pid):
                        print ('{:30}{:<30}'.format(x,y))
                    print("")
                time.sleep(10)
                os.system('cls')
                
            elif req == "6":
                print("\n6- Rede\n")
                legenda_rede = ['IPv4:', 'IPv6:', 'Máscara:', 'MAC:']
                valor_rede = [resposta[0], resposta[1], resposta[2], resposta[3]]
                for x,y in zip(legenda_rede,valor_rede):
                    print ('{:30}{:30}'.format(x,y))
                time.sleep(10)
                os.system('cls')

        if req == "7":
            endereco_ip = input("Entre com o número do IP da rede: ")
            cliente.send(req.encode('utf-8'))
            cliente.send(endereco_ip.encode('utf-8'))
                
            bytes_resp = cliente.recv(quant)
            resposta = pickle.loads(bytes_resp)
            
            print("\n7- NMAP\n")
            
            d1=resposta
            for key, d1 in d1.items():
                    print(key)
                    for attribute,value in d1.items():
                        print('{}: {}'.format(attribute,value))
                    print("")

            time.sleep(15)
            os.system('cls')
                   
            legenda_nmap = ['IP (sub-rede):', 'Protocolo:', 'Porta:', 'Estado:']
                
            for key, value in resposta.items():
                valor_nmap = [resposta[key], resposta.get(key, value[0]), resposta.get(key, value[1]), resposta.get(key, value[3])]

except Exception as erro:
    print(str(erro))

cliente.close()

input("Para sair pressione qualquer tecla...")