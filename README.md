## MaxMin Select por divisão e conquista

### Descrição do projeto

O projeto utiliza a estratégia de divisão e conquista para auxiliar o Select Sort. 
Assim, o código é composto por de três partes: 

#### Função recSelectionSort

Entrada: 
    - Lista: O array de inteiros que será arrumado.
    - Iterador I.
    - Iterador J. 

Retorno: 
    - A função retorna o menor valor entre o na posição i e o da posição k.

Nessa função, o valor de i é incrementado, de forma que o valor na posição i é comparado com o valor na posição k, um valor obtido pelo uso recursivo da função. 

O objetivo dessa função é auxiliar a função principal, a selectionSort

#### Função selectionSort 

Entrada: 
    - lista: O array de inteiros que será arrumado.
    - n: O tamanho desse array.
    - index: O indice a ser comparado para fazer a comparação.

O objetivo dessa função é a organização da lista, do menor para o maior, de forma recursiva. 

#### Corpo do código

Aqui, a lista é definida e depois imprimida para demonstração da função. 

### Como executar o projeto

1. Instalar o python na máquina

2. Navegar, pelo terminal, até a pasta do projeto

3. Inserir o valor desejado na lista na linha 28

4. Rodar o arquivo com "python3 main.py"

### Relatório Técnico 

Numero de loops ou entradas recursivas: 
    selectionSort: n.
    recSelectionSort: j (que no pior caso é n).

Numero de operações: 
    selectionSort: 4
    recSelectionSort: 2

O(4n*2n)
O(8n²)


Fontes: https://www.gatevidyalay.com/tag/selection-sort-using-divide-and-conquer/