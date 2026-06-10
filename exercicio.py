import random
import statistics as stats
from datetime import datetime
import json

valores = [random.randint(1, 500) for _ in range(30)]
print(f"Média: {stats.mean(valores):.2f}")
print(f"Menor: {min(valores)}")
print(f"Maior: {max(valores)}")
print(f"Data/Hora: {datetime.now()}")

dados = {
    "valores": valores,
    "media": stats.mean(valores),
    "menor": min(valores),
    "maior": max(valores),
    "data/hora": str(datetime.now()),
}

import os
os.makedirs("saida", exist_ok=True)

with open("saida/resultado.json", "w") as arquivo:
    json.dump(dados, arquivo, indent=4)
    print("Arquivo salvo com sucesso!")