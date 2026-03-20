class trip:
    main_group = ['HEMANG', 'MANN', 'YUVRAJ', 'PAGO']

    def __init__(self, name):
        self.n = name

    def going(self):
        print(f"Extra Person: {self.n}")

    @classmethod
    def main_going(cls):
        print(f"Main Group: {cls.main_group}")

t1 = trip('HET')
t1.going()
trip.main_going()