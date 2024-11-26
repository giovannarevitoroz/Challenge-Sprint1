# módulo importado para utilização de regex
import re

# declaração de variáveis
problema = ''
usuarioDados = []
usuarioVeiculo = []
# expressões regulares
regexCpf = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
regexTel = r'\d{2} 9\d{4}-\d{4}'
regexNome = r"^[A-Za-zÀ-ÿ'\- ]+$"
regexPlaca = r'^[A-Z]{3}-\d{1}[A-Z]{1}\d{2}$'

#peças e a disponibilidade
pecas_dados = {
    'Alinhamento': {'Braço de direção': 10, 'Terminal de direção': 3, 'Coxim do amortecedor': 0, 'Barra axial': 2},
    'Amortecedor e molas': {'Amortecedor dianteiro': 21, 'Amortecedor traseiro': 10, 'Mola dianteira': 23, 'Mola traseira': 0},
    'Ar condicionado': {'Compressor': 2, 'Condensador': 4, 'Evaporador': 6, 'Sensores de temperatura': 5},
    'Arrefecimento': {'Radiador': 10, 'Bomba de água': 20, 'Termostato': 6, 'Mangueira de radiador': 4},
    'Balanceamento': {'Pneus': 54, 'Rodas': 42, 'Contrapesos': 0, 'Porcas de fixação': 102},
    'Bateria': {'Bateria 40ah': 10, 'Bateria 60ah': 23, 'Cabos de ligação': 32, 'Cabos da bateria': 54},
    'Cambagem / caster': {'Cambagem dianteira': 10, 'Cambagem traseira': 13, 'Caster dianteiro': 32, 'Caster traseiro': 14},
    'Correias do Motor': {'Correia dentada': 2, 'Correia do alternador': 6, 'Correia da direção hidráulica': 0, 'Correia do ar condicionado': 9},
    'Freio': {'Discos de freio dianteiros': 43, 'Discos de freio traseiros': 53, 'Pastilhas de freio dianteiras': 32, 'Pastilhas de freio traseiras': 54},
    'Embreagens': {'Disco de embreagem': 5, 'Platô': 4, 'Atuador hidráulico': 10, 'Cilindro mestre': 15},
    'Filtros': {'Filtro de ar': 30, 'Filtro de óleo': 40, 'Filtro de combustível': 45, 'Filtro de cabine': 23},
    'Óleo do motor': {'Óleo lubrificante 5W-30': 32, 'Óleo lubrificante 10W-40': 24, 'Filtro de óleo': 12, 'Tampão do cárter': 12},
    'Palhetas do limpador': {'Palheta do limpador dianteiro': 10, 'Palheta do limpador traseiro':10, 'Braço do limpador dianteiro': 0, 'Braço do limpador traseiro': 0},
    'Suspensão': {'Braço oscilante': 10, 'Pivô': 21, 'Barra estabilizadora': 32, 'Batente de suspensão': 10},
    'Ignição': {'Vela de ignição': 21, 'Bobina de ignição': 32, 'Cabos de vela': 21, 'Sensor de posição': 0}
}

# preços dos serviços
servicos_preco = {'Ar-condicionado': 75, 'Arrefecimento': 100, 'Freios': 200, 'Filtros e Velas': 50, 'Balanceamento': 200, 'Alinhamento de Rodas': 75, 'Elétrica': 75}

