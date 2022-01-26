#Importando pickle
import pickle

#Iniciando função principal
def main():
    #Puxar info arquivo
    #--! pickle.load()
    #Cria uma variável com o arquivo para leitura
    archive = open("entrada.bin", 'rb')
    dictionario = pickle.load(archive)
    lista = pickle.load(archive)

    #Chama função de cálculo de notas
    listaNotas = calculoNotaTotal(dictionario, lista)
    #Debug listaNotas
    print(f'\n\nAqui:{listaNotas}')

#Calculo de notas e retorna lista
def calculoNotaTotal(dictionario, lista):
    listaAlunos = []
    for aluno in lista:
        matricula, nota1, nota2, nota3, nota4, tempo = aluno
        listaAlunos.append([matricula, nota1+nota2+nota3+nota4, tempo])

    return listaAlunos

def ordenar():
    pass




#Chama função principal
main()

