class Car:

    def __init__(self):
        self.__updateSoftware()

    def drive(self):
        print ('driving')

    def __updateSoftware(self):
        print ('updating software')

    def updatesoft(self):
        self.__updateSoftware()
redcar = Car()
redcar.drive()
redcar.updatesoft()
#redcar.__updateSoftware()  #not accesible from object.
