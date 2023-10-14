class Vehicle:
  def __init__(self, make, model):
    self.make = make
    self.model = model

  def moves(self):
    print('Moves along ...')

  def get_make_model(self):
    print(f"I'm a {self.make} {self.model}.")

my_car = Vehicle('Tesla', 'Model 3')
my_car.get_make_model()
my_car.moves()

your_car = Vehicle('Cadillac', 'Escalade')
your_car.get_make_model()
your_car.moves()

################################################################

class Airplane(Vehicle):
  def __init__(self, make, model, faa_id):
    super().__init__(make, model)
    self.faa_id = faa_id

  def moves(self):
    print('Flies along ...')

class Truck(Vehicle):
  def moves(self):
    print('Rumbles along ...')

class GolfCart(Vehicle):
  pass

cessna = Airplane('Cessna', 'Sky', 'N-123456')
mack = Truck('Mack', 'Pinnacle')
golfWagon = GolfCart('Yamaha', 'GC100')

cessna.get_make_model()
cessna.moves()
mack.get_make_model()
mack.moves()
golfWagon.get_make_model()
golfWagon.moves()

print('\n\n')

for v in (my_car, your_car, cessna, mack, golfWagon):
  v.get_make_model()
  v.moves