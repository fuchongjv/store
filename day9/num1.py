class AirConditioning:
    __brand = ""
    __price = 0

    def setBrand(self, brand):
        self.__brand = brand

    def getBrand(self):
        return self.__brand

    def setPrice(self, price):
        self.__price = price

    def getPrice(self):
        return self.__price

    def bootUp(self):
        print("空调开机了")

    def shutDown(self, time):
        print("空调在", time, "分钟后关机")


h = AirConditioning()
h.setBrand("海尔")
h.setPrice(2000)
print(h.getBrand(),h.getPrice())
h.bootUp()
h.shutDown(20)
