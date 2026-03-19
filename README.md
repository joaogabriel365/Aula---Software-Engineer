# Aula 2 - Software Engineer 25/02

"Eu trabalho com receitas internacionais e sempre 
preciso converter temperaturas. Às vezes a receita 
vem em Fahrenheit mas meu forno é em Celsius. 
Preciso de algo rápido que converta nos dois sentidos."

3 requisitos funcionais:

1- O sistema deve permitir a conversão de valores em Fahrenheit (°F) para Celsius (°C). Porque o usuário recebe receitas em Fahrenheit e precisa adaptar para o forno que está em Celsius. 

2- O sistema deve permitir a conversão de valores em Celsius (°C) para Fahrenheit (°F). Porque pode ocorrer a situação inversa (receita em Celsius e equipamento em Fahrenheit).

3-  O usuário deve poder digitar o valor da temperatura que deseja converter.
 Por quê? Para que ele possa converter qualquer temperatura específica de uma receita internacional.

2 requisitos não funcionais:

1-  O sistema deve apresentar o resultado imediatamente após a inserção do valor.

2- O sistema deve ter um layout fácil de usar, com poucos passos para realizar a conversão.

# Aula 3 - Software Engineer 04/03

Requisitos GymTrack:

Funcionais:

RF01: O sistema deve exibir o treino do aluno e armazenar os dados para mostrar seu progresso com o tempo

RF02: O sistema deve ter um timer integrado para marcar o tempo entre as series

RF03: o sistema deve ter um cadastro de exercícios com imagens/GIFs adicionado pelo admin

Não Funcionais:

RNF01: O sistema deve ter a interface intuitiva para que o aluno inicie seu treino em menos de 3 cliques

RNF02: O sistema deve funcionar nativamente em Android e iOS.

RNF03: O sistema deve ter os dados de saúde e treinos dos alunos devem ser criptografados

## REFLEXÃO:
### 1. Qual a diferença entre RF e RNF que você percebeu na prática?
RF define o que o sistema deve fazer, como por exemplo validar as repetições desse sistema.
RNF define como o sistema deve funcionar, como desempenho ou tempo de resposta.

### 2. O que aconteceria se esquecêssemos o RNF de performance?
O sistema poderia ficar lento e demorar para registrar os treinos

### 3. Cite 1 RNF que o GymTrack deveria ter mas que você não implementou
Um RNF que poderia existir é disponibilidade,
garantindo que o sistema esteja funcionando e acessível a qualquer momento.

# Aula 5 - Software Engineer 18/03

UC-02: Emprestar Livro

Ator: Leitor

Pré-condições:

O leitor deve estar cadastrado no sistema

O livro deve existir no sistema

O sistema deve estar disponível para operação

Fluxo Principal:

O leitor solicita o empréstimo de um livro

O sistema verifica a disponibilidade do livro (<<include>> Verificar disponibilidade)

O sistema registra o empréstimo para o leitor

O sistema confirma o empréstimo e informa a data de devolução

Fluxo de Exceção:

Se o livro não estiver disponível, o sistema informa ao leitor que o empréstimo não pode ser realizado

Se o leitor tiver pendências (ex: multa), o sistema bloqueia o empréstimo

Pós-condições:

O livro fica registrado como emprestado

O empréstimo fica associado ao leitor no sistema

Uma data de devolução é definida
