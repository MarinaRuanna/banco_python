from models.cliente import Cliente
from models.conta import Conta

joao: Cliente = Cliente('João Silva', 'joao_silva@gmail.com', '123.654.987-89', '01/01/1991')
maria: Cliente = Cliente('Maria Souza', 'maria_souza@gmail.com', '987.456.321-32', '30/12/1989')

print(joao)
print(maria)

contaf: Conta = Conta(joao)
contaa: Conta = Conta(maria)

print(contaf)
print(contaa)

