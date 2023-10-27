# Importar para CSV
import csv
from datetime import datetime

# Classe para perguntas
class Pergunta:
    def __init__(self, pergunta):
        self.pergunta = pergunta

# Classe para repostas
class Resposta:
    def __init__(self, idade, genero, respostas, nome):
        self.idade = int(idade)
        self.genero = genero
        self.respostas = respostas
        self.nome = nome
        self.data_hora = datetime.now()

# Classe para realizar enquete
class Enquete:
    def __init__(self):
        self.perguntas = [
            Pergunta("\nPergunta 1:\nVocê acredita que a polícia local está fazendo um bom trabalho na prevenção e combate ao crime?"),
            Pergunta("\nPergunta 2:\nVocê se sente seguro(a) em sua área de residência?"),
            Pergunta("\nPergunta 3:\nVocê toma medidas de segurança pessoal, como evitar andar em áreas perigosas à noite ou trancar as portas de sua casa?"),
            Pergunta("\nPergunta 4:\nVocê confia nas instituições de segurança, como a polícia e as forças armadas, para proteger a população?"),
            Pergunta("\nPergunta 5:\nVocê já participou ou consideraria participar de campanhas de conscientização e prevenção ao crime em sua cidade?"),
            Pergunta("\nPergunta 6:\nVocê ou alguém próximo a você já foi vítima de um crime nos últimos 12 meses?")
        ]
        self.respostas = []

    # Função para buscar respostas
    def extrair_resposta(self):
        print('Olá, tudo bem? Essa é uma pesquisa de satisfação sobre a segurança pública na sua cidade. (Caso não queira participar digite "00")')
        idade = input('Para iniciarmos a pesquisa, por favor, digite sua idade: ')
        if idade == '00':
            exit()
        nome = input('Me diga seu nome: ')
        if nome == '00':
            exit()
        genero = input('Agora digite seu gênero: ')
        if genero == '00':
            exit()

        # Comparativos
        respostas = []
        for pergunta in self.perguntas:
            resposta = input(f"{pergunta.pergunta}\n[ 1 ] Sim\n[ 2 ] Não\n[ 3 ] Não sei responder: ")
            if resposta in ('1', '2', '3'):
                if resposta == '1':
                    resposta = "SIM"
                elif resposta == '2':
                    resposta = "NAO"
                elif resposta == '3':
                    resposta = "NAO SEI RESPONDER"
                respostas.append(resposta)
            else:
                print('Opção inválida, tente novamente!')

        # Arquiva a resposta
        resposta = Resposta(idade, genero, respostas, nome)
        self.respostas.append(resposta)

    # Importa para o excel
    def importar_em_csv(self, nome_arquivo):
        with open(nome_arquivo, mode='a', newline='') as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                cabecalho = ["Nome", "Idade", "Genero", "Resposta 1", "Resposta 2", "Resposta 3", "Resposta 4", "Resposta 5", "Resposta 6", "Data e Hora"]
                writer.writerow(cabecalho)

            for resposta in self.respostas:
                linha = [resposta.nome, resposta.idade, resposta.genero] + resposta.respostas + [resposta.data_hora.strftime("%Y-%m-%d %H:%M:%S")]
                writer.writerow(linha)

# Criar uma instância da pesquisa
minha_pesquisa = Enquete()

# Salvar respostas em um arquivo CSV
minha_pesquisa.extrair_resposta()
minha_pesquisa.importar_em_csv('enquete.csv')
