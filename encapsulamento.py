class Usuario:
   def __init__ (self,nome,idade,cpf):
       self.nome=nome
       self.idade=idade
       self.cpf=cpf
       
isaac = Usuario('isaac',15,1234567890)       

print(isaac.nome)
print(isaac.idade)
print(isaac.cpf)
