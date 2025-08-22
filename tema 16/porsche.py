class Porsche:

    def __init__(self, nume, hp, an, motor):
        self.nume = nume
        self.hp = hp
        self.an = an
        self.motor = motor
        self.tip = None
        self.model = None  
        self.motor_ales = None  
        self.optiuni = ["sedan", "SUV", "sport"]

    def alege_tipul(self):
        tip_ales = input("Alege ce tip de mașină ai dori (sedan, SUV sau sport): ").lower()
        optiuni_normalizate = [tip.lower() for tip in self.optiuni]

        if tip_ales in optiuni_normalizate:
            self.tip = tip_ales
            print(f"Ai ales tipul: {self.tip}")
        else:
            print("Tipul introdus nu este valid.")

    def afiseaza_modele_disponibile(self):
        modele = {
            "suv": ["Cayenne", "Macan"],
            "sedan": ["Panamera"],
            "sport": ["911", "718 Cayman", "718 Boxster"]
        }

        tip_masina = self.tip.lower()  

        if tip_masina in modele:
            print(f"\nPentru tipul '{tip_masina.upper()}' poți alege din următoarele modele:")
            for model in modele[tip_masina]:
                print(f" - {model}")
                
            
            model_ales = input("\nAlege un model: ").lower()
            if model_ales in [m.lower() for m in modele[tip_masina]]:
                self.model = model_ales
                print(f"Ai ales modelul: {self.model}")
                self.alege_motor()  
            else:
                print("Modelul introdus nu este valid.")
        else:
            print("Nu există modele disponibile pentru acest tip.")

    def alege_motor(self):
        
        motoare = ["V6", "V8", "electric"]
        print(f"\nPentru modelul {self.model.upper()}, alege un motor din următoarele opțiuni:")
        for motor in motoare:
            print(f" - {motor}")


        motor_ales = input("Ce motor ai dori (V6, V8 sau electric)? ").upper()
        if motor_ales in motoare:
            self.motor_ales = motor_ales
            print(f"Ai ales motorul: {self.motor_ales}")
            
            if self.motor_ales == "V8":
                self.alege_varianta_track()  
        else:
            print("Motorul introdus nu este valid.")

    def alege_varianta_track(self):
        
        if self.model == "911":
            
            varianta = input("\nVrei să alegi o variantă Track (GT2 RS, GT3, GT3 RS)? ").lower()
            variante_posibile = ["gt2 rs", "gt3", "gt3 rs"]

            if varianta in variante_posibile:
                print(f"Ai ales varianta {varianta.upper()} pentru modelul 911.")
                
                if varianta == "gt3":
                    self.alege_cutie()
            else:
                print("Varianta introdusă nu este validă.")
        else:
            print("Nu există variante Track pentru acest model.")

    def alege_cutie(self):
        
        cutie = input("\nVrei cutie manuală sau automată? (manuală/automată): ").lower()
        if cutie in ["manuală", "automată"]:
            print(f"Ai ales cutia {cutie.upper()} pentru modelul GT3.")
        else:
            print("Opțiunea introdusă nu este validă.")


masina = Porsche("Panamera", 440, 2024, "V6")
masina.alege_tipul()

masina.afiseaza_modele_disponibile()

masina = Porsche("Panamera", 440, 2024, "V6")
masina.alege_tipul()

masina.afiseaza_modele_disponibile()


masina = Porsche("Panamera", 440, 2024, "V6")
masina.alege_tipul()
masina.alege_varianta()

masina.afiseaza_modele_disponibile()






