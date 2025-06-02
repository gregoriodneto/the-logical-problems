# ✅ Desafio proposto: "Analisador de Sentimentos Simples"
Você vai criar um programa que recebe uma lista de comentários de clientes e precisa classificá-los como:
- "Positivo"
- "Negativo"
- "Neutro"
Com base na presença de palavras-chave (como uma espécie de "modelo de IA" bem simplificado).

## ✅ Regras de Negócio:
1. Se o comentário tiver mais palavras positivas do que negativas, classifique como "Positivo".
2. Se tiver mais negativas, classifique como "Negativo".
3. Se empatar, classifique como "Neutro".
4. Gere um relatório geral com:
    - Quantos comentários foram positivos.
    - Quantos negativos.
    - Quantos neutros.
    - A porcentagem de cada um.

##  Exemplo de Estrutura de Dados (comments.json):
```bash
[
    {"client": "Maria", "comment": "O produto é ótimo, estou muito satisfeito!"},
    {"client": "Bob", "comment": "Horrível, péssimo atendimento e produto ruim."},
    {"client": "Carol", "comment": "Mais ou menos, poderia ser melhor."},
    {"client": "Daniel", "comment": "Adorei, excelente qualidade e entrega rápida!"},
    {"client": "Eve", "comment": "O produto não funciona, estou decepcionado."}
]
```

## ✅ Exemplo de lista de palavras:
```bash
positive_words = ["bom", "ótimo", "excelente", "adorei", "satisfeito", "gostei", "maravilhoso", "perfeito", "recomendo"]
negative_words = ["ruim", "péssimo", "horrível", "decepcionado", "insatisfeito", "demorado", "não funciona", "fraco", "desagradável"]
```

## ✅ Saída esperada:
```bash
{
    "Maria": {
        "comment": "o produto é ótimo, estou muito satisfeito!",
        "sentiment": "Positivo"
    },
    "Bob": {
        "comment": "horrível, péssimo atendimento e produto ruim.",
        "sentiment": "Negativo"
    },
    ...
    "summary": {
        "total_comments": 5,
        "classification": {
            "Positivo": 2,
            "Negativo": 2,
            "Neutro": 1
        },
        "percentage": {
            "Positivo": "40.00%",
            "Negativo": "40.00%",
            "Neutro": "20.00%"
        }
    }
}

```

## ✅ Como Rodar: 
Entrar na pasta do projeto da permissão ao arquivo e rodar o run.
```bash
chmod +x ./run.sh
./run.sh