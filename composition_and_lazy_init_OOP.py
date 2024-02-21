from time import sleep

class Engine:
    def __init__(self):
        print("The Engine class object is intialized, but its is_on attribute is still false")
        self.is_on = False

    def engine_start(self):
        self.is_on = True
        print("Engine is on. self.is_on = True.")

class Wheels:
    def __init__(self, fancy=False):
        self.fancy = fancy
        if self.fancy:
            sleep(5) # some construction process that takes time
        self.rotating = False

    def gas_pedal_signal(self):
        self.rotating = True
        if self.fancy:
            print("wheels rotating forward, but it looks like they are going backwards!")
        else:
            print("wheels rotating forward...")

class GasPedal:
    def __init__(self, parent_car_obj, wheels):
        self.parent_car_obj = parent_car_obj
        self.wheels = wheels

    def press(self):
        if self.parent_car_obj.engine.is_on:
            self.wheels.gas_pedal_signal()
        else:
            print("Engine is not on yet. Pedal can't send signal to wheels.")

class Car:
    def __init__(self, fancy=False):
        self._engine = None
        self._gas_pedal = None
        self.fancy = fancy
    
    # The @property decorator in Python allows us to define methods that act like attributes, meaning they can be accessed and assigned like regular attributes, 
    # but behind the scenes, they execute custom code. In the given context, @property is used to define getter methods for the engine and gas_pedal attributes in the Car class, allowing lazy initialization.
    @property
    def engine(self, new_engine=None):
        if new_engine is not None: # setter (that will also return a value which you can ignore if you only want to set the attribute value)
            self._engine = new_engine
        elif self._engine is None: # getter
            self._engine = Engine()
        return self._engine

    @property
    def gas_pedal(self, new_gas_pedal=None):
        if new_gas_pedal is not None: # setter (this will also return a value which you can ignore if you only want to set the attribute value)
            self._gas_pedal = new_gas_pedal
        elif self._gas_pedal is None: # getter
            self._gas_pedal = GasPedal(self, Wheels(self.fancy))
        return self._gas_pedal

    def start(self):
        print("The Engine class object will be created and then its engine_start() method is run.")
        self.engine.engine_start()

# Create a Car instance
print("Overview of code: Create a Car object instance that has lazy initialization. (That is, attributes will eventually, when & if needed, become Class objects, but are initialized to None to start.)")
print("Code note: We will try to avoid OOP inheritance while still working with objects of different variations. Composition of objects is used instead.")
print()
print("Initialize a Car object and set some attributes to None. The Car's attribute consist of objects a driver could directly interact with. For instance, the user can't directly affect the Wheels; the user has to go through the Engine and GasPedal objects to do that, so we won't add the wheels attribute to the Car class.")
my_car = Car()
print()

print("Press the gas pedal before the Car's engine has been started... Create the GasPeal attribute/object which will depend on the Car's Wheel attribute/object (so initalize one of those first if you haven't already) and then run the press() method on GasPedal property.")
my_car.gas_pedal.press()
print()

# Start the car
print("Ok, now start the Car's Engine by calling its start() method.")
my_car.start()
print()

print("Now try the gas pedal...")
my_car.gas_pedal.press()
print()
print("######################")
print()

# Start the car
print("create a second car, but this time make it 'Fancy'")
my_car2 = Car(fancy=True)
print("Don't press the Gas Pedal this time. Just start the Engine with Car's start() method.")
my_car2.start()
print()
print("The Car has some of its attributes/objects now (i.e. its Engine), but not all of its other parts/attribuytes/objects have been created yet (i.e. its GaPedal hasn't been needed yet). It's standing idle with no Gas Pedal (or Wheels which it will get via Composition).")
print()
print("Now try the gas pedal...")
my_car2.gas_pedal.press()

print()
print("########################")
print("change the wheels now")
my_car2.gas_pedal()