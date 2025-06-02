import os, json
from problems.utils.load_files import load_files

def detected_sentiments(text, positive_words, negative_words):
    text = text.lower()
    count_positive = sum(word in text for word in positive_words)
    count_negative = sum(word in text for word in negative_words)

    if count_positive > count_negative:
        return "Positivo"
    elif count_negative > count_positive:
        return "Negativo"
    else:
        return "Neutro"


def analyzer(comments):
    positive_words = ["bom", "ótimo", "excelente", "adorei", "satisfeito", "gostei", "maravilhoso", "perfeito", "recomendo"]
    negative_words = ["ruim", "péssimo", "horrível", "decepcionado", "insatisfeito", "demorado", "não funciona", "fraco", "desagradável"]

    grouping = {}    
    counts = {"Positivo": 0, "Negativo": 0, "Neutro": 0}

    for comment in comments:
        client  = comment["client"]
        text    = comment["comment"]

        sentiment = detected_sentiments(text, positive_words, negative_words)   
        counts[sentiment] += 1    

        grouping[client] = {
            "comment": comment["comment"],
            "sentiment": sentiment
        }

    total_comments = len(comments)
    grouping["summary"] = {
        "total_comments": total_comments,
        "classification": counts,
        "percentage": {
            key: f"{round((value / total_comments) * 100,2)}%" for key, value in counts.items()
        }
    }

    return grouping

if __name__ == "__main__":
    path = os.path.dirname(__file__)
    file_path = os.path.join(path, "comments.json")
    comments = load_files(file_path)
    result = analyzer(comments)
    print(result)