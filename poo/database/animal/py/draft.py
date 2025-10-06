class animal:
    def __init__(self, specie: str, sound: str):
        self.specie: str = specie
        self.sound: str = sound
        self.age: int = 0
    
    def ageBy(self, amount: int)-> None:
        self.age += amount
        if self.age >= 4:
            print(f"warning:",self.specie,"morreu")

    def makeNoise(self) -> None:
        if self.age >= 4:
            print("RIP")
        elif self.age == 0:
            print("---")
        else:
            print(self.sound)
    
    def show(self):
        print(f"{self.specie}:{self.age}:{self.sound}")

def main():
def main():
    bixo = animal("", "")
    while True:
        line: str = input()
        args: list[str] = line.split(" ")
        if args[0] == "$init":
            specie = args[1]
            sound = args[2]
            bixo = animal(specie, sound)
        elif args[0] == "$grow":
            amount: int = int(args[1])
            bixo.ageBy(amount)
        elif args[0] == "$show":
            bixo.show()
        elif args[0] == "$end":
            break
        elif args[0] == "$noise":
            bixo.makeNoise()

main()