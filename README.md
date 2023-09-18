# Strike a Match Algorithm

É um algoritmo de comparação de similaridade entre duas strings, chamado de "Strike a Match". O algoritmo é baseado na contagem de pares de caracteres comuns entre as strings, dividindo o tamanho da interseção pelo tamanho dos conjuntos de pares. O algoritmo é capaz de reconhecer a similaridade lexical, a robustez à mudança de ordem das palavras e a independência da língua.

## Requisitos

- **Um verdadeiro reflexo da similaridade lexical** – strings com pequenas diferenças devem ser reconhecidas como semelhantes. Em particular, uma sobreposição significativa de substrings deve apontar para um alto nível de similaridade entre as strings.

- **Robustez às mudanças na ordem das palavras** - duas cadeias que contêm as mesmas palavras, mas em ordem diferente, devem ser reconhecidas como semelhantes. Por outro lado, se uma string for apenas um anagrama aleatório dos caracteres contidos na outra, então ela deverá (geralmente) ser reconhecida como diferente.

- **Independência de idioma** – o algoritmo deve funcionar não apenas em inglês, mas em muitos idiomas diferentes.

## Fórmula do algoritmo

- similarity(text1, text2) = (2 x intersection) / bigramText1 + bigramText2

## Lógica do algoritmo

- Primeiro, divide cada string em um conjunto de pares de caracteres adjacentes. Por exemplo, a string "FRANCE" seria dividida em {"FR", "RA", "AN", "NC", "CE"}.
- Segundo, calcula a interseção entre os dois conjuntos, ou seja, os pares de caracteres que são comuns às duas strings. Por exemplo, a interseção entre "FRANCE" e "FRENCH" seria {"FR", "NC"}.
- Terceiro, divide o tamanho da interseção pelo tamanho dos dois conjuntos, obtendo um valor entre 0 e 1 que representa a similaridade entre as strings. Quanto maior o valor, mais similares são as strings. Por exemplo, a similaridade entre "FRANCE" e "FRENCH" seria (2 * 2) / 10  = 0.4.

## Referências
- http://www.catalysoft.com/articles/StrikeAMatch.html
