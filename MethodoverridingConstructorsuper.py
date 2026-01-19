class Raman:
    def __init__(self, pen):
        self.pen = pen

    def use(self):
        print("Pen:", self.pen)


class Harleen(Raman):
    def __init__(self, pen, pencil):
        super().__init__(pen)   # Pass pen to Raman
        self.pencil = pencil

    def use(self):
        super().use()
        print("Pencil:", self.pencil)


class Karan(Harleen):
    def __init__(self, pen, pencil, eraser):
        super().__init__(pen, pencil)   # Pass pen & pencil upward
        self.eraser = eraser

    def use(self):
        super().use()
        print("Eraser:", self.eraser)


K = Karan("Parker", "Nataraj", "Doms")
K.use()
