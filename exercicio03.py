from faker import Faker
from rich.console import Console
from rich.table import Table

# CORREÇÃO: O jeito certo de chamar o Faker com o padrão do Brasil
fake = Faker("pt_BR") 
console = Console()

tabela = Table(title="Perfis de usuários brasileiros")
tabela.add_column("Nome", style="cyan", no_wrap=True)
tabela.add_column("Email", style="magenta")
tabela.add_column("cidade", style="green")

for _ in range(5):
    nome = fake.name()
    email = fake.email()
    cidade = fake.city()
    tabela.add_row(nome, email, cidade)

console.print(tabela)
