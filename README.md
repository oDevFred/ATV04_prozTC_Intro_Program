# Calculadora com Função de Operação Matemática

Este projeto foi desenvolvido como parte do curso de Introdução à Programação oferecido pela Proz em parceria com a AWS no programa Talento Cloud. O código implementa uma calculadora que realiza operações matemáticas básicas entre dois números, com o tipo de operação definido por um terceiro parâmetro. Esse exercício fortalece o uso de funções, parâmetros e estrutura condicional em Python.

## Funcionalidade do Programa

O código solicita dois números e o tipo de operação que o usuário deseja realizar, representada por um operador matemático (`+`, `-`, `*`, `/`). A função `calculadora` então executa a operação com base nos três parâmetros:

1. `+`: Soma
2. `-`: Subtração
3. `*`: Multiplicação
4. `/`: Divisão (com verificação de divisão por zero)

Caso o operador seja inválido, a função retorna `0`, indicando um erro de operação.

### Estrutura do Código

1. **Entradas do Usuário**
   - Solicita dois números (`num1` e `num2`) e um operador (`oper`).
   
2. **Função `calculadora`**
   - Recebe três parâmetros: `numero1`, `numero2`, e `operador`.
   - Usa uma estrutura condicional para verificar o operador:
     - Retorna o resultado da operação se o operador é válido.
     - Retorna `0` se o operador é inválido.
   - Verifica também se `numero2` é zero antes de realizar uma divisão, retornando uma mensagem de erro em caso de divisão por zero.

3. **Saída do Resultado**
   - Exibe o resultado formatado ou uma mensagem de erro caso a operação não seja possível.

## Exemplo de Uso

### Entrada
```plaintext
Digite um número: 10
Digite outro número: 5
Digite o operador (+, -, *, /): *
```

### Saída
```plaintext
O resultado de 10.00 * 5.00 é: 50.00.
```

Se um operador inválido for inserido:
```plaintext
Digite um número: 10
Digite outro número: 5
Digite o operador (+, -, *, /): ^
O resultado de 10.00 ^ 5.00 é: 0.00.
```

Se tentar dividir por zero:
```plaintext
Digite um número: 10
Digite outro número: 0
Digite o operador (+, -, *, /): /
Você não pode dividir um número por 0
```

## Tecnologias e Conceitos Utilizados

- **Python**: Linguagem de programação.
- **Funções**: `def` para definir funções personalizadas.
- **Entrada e Saída de Dados**: `input()` e `print()`.
- **Estrutura Condicional**: `if-elif-else` para validação de operadores e prevenção de divisão por zero.
- **Formatação de Saída**: Formatação de valores float para exibir resultados com duas casas decimais.

## Autor

Caio Frederico, como parte do curso Talento Cloud da Proz e AWS.
