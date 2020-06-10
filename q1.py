import abc

class Motor():
    @abc.abstractmethod
    def energia(self):
        pass

class Veiculo():
    def __init__(self, motor):
        self.motor = motor

    @abc.abstractmethod
    def mover(self):
        pass

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
