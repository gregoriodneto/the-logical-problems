# ✅ Desafio proposto: "Analisador de Tendências de Vendas"
Analisador de tendências de vendas.

## ✅ Regras de Negócio:
Você receberá uma lista de vendas, cada uma com:
1. "client": nome do cliente.
2. "product": nome do produto comprado.
3. "quantity": quantidade comprada.
4. "unit_price": preço unitário.
5. "date": data da compra ("YYYY-MM-DD").

## ✅ Seu script deve:
1. Calcular o total gasto por cada cliente.
2. Listar os produtos mais vendidos (em quantidade total).
3. Determinar o dia com maior volume de vendas (em faturamento total).
4. Exibir um resumo com:
    - Faturamento total.
    - Cliente que mais gastou.
    - Produto mais vendido.

## ✅ Exemplo de input (sales.json):
```bash
[
    {"client": "Ana", "product": "Notebook", "quantity": 1, "unit_price": 3500, "date": "2025-05-01"},
    {"client": "Bruno", "product": "Mouse", "quantity": 2, "unit_price": 50, "date": "2025-05-02"},
    {"client": "Ana", "product": "Teclado", "quantity": 1, "unit_price": 150, "date": "2025-05-01"},
    {"client": "Carlos", "product": "Monitor", "quantity": 1, "unit_price": 900, "date": "2025-05-03"},
    {"client": "Bruno", "product": "Notebook", "quantity": 1, "unit_price": 3500, "date": "2025-05-02"}
]

```

## ✅ Exemplo de saída esperada:
```bash
{
  "clients": {
    "Ana": 3650,
    "Bruno": 3600,
    "Carlos": 900
  },
  "most_sold_product": "Notebook",
  "busiest_day": "2025-05-02",
  "summary": {
    "total_revenue": 8150,
    "top_client": "Ana",
    "top_product": "Notebook"
  }
}

```

## ✅ Como Rodar: 
Entrar na pasta do projeto da permissão ao arquivo e rodar o run.
```bash
chmod +x ./run.sh
./run.sh