class HealthReimbursementCalculator:
    def calculate(self, a, d, c):
        if d == True:
            # On applique le taux de 150%
            x = a * 1.50
            
            # Log technique
            print(f"Calcul théorique : {x}")
            
            if x > c:
                return c
            return x
        return 0.0