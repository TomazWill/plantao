## Projeto em Python para saber quem está de plantão

---
<br>

### Sobre o Projeto:
- O projeto ainda precisa passar por várias melhorias. <br>
  Ele se encontra em 'fase de esboço', com muitos bugs 😅... <br>
  Dedicarei um tempo para resolvê-los e melhorar o funcionamento do projeto! 😉

<br>

> Como será a alimentação da ferramenta:
- Este projeto vai trabalhar em cima de dados que será adicionado pelo usuário final. <br>
  O usuário pode informar 1 mês fechado (sobre quem é os plantonistas e de quantos dias cada um vai atuar)

> Como ficaria para o usuário final:
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