#marcas disponiveis
marcas = {
        'Chevrolet': {'Corsa': [1995, 2002, 2009], 'Onix': [2012, 2017, 2021], 'Prisma': [2006, 2013, 2018]},
        'Ford':{'Ka': [1997, 2005, 2012], 'EcoSport': [2003, 2010, 2018], 'Focus': [1998, 2008, 2015]},
        'Honda': {'Civic': [1996, 2004, 2011], 'Fit': [2001, 2008, 2015], 'HR-V': [2014, 2017, 2020]},
        'Volkswagen': {'Gol': [1980, 1998, 2012], 'Polo': [1995, 2002, 2010], 'Jetta': [1984, 1999, 2007]},
        'Toyota': {'Corolla': [1990, 2002, 2010], 'Hilux': [1998, 2005, 2013], 'Etios': [2010, 2015, 2020]},
        'Hyundai': {'HB20': [2012, 2016, 2020], 'Tucson': [2004, 2010, 2016], 'Creta': [2014, 2018, 2022]},
        'Fiat': {'Uno': [1983, 1996, 2004], 'Argo': [2017, 2020, 2023], 'Toro': [2016, 2019, 2022]},
        'Nissan': {'March': [2002, 2010, 2018], 'Versa': [2006, 2013, 2020], 'Kicks': [2016, 2019, 2023]},
        'Jeep': {'Renegade': [2014, 2017, 2021], 'Compass': [2006, 2012, 2018], 'Grand Cherokee': [1992, 2005, 2014]},
        'Renault': {'Kwid': [2015, 2018, 2022], 'Sandero': [2008, 2014, 2019], 'Duster': [2010, 2015, 2020]}
    }
        

# cadastro do usuario
def cadastro_usuario():
    print("Iniciando cadastro do usuário...\n")
    if len(usuarioDados) > 0:
        print("Você já está cadastrado. Irei te redirecionar para o menu...")
        return
    # cadastro nome
    while True:
        nome = input("Digite o seu nome........................: ")
        if re.match(regexNome, nome) is None:
            print("Digite um nome válido.")
            continue
        else:
            usuarioDados.append(nome)
            break 
    # cadastro idade   
    while True:
        idade = input("Digite sua idade.........................: ")
        if not idade.isdigit() or int(idade) < 18:
            print("Digite uma idade válida.")
            continue
        else:
            usuarioDados.append(idade)
            break
    # cadastro CPF
    while True:
        cpf = input("Digite o seu CPF (ex: xxx.xxx.xxx-xx)....: ")
        if re.match(regexCpf, cpf) is None:
            print("Digite um CPF válido.")
            continue
        else:
            usuarioDados.append(cpf)
            break
    # cadastro endereço
    while True:
        endereco = input("Digite o seu endereço....................: ")
        if re.match(regexNome, endereco) is None:
            print("Digite um endereço válido.")
            continue
        else:
            usuarioDados.append(endereco)
            break
    # cadastro telefone
    while True:
        telefone = input("Digite o seu telefone (ex: xx xxxxx-xxxx): ")
        if re.match(regexTel, telefone) is None:
            print("Digite um número de telefone válido.")
            continue
        else: 
            usuarioDados.append(telefone)
            break
    print("\nUsuário cadastrado com sucesso!")

#cadastro do veiculo
def cadastro_veiculo():
    print("Iniciando cadastro de veículo...\n")
    if len(usuarioVeiculo) > 0:
        print("Você já possui um veículo cadastrado. Irei te redirecionar para o menu...")
        return
    # cadastro marca através de um menu
    while True:
        print("==============[ MARCA ]==============\n")
        for i in range(len(marcas)):
            print(f"{i:<2} - {list(marcas)[i]}")
        marca = input("\nSelecione a marca do seu carro...........: ")
        if not marca.isdigit() or (int(marca) > 10 or int(marca) < 0):
            print("Selecione uma opção válida.")
            continue
        else:
            marca = int(marca)
            usuarioVeiculo.append(list(marcas.keys())[marca])
            break
    # cadastro modelo através de um menu
    while True:
        print("\n==============[ MODELO ]==============\n")
        for i in range(len(marcas[usuarioVeiculo[0]])):
            print(f"{i} - {list(marcas[usuarioVeiculo[0]])[i]}")
        modelo = input("\nSelecione o modelo do seu carro..........: ")
        if not modelo.isdigit() or (int(modelo) > 2 or int(modelo) < 0):
            print("Selecione uma opção válida.")
            continue
        else:
            modelo = int(modelo)
            usuarioVeiculo.append(list(marcas[usuarioVeiculo[0]].keys())[modelo])
            break
    # cadastro do ano do veículo
    while True:
        print("\n==============[ ANO ]==============\n")
        for i in range(len(marcas[usuarioVeiculo[0]][usuarioVeiculo[1]])):
            print(f"{i} - {list(marcas[usuarioVeiculo[0]][usuarioVeiculo[1]])[i]}")
        ano = input("\nSelecione o ano do seu carro.............: ")
        if not ano.isdigit() or (int(ano) > 2 or int(ano) < 0):
            print("Selecione uma opção válida.")
            continue
        else:
            ano = int(ano)
            usuarioVeiculo.append(marcas[usuarioVeiculo[0]][usuarioVeiculo[1]][ano])
            break
    # cadastro da placa do veículo
    while True:
        placaVeiculo = input("Qual a placa do seu carro? (ex: ABC-1D23): ")
        if re.match(regexPlaca, placaVeiculo) is None:
            print("Insira um formato de placa válido.")
            continue
        else:
            usuarioVeiculo.append(placaVeiculo)
            break
    print("\nVeículo foi cadastrado com sucesso!")

