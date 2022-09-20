## Projeto em Python para saber quem está de plantão

---
<br>

### Sobre o Projeto:
- O projeto se encontra em fase de 'teste', com alguns bugs. E será melhorado com o tempo.

<br>

> Alimentação da ferramenta:
- Este projeto vai trabalhar com dados que será adicionado pelo usuário final. <br>
  O usuário pode informar 1 mês inteiro (sobre quem é os plantonistas e de quantos dias cada um vai atuar)

> Visão do Usuário Final:
- Será mostrado quem está de plantão no dia atual (teria como ver por semana ou o mês)

<br>

---
<br>

### Futuro:
- Fazer disparar mensagens para telegram comunicando quem está de plantão no dia atual.
- Poderia ter uma front para que o usuário passe as informações...
- Fazer a utilização de banco de dados

<br>

---
<br>

### TO DO:
- Fazer melhorias no código (Passar blocos lógicos para métodos, fazer o uso das classes...)
- Fazer documentação do Projeto
- Pensar nas formas de interação do cliente, para obter os resultados dinâmicos
- Verificar de trazer quem está de plantão no dia atual como default (ter opção de ver o inicio e o final do plantão da pessoa)
- Passar classes 'Distribuição Detalhada' e 'Distribuição Genérica' para Design Pattern (Strategy) pois não está seguindo conceito SOLID (Open-Closed Principle)


<br>

---
<br>

### Exemplo de dados (JSON):
```json
[
  {
    "mes": 8,
    "tipo-distribuicao": "generico",
    "revezamento-por-dias": 3,
    "quem-inicia-o-mes": {
        "nome": "Willian2",
        "telefone": "12345678902",
        "qtd-dias": 1
    },
    "plantonistas": [
      {
        "nome": "Willian1",
        "telefone": "12345678901"
      },
      {
        "nome": "Willian2",
        "telefone": "12345678902"
      },
      {
        "nome": "Willian3",
        "telefone": "12345678903"
      },
      {
        "nome": "Willian4",
        "telefone": "12345678904"
      },
      {
        "nome": "Willian5",
        "telefone": "12345678905"
      }
    ]
  },
  {
    "mes": 9,
    "tipo-distribuicao": "detalhado",
    "revezamento-por-dias": 0,
    "quem-inicia-o-mes": [],
    "plantonistas": [
      {
        "nome": "Willian1",
        "telefone": "12345678901",
        "dias-do-plantao": [1,2,3,16,17,18]
      },
      {
        "nome": "Willian2",
        "telefone": "12345678902",
        "dias-do-plantao": [4,5,6,19,20,21]
      },
      {
        "nome": "Willian3",
        "telefone": "12345678903",
        "dias-do-plantao": [7,8,9,22,23,24]
      },
      {
        "nome": "Willian4",
        "telefone": "12345678904",
        "dias-do-plantao": [10,11,12,25,26,27]
      },
      {
        "nome": "Willian5",
        "telefone": "12345678905",
        "dias-do-plantao": [13,14,15,28,29,30]
      }
    ]
  }
]
```

