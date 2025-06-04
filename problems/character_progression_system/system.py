import os
from problems.utils.load_files import load_files

def system_level(level, experience):
    if level >= 1 and level <= 10:
        exp_needed = 500
    elif level >= 11 and level <= 20:
        exp_needed = 1000
    else:
        exp_needed = 2000

    if experience >= exp_needed:
        return system_level(level + 1, experience - exp_needed)
    else:
        return level
    
def skill_management(level, skills):
    level_skills = level / 5
    if level_skills >= 3:
        return skills[:3]
    elif level_skills >= 2:
        return skills[:2]
    elif level_skills >= 1:
        return skills[:1]
    else:
        return []

def character_progression(characters):
    classes_skills = {
        "Guerreiro": ["Ataque Poderoso", "Defesa de Ferro", "Fúria"],
        "Mago": ["Bola de Fogo", "Barreira Mágica", "Teleporte"],
        "Arqueiro": ["Flecha Explosiva", "Camuflagem", "Tiro Preciso"]
    }

    total_battle = 0
    above_level_20 = 0
    grouping = {}
    for char in characters:
        name            = char["name"]
        level           = char["level"]
        experience      = char["experience"]
        battles_won     = char["battles_won"]
        battles_lost    = char["battles_lost"]
        class_char      = char["class"]

        total_experience = experience + (battles_won * 100) + (battles_lost * 20)
        level = system_level(level, total_experience)
        if level > 20:
            above_level_20 += 1

        total_battle += battles_won + battles_lost
        skills = skill_management(level, classes_skills[class_char])
        grouping[name] = {
            "final_level": level,
            "final_experience": total_experience,
            "skills": skills
        }

    grouping["summary"] = {
        "total_battle": total_battle,
        "above_level_20": above_level_20
    }

    return grouping

if __name__ == "__main__":
    path = os.path.dirname(__file__)
    file_path = os.path.join(path, "characters.json")
    characters = load_files(file_path)
    result = character_progression(characters)
    print(result)