# visualização das informações do usuário (Nome, Idade, CPF, endereço e telefone)
def verificar_usuario():
    print("Iniciando verificação de informações de usuário...")
    if usuarioDados == []:
        print("Você ainda não se cadastrou. Irei te redirecionar para a seção de cadastro...\n")
        cadastro_usuario()
    else:
        print("\n==============[ INFORMAÇÕES DO USUÁRIO ]==============\n") 
        print(f"Nome....: {usuarioDados[0]}") 
        print(f"Idade...: {usuarioDados[1]}") 
        print(f"CPF.....: {usuarioDados[2]}") 
        print(f"Endereço: {usuarioDados[3]}") 
        print(f"Telefone: {usuarioDados[4]}\n") 
        input("Pressione ENTER para voltar ao menu: ")
        print("Retornando ao menu principal...")

# visualização das informações do veículo (Marca, modelo, ano e placa)
def verificar_veiculo():
    print("Iniciando verificação de informações do veículo...")
    if usuarioVeiculo == []:
        print("Você ainda não cadastrou o veículo. Irei te redirecionar para a seção de cadastro...\n")
        cadastro_veiculo()
    else:
        print("\n==============[ INFORMAÇÕES DO VEÍCULO ]==============\n") 
        print(f"Marca.....: {usuarioVeiculo[0].capitalize()}") 
        print(f"Modelo....: {usuarioVeiculo[1]}") 
        print(f"Ano.......: {usuarioVeiculo[2]}") 
        print(f"Placa.....: {usuarioVeiculo[3]}\n")
        input("Pressione ENTER para voltar ao menu: ")
        print("Retornando ao menu principal...")

# pré-diagnóstico básico, apenas com if e palavras-chave
def auto_diagnostico():
    print("\nIniciando autodiagnóstico...")
    while True:
        problema = (input("\nQual o problema enfrentado no carro?: ")).lower()
        if 'ar-condicionado' in problema or 'ar condicionado' in problema or 'gelando' in problema or 'esfriando' in problema:
            print("\nO problema apresentado está relacionado a alguma peça do ar-condicionado.")
            problema = 'Ar-condicionado'
            return problema
        elif 'superaquecimento' in problema or 'motor' in problema:
            print("\nO problema apresentado está relacionado ao sistema de arrefecimento, possivelmente afetado por uma falha na bomba d'água ou vazamento no radiador.")
            problema = 'Arrefecimento'
            return problema
        elif 'freio' in problema or 'frear' in problema or 'freiar' in problema or 'frenagem' in problema:
            print("\nO problema apresentado está relacionado aos discos e pastilhas de freio.")
            problema = 'Freios'
            return problema
        elif 'devagar' in problema or 'lento' in problema or 'potência' in problema or 'aceleração' in problema:
            print("\nO problema apresentado está relacionado ao desempenho do motor, possivelmente afetado por problemas de filtragem ou falhas nas velas de ignição.")
            problema = 'Filtros e Velas'
            return problema
        elif 'volante' in problema or 'tremer' in problema or 'tremendo' in problema or 'vibração' in problema or 'vibrando' in problema or 'pneu' in problema or 'roda' in problema:
            print("\nO problema apresentado está relacionado ao balanceamento das rodas.")
            problema = 'Balanceamento'
            return problema
        elif 'desalinhado' in problema or 'puxando' in problema or 'volante desalinhado' in problema:
            print('\nO problema apresentado está relacionado ao desalinhamento das rodas.')
            problema = 'Alinhamento de Rodas'
            return problema
        elif 'não liga' in problema or 'partida' in problema or 'luz fraca' in problema or 'elétrica' in problema:
            print("\nO problema apresentado está em alguma parte elétrica do carro (bateria, cabos, ignição)")
            problema = 'Elétrica'
            return problema
        elif 'óleo' in problema or 'nível de óleo baixo' in problema or 'vazamento' in problema:
            print("\nO problema apresentado está relacionado ao óleo do motor do carro.")
            problema = 'Óleo do Motor'
            return problema
        else:
            print("Problema não registrado.")
            continue

