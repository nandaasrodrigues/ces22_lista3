# Decorator para formulacao de pizza adicionando os ingredientes desejados e o valor final,
# sendo 20 reais o preco da massa apenas (obrigatória)

class ComponentePizza:
    def pegarDescricao(self):
        return self.__class__.__name__
    def pegarCustoTotal(self):
        return self.__class__.custo  


class Massa(ComponentePizza):
    custo = 20.0

class Decorator(ComponentePizza):
    def __init__(self, componentePizza):
        self.componente = componentePizza
    def pegarCustoTotal(self):
        return self.componente.pegarCustoTotal() + ComponentePizza.pegarCustoTotal(self)
    def pegarDescricao(self):
        return (self.componente.pegarDescricao() + ' ' + ComponentePizza.pegarDescricao(self))

class Mussarela(Decorator):
    custo = 8.0
    def __init__(self, componentePizza):
        Decorator.__init__(self, componentePizza)

class Catupiry(Decorator):
    custo = 5.0
    def __init__(self, componentePizza):
        Decorator.__init__(self, componentePizza)

class Provolone(Decorator):
    custo = 8.0
    def __init__(self, componentePizza):
        Decorator.__init__(self, componentePizza)

class Cheddar(Decorator):
    custo = 8.0
    def __init__(self, componentePizza):
        Decorator.__init__(self, componentePizza)

class Frango(Decorator):
    custo = 12.0
    def __init__(self, componentePizza):
        Decorator.__init__(self, componentePizza)

class Calabresa(Decorator):
    custo = 6.0
    def __init__(self, componentePizza):
        Decorator.__init__(self, componentePizza)

class Cebola(Decorator):
    custo = 3.0
    def __init__(self, componentePizza):
        Decorator.__init__(self, componentePizza)

class Tomate(Decorator):
    custo =4.0
    def __init__(self, componentePizza):
        Decorator.__init__(self, componentePizza)

class Ovo(Decorator):
    custo = 5.0
    def __init__(self, componentePizza):
        Decorator.__init__(self, componentePizza)

pizza_quatro_queijos = Mussarela(Provolone(Catupiry(Cheddar(Massa()))))
print(pizza_quatro_queijos.pegarDescricao()+ ": R$" + str(pizza_quatro_queijos.pegarCustoTotal()))

pizzaPortuguesa = Mussarela(Calabresa(Tomate(Cebola(Ovo(Massa())))))
print(pizzaPortuguesa.pegarDescricao()+ ": R$" + str(pizzaPortuguesa.pegarCustoTotal()))

pizza_frango = Frango(Catupiry(Cebola(Tomate(Massa()))))
print(pizza_frango.pegarDescricao()+ ": R$" + str(pizza_frango.pegarCustoTotal()))

f"dfgjjj"