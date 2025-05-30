import os
from datetime import datetime, timedelta
from problems.utils.load_files import load_files

def management(proposals):
    grouping = {}
    total_approved_borrowed = 0
    total_rejected_borrowed = 0
    summary_books = []
    
    for proposal in proposals:
        user = proposal["user"]
        user_type = proposal["user_type"]
        borrowed_books = proposal["borrowed_books"]
        has_late_books = proposal["has_late_books"]
        requested_books = proposal["requested_books"]
        
        today = datetime.now()

        reasons = []
        books = []
        
        if user_type == "Aluno":
            expected_return_date = today + timedelta(days=7)
        elif user_type == "Professor":
            expected_return_date = today + timedelta(days=14)
        elif user_type == "Pesquisador":
            expected_return_date = today + timedelta(days=30)
        else:
            reasons.append("Tipo de usuário inválido.")
            expected_return_date = None

        if borrowed_books >= 5:
            reasons.append("Número máximo de livros emprestados.")

        if has_late_books:
            reasons.append("Usuário contém livros em atraso.")
        
        for book in requested_books:
            if book["stock"] <= 0:
                reasons.append(f"Livro '{book['title']}' não disponível.")
            else:
                books.append(book)

        if reasons:
            status = "Rejected"
            total_rejected_borrowed += 1
        else:
            status = "Approved"
            total_approved_borrowed += 1

        grouping[user] = {
            "status": status,
            "reasons": reasons,
            "expected_return_date": expected_return_date.strftime("%Y-%m-%d") if status == "Approved" else None,
            "number_books_borrowed": len(books),
            "borrowed_books": [book["title"] for book in books]            
        }

        if reasons:
            summary_books.append({ user:reasons })

    grouping["summary"] = {
        "total_loans_made": total_approved_borrowed,
        "total_loans_denied": total_rejected_borrowed,
        "denial_reasons": summary_books
    }

    return grouping

if __name__ == "__main__":
    path = os.path.dirname(__file__)
    file_path = os.path.join(path, "proposals.json")
    proposals = load_files(file_path)
    result = management(proposals)
    print(result)