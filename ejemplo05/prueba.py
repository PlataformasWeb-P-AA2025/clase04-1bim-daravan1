import chardet
#Prueba para verificar tipo de codificación  del csv
ruta = r'C:/Users/darav/Desktop/Plataformas/clase04-1bim-daravan1/ejemplo05/atp_tennis.csv'

with open(ruta, 'rb') as f:
    resultado = chardet.detect(f.read(10000))
    print(resultado['encoding'])
