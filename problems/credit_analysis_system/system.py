import os
from problems.utils.load_files import load_files

def credit_analysis(proposals):
    grouping = {}
    approved = 0
    rejected = 0
    for proposal in proposals:
        name = proposal["name"]
        income = proposal["income"]
        age = proposal["age"]
        requested_amount = proposal["requested_amount"]
        installments = proposal["installments"]
        debts = proposal["debts"]

        total_dividas = sum(debts)
        nova_parcela = round(requested_amount / installments, 2)
        comprometimento = round((total_dividas + nova_parcela) / income, 2)

        status = "Aprovado"
        motivos = []
        if age < 18:
            motivos.append("Idade insuficiente")
        if comprometimento > 0.40:
            motivos.append("Alta renda comprometida")
        if installments > 60:
            motivos.append("Parcelamento excede o limite de 60 meses")

        if len(motivos) > 0:
            status = "Reprovado"

        if status == "Aprovado":
            approved += 1
        else:
            rejected += 1

        grouping[name] = {
            "status": status,
            "motivos": motivos,
            "comprometimento": comprometimento,
            "nova_parcela": nova_parcela
        }

    approved_percent = round((approved * 100) / len(proposals),2)
    grouping["summary"] = {
        "approved": approved,
        "rejected": rejected,
        "approved_percent": approved_percent
    }
    return grouping

if __name__ == "__main__":
    path = os.path.dirname(__file__)
    file_path = os.path.join(path, "credits.json")
    proposals = load_files(file_path)
    result = credit_analysis(proposals)
    print(result)