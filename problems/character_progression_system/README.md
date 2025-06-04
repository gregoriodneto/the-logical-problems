# ✅ Desafio proposto: "Sistema de Progressão de Personagens"
Ele envolve gestão de personagens, cálculo de experiência, nível, e habilidades desbloqueadas.

## 🎯 Entrada:
- Uma lista de dicionários, cada um representando um personagem com:
    - ```name```: Nome do personagem.
    - ```level```: Nível atual.
    - ```experience```: Experiência atual.
    - ```battles_won```: Número de batalhas ganhas.
    - ```battles_lost```: Número de batalhas perdidas.
    - ```class```: Classe do personagem (```"Guerreiro"```, ```"Mago"``` ou ```"Arqueiro"```).

## ✅ Regras de Negócio:
1. Cada batalha vencida dá 100 de XP.
2. Cada batalha perdida dá 20 de XP.
3. Para subir de nível:
    - De nível 1 a 10: precisa de 500 XP.
    - De nível 11 a 20: precisa de 1000 XP.
    - Acima de nível 20: precisa de 2000 XP.
4. Ao subir de nível, desbloqueia habilidades conforme a classe:
| Classe    | Habilidades desbloqueadas                           |
| --------- | --------------------------------------------------- |
| Guerreiro | \["Ataque Poderoso", "Defesa de Ferro", "Fúria"]    |
| Mago      | \["Bola de Fogo", "Barreira Mágica", "Teleporte"]   |
| Arqueiro  | \["Flecha Explosiva", "Camuflagem", "Tiro Preciso"] |
*Desbloqueia uma habilidade nova a cada 5 níveis.*

## 🎯 Saída esperada:
- Um dicionário com a progressão de cada personagem:
    - Nome.
    - Nível final.
    - Experiência final.
    - Habilidades desbloqueadas.
- E um resumo:
    - Total de batalhas.
    - Quantos personagens chegaram acima do nível 20.

## ✅ Como Rodar: 
Entrar na pasta do projeto da permissão ao arquivo e rodar o run.
```bash
chmod +x ./run.sh
./run.sh