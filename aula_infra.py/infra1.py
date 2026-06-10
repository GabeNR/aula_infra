#from pathlib import Path
import pathlib


pasta = pathlib.Path("dados")
pasta.mkdir(exist_ok=True)
arquivo = pasta / "registro.txt"
arquivo.write_text("conteúdo" , encoding="utf-8")
print(arquivo.read_text(encoding="utf-8"))
