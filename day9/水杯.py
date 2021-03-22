# 高度，容积，颜色，材质
# 能存放液体
class WaterCup:
    __high = 0
    __volume = 0
    __colour = ""
    __material = ""

    def setHigh(self, high):
        self.__high = high

    def getHigh(self):
        return self.__high

    def setVolume(self, volume):
        self.__volume = volume

    def getVolume(self):
        return self.__volume

    def setColour(self, colour):
        self.__colour = colour

    def getColour(self):
        return self.__colour

    def setMaterial(self, material):
        self.__material = material

    def getMaterial(self):
        return self.__material

    def store(self):
        print("水杯高", self.__high, "存放了", self.__volume, "颜色为", self.__colour, "材质为", self.__material)


m = WaterCup()
m.setHigh(2)
m.setVolume(30)
m.setColour("白色")
m.setMaterial("陶瓷")
m.store()
