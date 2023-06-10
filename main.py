import pandas as pd
import numpy as np

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from utils.connection_database import connect

# Conexão com o banco pela funcao connect()
con = connect()

# Leitura dos dados
data = pd.read_sql('SELECT * FROM ag002.`breast-cancer`;', con)

# Decision tree
tree = DecisionTreeClassifier()

# Separando metricas de treinamento e de teste
x = data.loc[:, ['age', 'menopause', 'tumor-size', 'inv-nodes', 'node-caps', 'deg-malig', 'breast', 'breast-quad', 'irradiat']]
x = np.array(x)

y = data['class']
y = np.array(y)

# Separando treino e teste
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
print('\nMETRICAS: ')
print(f'Tamanho x de treino: {x_train.shape}')
print(f'Tamanho x de teste: {x_test.shape}')
print(f'Tamanho y de treino: {y_train.shape}')
print(f'Tamanho y de teste: {y_test.shape}')

# treinando modelo
tree.fit(x_train, y_train)

tree_predict = tree.predict(x_test)

avaliacao = accuracy_score(y_test, tree_predict)

print(f'\nAVALIACAO: {round(avaliacao * 100, 2)}%')

# input dos dados
data = [input('\nIDADE: '), input('MENOPAUSA: '), input('DIAMETRO DO TUMOR: '), input('LINFONODO AXILAR: '),
        input('PENETRAÇÃO DO TUPOS NA CAPSULA DO LINFONODO: '), input('GRAU DE MALIGNIDADE: '), input('MAMA: '),
        input('QUADRANTE DA MAMA AFETADO: '), input('RADIOTERAPIA: ')]

data_test = np.array([data, ])

tree_predict_data = tree.predict(data_test)

if tree_predict_data == 2:
    print('\nSIM')
elif tree_predict_data == 1:
    print('\nNÃO')
else:
    print('SOLUÇÃO NÃO DETERMINADA')


