#Importando pickle
import pickle

#Iniciando função principal
def main():
    #Puxar info arquivo
    #--! pickle.load()
    #Cria uma variável com o arquivo para leitura
    archive = open("entrada.bin", 'rb')
    dictionario = pickle.load(archive)
    print(dictionario)

#Chama função principal
main()

