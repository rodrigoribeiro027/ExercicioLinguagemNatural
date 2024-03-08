# ExercicioLinguagemNatural
Exercício Processamento de Linguagem Natural
    
<h3>Instalação</h3>
  
Crie uma pasta e realize um clone do repositório
```
git clone https://github.com/rodrigoribeiro027/ExercicioLinguagemNatural
```


Abra sua IDE e crie o ambiente virtual Python:
```bash(ou cmd)
python3 -m venv env
```
Entrar no diretório e ativar o ambiente virtual
```
cd venv/Scripts/activate
```
Voltar no diretório do programa
```
c:\ExercicioLinguagemNatural\
```    

Atualizar o pip
```
python.exe -m pip install --upgrade pip
```    

Executar o seguinte comando para instalar as dependências necessárias.
```
pip install -r requirements.txt
```        

Rodar a aplicação
```
python exercicio.py
```

# Exercicio

PP.1.2. Exemplifique a stemização e a lematização de um texto, em língua portuguesa. Ilustre
um caso onde textos diferentes conduzem a uma mesma saída através do stemming ou
lemmazaon. Considere como saída um vetor ordenado contendo lemas e stems.  

# os textos usados
texto1 = "Eu gosto de agua"
<br/>
texto2 = "Eu gostaria de agua"
# Saida e explicações

Na stemização, a ideia é cortar pedaços do final das palavras para deixá-las mais básicas. Por exemplo, "voando" vira "voand".
<br/>
Saída do Stemming do Texto 1: ['agu', 'de', 'eu', 'gost']
<br/>
Saída do Stemming do Texto 2: ['agu', 'de', 'eu', 'gost']
_________________________________________________________________
Na lematização, a ideia é olhar para a palavra como um todo e reduzi-la à sua forma principal. Por exemplo, "voando" pode virar "voar".
<br/>
Saída da Lematização do Texto 1: ['agua', 'de', 'eu', 'gosto']
<br/>
Saída da Lematização do Texto 2: ['agua', 'de', 'eu', 'gostaria']

# Ilustre
um caso onde textos diferentes conduzem a uma mesma saída através do stemming ou
lemmazaon.

A mesma frase pode ter o mesmo resultado nas utilizaçoes porem o Sentido da frase é diferente causando incorencia nos sentidos.
<br/>
Saída do Stemming do Texto 1: ['agu', 'de', 'eu', 'gost']
<br/>
Saída do Stemming do Texto 2: ['agu', 'de', 'eu', 'gost']
______________________________________________________________________________________________________________________________
<br/>
Saída da Lematização do Texto 1: ['agua', 'de', 'eu', 'gosto']
<br/>
Saída da Lematização do Texto 2: ['agua', 'de', 'eu', 'gostaria']