# auto-orçamento com base no pré-diagnóstico
def auto_orcamento():
    print("\nIniciando autoorçamento...")
    while True:
        # o autoorçamento só será feito caso o problema tenha sido descoberto no pré-diagnóstico.
        if not problema:
            print("Você não realizou um autodiagnóstico ainda. Irei te redirecionar para realizar um.")
            auto_diagnostico()
            break
        for servico, preco in servicos_preco.items():
            if servico == problema:
                print("\n==============[ ORÇAMENTO ]==============\n")
                print(f"Problema...........: {servico}")
                print(f"Preço do serviço...: R${preco:.2f}")
                input("\nPressione ENTER para voltar ao menu: ")
                print("Retornando ao menu principal...")
        break


# verificar a disponibilidade de determinada peça
def disponibilidade_pecas():
    print("Iniciando verificação da disponibilidade de peça...")
    while True:
        print("\n==============[ CONJUNTOS ]==============\n")
        for i in range(len(pecas_dados)):
            print(f"{i+1:<2d} - {list(pecas_dados)[i]}")
        print("0  - Sair\n")
        option_pecas = input("Selecione um dos conjuntos para continuar: ")
        if not option_pecas.isdigit() or (int(option_pecas) > 15 or int(option) < 0):
            print("\nSelecione uma opção válida.")
            continue
        option_pecas = int(option_pecas)
        if option_pecas == 0:
            print("Retornando ao menu principal...")
            break
        if 1 <= option_pecas <= 15:
            i = option_pecas - 1
            # obtem a chave da opção selecionada
            chave = list(pecas_dados.keys())[i]
            # imprime o conjunto selecionado e as peças, juntamente com a quantidade disponível
            print(f"\n==============[ PEÇAS - {chave.upper()} ]==============\n") 
            for peca, disponivel in pecas_dados[chave].items():
                if disponivel == 0:
                    print(f"{peca:<30} - {'Peça indisponível'}")
                elif disponivel == 1:
                    print(f"{peca:<30} - {disponivel:>2} disponível")
                else:
                    print(f"{peca:<30} - {disponivel:>2} disponíveis")
        input("\nPressione ENTER para voltar ao menu de peças: ")
        print("Retornando ao menu de peças...")

# menu inicial
while True:
    print("\n==============[ MENU ]==============\n")
    print("1 - Cadastro Usuário")
    print("2 - Cadastro Veículo")
    print("3 - Verificar informações de usuário")
    print("4 - Verificar informações do veículo")
    print("5 - Autodiagnóstico")
    print("6 - Auto orçamento")
    print("7 - Disponibilidade de peças")
    print("0 - Sair\n")
    option = input("Opção: ")
    if not option.isdigit() or (int(option) > 7 or int(option) < 0):
        print("Selecione uma opção válida.")
        continue
    option = int(option)
    if option == 0:
        print("\nSolicitação encerrada.\n")
        break
    elif option == 1:
        cadastro_usuario()
    elif option == 2:
        cadastro_veiculo()       
    elif option == 3:
        verificar_usuario()
    elif option == 4:
        verificar_veiculo()
    elif option == 5:
        problema = auto_diagnostico()
    elif option == 6:
        auto_orcamento()
    elif option == 7:
        disponibilidade_pecas()