#from rich.console import console
#from rich.table import table

#cosole = console()
#tabela = table(title="Produtos")
#tabela.add_column("ID")
#tabela.add_column("Nome")
#tabela.add_column("Preço")
                  
#tabela.add_row("1", "Teclado", "R$ 150,00")
#tabela.add_row("1", "Mouse", "R$ 80,00")

#console.print(tabela)       


from faker import Faker

fake = Faker("pt-BR")
for _ in range(3):
    print(f"{fake.name()} - {fake.email()}")  
