class Raman :
    def use(self):
     print("Raman calling...")

class Harleen(Raman) :
     def use(self):
      super().use()
      print("Harleen Calling")

class Karan(Harleen) :
  def use(self):
      super().use()
      print("Karan Calling")

K= Karan()
K.use()  