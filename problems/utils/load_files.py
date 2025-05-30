import os, json

def load_files(file):
    try:        
        with open(file, "r") as f:
            data = json.load(f)
        return data
    except Exception as e:
        print(f"Erro ao carregar arquivo:\n {e}")
        return