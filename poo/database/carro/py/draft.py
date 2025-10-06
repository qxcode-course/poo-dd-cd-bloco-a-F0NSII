class carro:
    def __init__(self):
        self.pas: int = 0
        self.gas: int = 0
        self.km: int = 0
    
    def addPas(self, sumPas: int) -> None:
        self.pas += sumPas
        if self.pas > 2:
            print("fail: limite de pessoas atingido")
            self.pas = 2
        elif self.pas == 0:
            print("fail: nao ha ninguem no carro")

    def addGas(self, sumGas: int) -> None:
        self.gas += sumGas


    def addKm(self, sumKm: int) -> None:
        self.km += sumKm    
        self.gas - sumKm   

    def Show(self):
        print(f"pass: {self.pas}, gas: {self.gas}, km:{self.km}")

def main():
    Car = carro()
    while True:
        line: str = input()
        args: list[str] = line.split(" ")
        if args[0] == "enter":
            sumPas: int = int(args[1])
            Car.addPas(sumPas)
        elif args[0] == "leave":
            sumPas: int = -1
            Car.addPas(sumPas)
        elif args[0] == "show":
            Car.Show()
        elif args[0] == "fuel":
            sumGas: int = int(args[1])
            Car.addGas(sumGas)
        elif args[0] == "drive":
            sumKm: int = int(args[1])
            Car.addKm(sumKm)
            




main()