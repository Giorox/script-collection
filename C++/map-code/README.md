# Estrutura Mapa em C++
## Construção de uma estrutura de dados associativa “mapa” utilizando a linguagem C++.

### O código:
A estrutura foi implementada usando classes e templates uma estrutura de dados mapa. A parte interna de um mapa é implementada usando hashing. A estrutura foi implementada usando uma tabela hashing com tratamento de colisão com listas encadeadas. A estrutura também contém um iterador que percorre os dados do mapa de forma ordenada da menor para a maior chave.

## Mapa

### Características:
- A estrutura mapa insere sempre um elemento usando um par (chave, valor).
- Não existe dois elementos com a mesma chave.
- A chave do mapa é sempre um inteiro ou uma string e o valor pode ser qualquer tipo de objeto.
- Para identificar o tipo da chave no template foi utilizado a função typeid.

### Operações do mapa:
- **Adicionar** um elemento no mapa: fornecendo a chave K e valor T.
   - A função verifica se já existe algum elemento com a chave K, caso já exista ela deve retorna um pair contendo o endereço de T do elemento encontrado e false, caso não tenha nenhum elemento com a chave K, o elemento é inserido no mapa e retorna um pair contendo o endereço de T do elemento inserido e true;
- **Remover** um elemento do mapa: fornecendo a chave K;
- **Pesquisa** de um elemento no mapa: fornecendo a chave K
  - A função retorna o endereço do valor T, caso encontre o elemento, e NULL caso não encontre.;
- **Iterar** sobre os elementos: Utilizando o iterador.

### O mapa tem a sobrecarga do operador “[]”:
- **[ chave ]** : Retorna o endereço do valor (objeto) do mapa caso a chave exista, caso contrário ele insere no mapa um elemento para a chave colocada (o valor é um objeto padrão “vazio”);
  - Exemplos da operação: obj=m[25]; ou cout <<m[25]; ou m[23]=obj;

## Hashing
### O hashing tem as seguintes características:
- O tamanho da tabela é 𝑀=107;
- A função de transformação é ℎ(𝑘)=𝑘 mod 𝑀;
- Os dados são armazenados nas listas encadeadas que são utilizadas no tratamento das colisões;
- Obs: As operações no mapa sempre utilizam a chave

## Iterador
### O iterador implementado utiliza uma lista encadeada onde cada célula contém o endereço de onde está armazenado os dados na hashing. O iterador tem as seguintes características:
- Uma variável que aponta sempre para o início da lista;
- Uma variável que armazena a posição atual de acesso do iterador;
- A sobrecarga do operador ++ que muda a posição atual de acesso do iterador para a próxima célula da lista do iterador;
- Ele percorre o hashing de forma ordena da menor para a maior chave;
Obs: As operações de inserção e remoção do hashing são ser refletidas no iterador.
