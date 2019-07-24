# Documentação

![](https://storage.googleapis.com/typewriter/typewriter.jpg)

Projeto de Bloco - Arquitetura de Computadores, Sistemas Operacionais e Redes

Instituto Infnet - ESTI - Engenharia da Computação

Prof. Cassius Figueiredo

***

### Desenvolvimento
**Etapa 1 – Seleção das funções:**

Para obter as informações da máquina servidora foram utilizadas as seguintes bibliotecas externas no compilador Thonny junto com as bibliotecas nativas do Python para maior suporte: 
* psutil (v 5.5.0) [1]
* Py-cpuinfo (v 3.2.0) [2]
* nmap (v 0.6.1) * [3] 
* datetime, os, pickle, platform, socket, subprocess e time (nativos do Python)

*: Para suporte à biblioteca nmap foi utilizado o software nmap (v 7.7.0) [4] no sistema operacional Windows 10 (64 bits).

Devido ao fato de que cada biblioteca externa é utilizada no desenvolvimento de aplicações em diversos sistemas operacionais e cada sistema fornecer seu próprio nível de acesso, características distintas e quantidade variável de informações disponíveis para coleta, houve a necessidade de um levantamento completo de cada ferramenta disponível em cada biblioteca externa para o sistema que foi feito o desenvolvimento da aplicação, no caso Windows, sistema operacional de código fonte fechado. Por se tratar de um sistema com acesso mais restrito que o Linux / UNIX, a quantidade de informação disponível foi mais limitada, porém não apareceu um agravante visto que as informações básicas de monitoramento de recursos estavam disponíveis. 

![](https://storage.googleapis.com/typewriter/figura_1.jpg)
> Figura 1: Levantamento de informações para função do Processador.

![](https://storage.googleapis.com/typewriter/figura_2.jpg)
> Figura 2: Levantamento de informações para função do Disco Rígido.


***

**Etapa 2 – Teste das funções:**

Máquina de teste 1:
* Processador: Intel Core i7-7500U (Base: 2.90 GHz / Testes: 3.5 GHz)
* Memória RAM: 8 GB / 2133 MHz / SODIMM 
* Armazenamento: SanDisk Ultra II (SSD)
* Rede Ethernet: Realtek PCIe GBE Family Controller
* Rede Wireless: Qualcomm Atheros QCA9377

Máquina de teste 2:
* Processador: Intel Core i7-7700 (Base: 3.60 GHz)
* Memória RAM: 8 GB 

Máquina de teste 3:
* Processador: AMD A6-3500
* Memória RAM: 8 GB 

O projeto começou a tomar forma com a seleção das funções feita previamente, o que demorou tempo, porém resultou em um foco maior em quais funções realmente deveriam ser abordadas na aplicação para que fosse funcional e realmente útil o resultado apresentado para o usuário. 

Foi decidido que iniciariam os testes apenas com resultado no Cliente, buscando informações do próprio computador para facilitarem os testes e resolverem possíveis erros. Sem dúvida não foram utilizadas todas as funções levantadas na Etapa 1 visto que seu número é consideravelmente grande e por possuir funções que não são relevantes para um servidor – E.g.: função para medição de temperatura da bateria (notebook) – o que resultou em uma gama de funções ainda mais estrita. 
Houveram funções – E.g.: tempo gasto pelo processador em interrupções e DPC, estatística de I/O do disco rígido, quantidade de bytes escritos e lidos, tipo de conexão do NIC – que poderiam ter sido implementadas, porém foram cortadas para manter a essência da aplicação que seria o simples monitoramento dos recursos de um sistema computacional remoto. Da mesma forma, funções que não funcionaram como esperado ou houveram divergência de execução nas máquinas que foram feitos os testes foram retiradas também.

Os testes se resumiram à coleta de uma determinada informação e a impressão dela no console do compilador. Os recursos monitorados foram separados em projetos específicos para testes unitários de cada recurso e suas respectivas funções, após foram testados como um todo e assim reuniram-se todos as áreas monitoradas para verificar a execução em conjunto e continuar a implementação. 
Houveram resultados que são retornados por meio de listas e dicionários e para isso sua manipulação foi feita para extração de uma ou mais informação(ões) que entraria(m) no projeto final. 

![](https://storage.googleapis.com/typewriter/figura_3.jpg)
> Figura 3: Teste do recurso Processador.


***

**Etapa 3 – Implementação:**

Foram separados os projetos, o Servidor é agora responsável apenas pela captura das informações dos seus recursos e envio do conjunto de dados (brutos) através de lista ou dicionário (dependendo do recurso escolhido) para o Cliente com a conversão desses objetos retornados pela função do recurso em bytes, permitido com a utilização da biblioteca nativa do Python chamada “pickle” que realiza essa conversão para assim ser possível enviar esse objeto agora em bytes pela conexão criada pela biblioteca nativa do Python definida por “socket” que realiza esta comunicação entre os dois lados sob o protocolo escolhido que foi o TCP. O Cliente é responsável pelo recebimento do pacote de resposta ainda em bytes e a mesma biblioteca “pickle” citada previamente realiza a conversão de bytes para o objeto gerado pela função no servidor. O cliente processa a lista ou dicionário recebido, formata a resposta e imprime-a no meio de apresentação, podendo ser compilador, CMD ou Power Shell no Windows.

Nesta Etapa ocorreu a criação do código para conexão entre o Cliente e Servidor. Foram feitos para ambos protocolos TCP e UDP, porém escolhido o TCP por sua confiabilidade na entrega da informação. Houveram as avaliações de performance embora o UDP seja mais rápido. Para pacotes de até 32 kilobyte (KB) foi tomado por base indiferente a performance dos protocolos, o que resultou na escolha de um protocolo mais confiável com o TCP. Não houve problema na criação do socket.
A maior dificuldade na parte de formatação foi extrair da resposta os resultados, visto que algumas respostas vinham como lista, porém com outra lista e um dicionário dentro.

Funções como limpeza da tela através do comando “cls” na CMD tiveram que ser implementadas junto à utilização da biblioteca nativa do Python “time” com a função “time.sleep(tempo em segundos)” para aparecer na tela o resultado e aguardar alguns segundos para limpar a tela e mostrar o menu novamente, pois aparecia a informação e a tela era limpa em seguida, para evitar maiores problemas com implementação de alguma tecla, foi escolhido manter a função “time” para resolver o  problema.

![](https://storage.googleapis.com/typewriter/figura_4.jpg)
> Figura 4 (Cliente): Tentativa de conexão com servidor, envio da requisição, recebimento da resposta, decodificação do pacote de resposta, formatação e impressão da resposta.

![](https://storage.googleapis.com/typewriter/figura_5.jpg)
> Figura 5 (Servidor): Recebimento da requisição, análise do número escolhido, chamada da função que retornará o uso do recurso desejado, conversão para bytes da resposta e envio para o Cliente.


***

### Recursos

Detalhamento e interpretação dos resultados gerados por cada função do projeto. Cada item corresponde a uma requisição de determinado recurso do servidor. Cada subitem corresponde ao que essa requisição irá retornar para o cliente.

**1. Processador:**

![](https://storage.googleapis.com/typewriter/1.png)

1.1 Modelo: Retorna a fabricante, modelo, frequência base anunciada.

1.2 Arquitetura: Retorna o tipo de arquitetura do processador.

1.3 Palavra: Retorna à quantidade de palavras que é processado em conjunto em um sistema computacional. E.g.: Um processador com palavra no valor de 64 bits consegue processar 8 palavras por vez, visto que uma palavra possui 8 bits (64 / 8 = 8).

1.4.	Frequência média: No momento da execução da função do processador ocorrem dez coletas da frequência atual do processador com intervalos de um segundo entre elas, depois uma média é feita e gerado o valor da frequência média em Giga-hertz (GHz).

1.5.	Uso: No momento da execução da função do processador ocorrem dez coletas da porcentagem de uso do processador com intervalos de um segundo entre elas, depois uma média é feita e gerado o valor do uso médio em porcento (%). 

1.6.	Uso núcleos: Retorna o uso em porcento de cada núcleo do processador. 

1.7.	Núcleos Físicos: Retorna quantidade de núcleos físicos do processador.

1.8.	Núcleos Lógicos: Retorna quantidade de núcleos lógicos do processador.

**2. Memória:**

![](https://storage.googleapis.com/typewriter/2.png)

2.1 RAM total: Retorna à quantidade de memória total do sistema computacional em gigabyte (GB).
 
2.2 RAM disponível: Retorna à quantidade de memória disponível do sistema computacional em gigabyte (GB). 

2.3 RAM uso: Retorna à quantidade de memória em uso do sistema computacional em gigabyte (GB). 

2.4 Swap total: Retorna à quantidade de memória swap total do sistema computacional em gigabyte (GB). 

2.5 Swap disponível: Retorna à quantidade de memória swap disponível do sistema computacional em gigabyte (GB). 

**3. Armazenamento:**

![](https://storage.googleapis.com/typewriter/3.png)

3.1. Total: Retorna à quantidade de armazenamento total na partição corrente do sistema computacional em gigabyte (GB).
 
3.2. Livre: Retorna à quantidade de armazenamento disponível na partição corrente do sistema computacional em gigabyte (GB). 

3.3. Utilizado: Retorna à quantidade de armazenamento utilizado na partição do sistema operacional em forma de percentual.

**4. Arquivos**

![](https://storage.googleapis.com/typewriter/4.png)

4.1. Tamanho: Retorna o tamanho do arquivo em bytes no diretório corrente.

4.2. Caminho: Retorna o caminho que o arquivo está localizado.

4.3. Criação: Retorna a data de criação do arquivo.

4.4. Modificação: Retorna a última data de modificação do arquivo. 

4.5. Último acesso: Retorna a data do último acesso ao arquivo. 

**5. Processos**

![](https://storage.googleapis.com/typewriter/5.png)

5.1. PID: Retorna o número identificador do processo no sistema operacional. 

5.2. Executável: Retorna o caminho absoluto do executável do processo.

5.3. CPU: Retorna em segundos a quantidade de tempo que o processador gastou realizando o processamento desse processo criado pelo usuário. 

5.4. Memória: Retorna à quantidade em megabyte (MB) de memória que o processo utilizou. 

**6. Rede**

![](https://storage.googleapis.com/typewriter/6.png)

6.1. IPv4: Retorna o IP do servidor no formato IPv4.

6.2. IPv6: Retorna o IP do servidor no formato IPv6.  

6.3. Máscara: Retorna a máscara que o servidor está utilizando. 

6.4. MAC: Retorna o endereço MAC do servidor. 

**7. Nmap**

![](https://storage.googleapis.com/typewriter/7.png)

7.1. IP (sub-rede): Retorna o IP da sub-rede.

7.2. Protocolo: Retorna o protocolo da conexão (E.g.: TCP ou UDP).

7.3. Porta: Retorna o número da Porta.

7.4. Estado: Retorna o estado da porta, ‘open’ (aberta) ou ‘closed’ (fechada).


***

### Conclusão

Muitas dificuldades surgiram, dentre elas a limpeza da tela e posteriormente a exibição dinâmica do menu após resposta da requisição. A principal dificuldade foi com o nmap, onde problemas inesperados aconteceram na parte de execução dos testes. Porém obtivemos pontos positivos, como a experiência adquirida ao lidar com tais situações, onde foi necessário pensar em uma outra abordagem para resolver o erro que apresentava no compilador Thonny. O segundo ponto foi o aprendizado que cada integrante obteve ao longo do processo. Para finalizar, o terceiro ponto foi a qualidade dos resultados obtidos que pode manter a essência do projeto de uma aplicação simples de monitoramento de recursos de um sistema operacional.  

### Referências

1. [https://psutil.readthedocs.io/en/latest/](https://psutil.readthedocs.io/en/latest/)
2. [https://github.com/workhorsy/py-cpuinfo](https://github.com/workhorsy/py-cpuinfo)
3. [https://xael.org/norman/python/python-nmap/](https://xael.org/norman/python/python-nmap/)
4. [https://nmap.org/man/pt_BR/](https://nmap.org/man/pt_BR/)

### Glossário

Bit(s): Menor unidade de informação que pode ser armazenada ou transmitida.

Byte(s): Conjunto estruturado de dados formado por uma sequência ordenada de oito bits.

Bytes escritos: Quantidade de bytes que são escritos em disco em determinado intervalo de tempo.

Bytes lidos: Quantidade de bytes que são lidos em disco em determinado intervalo de tempo.

Cliente: Máquina com perfil ativo que envia solicitações para realização de processos em um sistema computacional com perfil passivo (servidor).

Cliente-Servidor: Arquitetura baseada em um computador (cliente) que envia requisições para serem processadas em outro computador (servidor) e espera receber uma resposta de volta. Geralmente referenciada como um computador pessoal que envia requisições para um conjunto computacional processá-las e retorná-las como resposta para o computador de origem. 

CMD: Interpretador de linha de comando utilizado no sistema operacional Windows. 

Compilador: Programa de computador que a partir de um código em determinada linguagem de programação compilada gera um programa semanticamente equivalente, porém em outra linguagem, código objeto.

Dicionário: Estrutura de armazenamento da linguagem Python, baseada em uma chave referenciando a um item e um valor que pode ser unitário ou outra estrutura de armazenamento (outro dicionário, lista, tupla).

DPC (Deferred Procedure Call): Mecanismo do Sistema operacional Windows que permite que tarefas de alta-prioridade adiem tarefas necessárias com prioridade baixa para execução posterior.  

Giga-hertz: Equivale a 1.000.000.000 hertz.

I/O: Da computação Input/Output.

Interrupções de hardware: Sinal resultante da troca de contexto de um dispositivo. 

Kilobyte: Equivalente a 1.000 bytes.

Lista: Estrutura de armazenamento da linguagem Python, baseada em posições onde cada posição pode ser apenas um valor unitário ou outra estrutura de armazenamento (outra lista, dicionário, tupla).

NIC (Network Interface Card – “Placa de Rede”): Hardware presente em um sistema computacional que é responsável pela comunicação entre o computador e uma rede de computadores (E.g.: Internet).

Power Shell: Ferramenta multiplataforma disponível no Windows e voltada para automação e configuração do sistema por meio de scripts (códigos).

Processador: Circuito integrado que realiza as funções de cálculo e tomada de decisão de um computador.

TCP (Transmission Control Protocol): Conjunto de protocolos de comunicação entre computadores em rede. 

UDP (User Datagram Protocol): Protocolo de transferência de dados da camada de transporte.

Windows: Formalmente chamado de Microsoft Windows. Sistema operacional desenvolvido pela empresa norte-americana Microsoft Corporation.
