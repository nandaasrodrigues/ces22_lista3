import abc

class Motor(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def energia(self):
        pass

class Veiculo(metaclass=abc.ABCMeta):
    def __init__(self, motor):
        self.motor = motor

    @abc.abstractmethod
    def mover(self):
        pass

class VeiculoCombustao(metaclass=abc.ABCMeta):

class VeiculoEletricidade(metaclass=abc.ABCMeta):

class VeiculoHibrido(metaclass=abc.ABCMeta):


class Carro(Veiculo):
    def __init__(self, motor):
        super(Carro, self).__init__(motor)

    def mover(self):
        print("Carro movido a ", end="")
        self.motor.energia()

class Caminhao(Veiculo):
    def __init__(self, motor):
        super(Caminhao, self).__init__(motor)

    def mover(self):
        print("Caminhao movido a ", end="")
        self.motor.energia()

class Moto(Veiculo):
    def __init__(self, motor):
        super(Moto, self).__init__(motor)

    def mover(self):
        print("Moto movida a ", end="")
        self.motor.energia()


class MotorEletrico(Motor):
    def energia(self):
        print("energia eletrica.")

class MotorHibrido(Motor):
    def energia(self):
        print("energia eletrica e combustao.")

class MotorCombustao(Motor):
    def energia(self):
        print("combustao.")


auto1 = Carro(MotorHibrido())
auto1.mover()

auto2 = Moto(MotorEletrico())
auto2.mover()

auto3 = Caminhao(MotorCombustao())
auto3.mover()


class FrenchLocalizer: 
  
    """ it simply returns the french version """
  
    def __init__(self): 
  
        self.translations = {"car": "voiture", "bike": "bicyclette", 
                             "cycle":"cyclette"} 
  
    def localize(self, message): 
  
        """change the message using translations"""
        return self.translations.get(msg, msg) 
  
class SpanishLocalizer: 
    """it simply returns the spanish version"""
  
    def __init__(self): 
        self.translations = {"car": "coche", "bike": "bicicleta", 
                             "cycle":"ciclo"} 
  
    def localize(self, msg): 
  
        """change the message using translations"""
        return self.translations.get(msg, msg) 
  
class EnglishLocalizer: 
    """Simply return the same message"""
  
    def localize(self, msg): 
        return msg 
  
def Factory(language ="English"): 
  
    """Factory Method"""
    localizers = { 
        "French": FrenchLocalizer, 
        "English": EnglishLocalizer, 
        "Spanish": SpanishLocalizer, 
    } 
  
    return localizers[language]() 
  
if __name__ == "__main__": 
  
    f = Factory("French") 
    e = Factory("English") 
    s = Factory("Spanish") 
  
    message = ["car", "bike", "cycle"] 
  
    for msg in message: 
        print(f.localize(msg)) 
        print(e.localize(msg)) 
        print(s.localize(msg))