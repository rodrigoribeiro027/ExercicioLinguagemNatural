import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import RSLPStemmer, WordNetLemmatizer

nltk.download('punkt')
nltk.download('rslp')
'''PP.1.2. Exemplifique a stemização e a lematização de um texto, em língua portuguesa. Ilustre
um caso onde textos diferentes conduzem a uma mesma saída através do stemming ou
lemmazaon. Considere como saída um vetor ordenado contendo lemas e stems.  '''

#Na stemização, a ideia é cortar pedaços do final das palavras para deixá-las mais básicas. Por exemplo, "voando" vira "voand".

def stem_text(texto):
    stemmer = RSLPStemmer()
    tokens = word_tokenize(texto.lower())
    stems = [stemmer.stem(token) for token in tokens]
    return sorted(set(stems))

#na lematização, a ideia é olhar para a palavra como um todo e reduzi-la à sua forma principal. Por exemplo, "voando" pode virar "voar".
def lematizar_texto(texto):
    lematizador = WordNetLemmatizer()
    tokens = word_tokenize(texto.lower())
    lemas = [lematizador.lemmatize(token) for token in tokens]
    return sorted(set(lemas))


texto1 = "Eu gosto de agua"
texto2 = "Eu gostaria de agua"
#gostaria de falar que a mesma frase pode ter o mesmo resultado nas utilizaçoes porem o Sentido da frase é diferente causando incorencia nos sentidos.
saida_stem_texto1 = stem_text(texto1)
saida_stem_texto2 = stem_text(texto2)

saida_lematizada_texto1 = lematizar_texto(texto1)
saida_lematizada_texto2 = lematizar_texto(texto2)

print("Saída do Stemming do Texto 1:", saida_stem_texto1)
print("Saída do Stemming do Texto 2:", saida_stem_texto2)
print("______________________________________________________________________________________________________________________________")
print("Saída da Lematização do Texto 1:", saida_lematizada_texto1)
print("Saída da Lematização do Texto 2:", saida_lematizada_texto2)
print('adawda'  +nltk.__version__)
