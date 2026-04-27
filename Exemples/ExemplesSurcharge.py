class Money:
    def __init__(self, amount: float, currency: str = "EUR"):
        self.amount = amount
        self.currency = currency

    # Getter
    @property
    def amount(self) -> float:
        return self._amount

    # Setter
    @amount.setter
    def amount(self, value: float) -> None:
        if value < 0:
            raise ValueError("Le montant ne peut pas être négatif.")
        self._amount = value

    @property
    def currency(self) -> str:
        return self._currency

    @currency.setter
    def currency(self, value: str) -> None:
        if not value:
            raise ValueError("La devise est obligatoire.")
        self._currency = value.upper()

    # Surcharge de l'opérateur +
    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented

        if self.currency != other.currency:
            raise ValueError("Impossible d'additionner deux devises différentes.")

        return Money(self.amount + other.amount, self.currency)

    # Surcharge de l'opérateur -
    def __sub__(self, other):
        if not isinstance(other, Money):
            return NotImplemented

        if self.currency != other.currency:
            raise ValueError("Impossible de soustraire deux devises différentes.")

        result = self.amount - other.amount

        if result < 0:
            raise ValueError("Le résultat ne peut pas être négatif.")

        return Money(result, self.currency)

    # Surcharge de ==
    def __eq__(self, other):
        if not isinstance(other, Money):
            return False

        return self.amount == other.amount and self.currency == other.currency

    # Affichage utilisateur
    def __str__(self):
        return f"{self.amount:.2f} {self.currency}"

    # Affichage développeur/debug
    def __repr__(self):
        return f"Money(amount={self.amount}, currency='{self.currency}')"