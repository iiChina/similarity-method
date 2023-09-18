# Strike a Match Algorithm

Este site é um artigo que explica um algoritmo de comparação de similaridade entre duas strings, chamado de "Strike a Match". O algoritmo é baseado na contagem de pares de caracteres comuns entre as strings, dividindo o tamanho da interseção pelo tamanho médio dos conjuntos de pares. O algoritmo é capaz de reconhecer a similaridade lexical, a robustez à mudança de ordem das palavras e a independência da língua.

## Fórmula do algoritmo

- similarity(text1, text2) = (2 x intersection) / bigramText1 + bigramText2

## Lógica do algoritmo

O algoritmo funciona da seguinte forma:

- Primeiro, ele divide cada string em um conjunto de pares de caracteres adjacentes. Por exemplo, a string "FRANCE" seria dividida em {"FR", "RA", "AN", "NC", "CE"}.
- Segundo, ele calcula a interseção entre os dois conjuntos, ou seja, os pares de caracteres que são comuns às duas strings. Por exemplo, a interseção entre "FRANCE" e "FRENCH" seria {"FR", "NC"}.
- Terceiro, ele divide o tamanho da interseção pelo tamanho dos dois conjuntos, obtendo um valor entre 0 e 1 que representa a similaridade entre as strings. Quanto maior o valor, mais similares são as strings. Por exemplo, a similaridade entre "FRANCE" e "FRENCH" seria (2 * 2) / 10  = 0.4.

## Comparação com outros métodos

O autor também compara o algoritmo com outros métodos existentes, como o Soundex, a Distância de Edição e a Maior Substring Comum, mostrando as vantagens e desvantagens de cada um. Ele conclui que o algoritmo "Strike a Match" é simples, mas eficaz para comparar strings que têm palavras parecidas, mas não idênticas. Ele também é capaz de lidar com mudanças na ordem das palavras e diferenças linguísticas. O autor mostra exemplos de como o método funciona com strings em inglês, francês, espanhol e português.

## Referências
- http://www.catalysoft.com/articles/StrikeAMatch.html
