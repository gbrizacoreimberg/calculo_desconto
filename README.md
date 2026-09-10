# Calculadora de Desconto

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python\&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Projeto-black?logo=github)

## Sobre o projeto:

Este projeto é uma **Calculadora de Desconto**, desenvolvida em **Python** 🐍.
O programa solicita ao usuário o **valor da compra** e, de acordo com o valor informado, calcula automaticamente a **porcentagem de desconto**, o **valor do desconto em reais** e o **valor final a ser pago**.

## Objetivo:

Esse projeto é um trabalho que fiz para meu curso, como forma de aprendizado da linguagem **Python**, principalmente sobre o uso de **variáveis, entrada de dados, estruturas condicionais (`if`, `elif` e `else`) e cálculos matemáticos**.

O projeto também faz parte do meu aprendizado sobre o uso do **Git e GitHub** para versionamento e organização de projetos.

## Regras de desconto:

O programa aplica diferentes porcentagens de desconto de acordo com o valor da compra:

| Valor da compra            | Desconto |
| -------------------------- | -------: |
| Menor que R$ 200,00        |       5% |
| De R$ 200,00 até R$ 299,99 |      10% |
| R$ 300,00 ou mais          |      15% |

## Fórmulas utilizadas nos cálculos:

```text
Valor do desconto = Valor da compra × Percentual de desconto ÷ 100
```

### Onde:

* **Valor da compra** = valor total da compra informado pelo usuário.
* **Percentual de desconto** = desconto aplicado de acordo com o valor da compra.
* **Valor do desconto** = valor economizado pelo cliente.

Depois, o programa calcula o valor final:

```text
Valor final = Valor da compra - Valor do desconto
```

### Onde:

* **Valor final** = valor que o cliente deverá pagar após a aplicação do desconto.

## Exemplo:

Considere uma compra no valor de **R$ 300,00**:

```text
Valor da compra = R$ 300,00
Percentual de desconto = 15%

Valor do desconto = 300 × 15 ÷ 100
Valor do desconto = R$ 45,00

Valor final = 300 - 45
Valor final = R$ 255,00
```

Resultado:

```text
Porcentagem de desconto: 15%
Valor do desconto em reais: R$ 45.00
Valor final a ser pago: R$ 255.00
```

## Como executar:

### 1. Instale o Python

É necessário ter o **Python 3** instalado em seu computador para executar o programa.

### 2. Abra a pasta do projeto

Abra o terminal na pasta do projeto, onde estão os arquivos `app.py` e `README.md`.

### 3. Execute o programa

No terminal, utilize o comando:

```bash
python app.py
```

Após executar o comando, o programa solicitará o **valor da compra** e calculará automaticamente o desconto e o valor final a ser pago.

## Tecnologias utilizadas:

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="40" alt="Python">

## Autora

**Giovana Brizaco Reimberg**
