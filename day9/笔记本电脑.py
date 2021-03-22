# 有笔记本电脑（屏幕大小，价格，cpu型号，内存大小，待机时长），行为（打字，打游戏，看视频）
class Laptop:
    __screen = 0
    __price = 0
    __cpu = ""
    __memory = ""
    __standby = 0

    def setScreen(self, screen):
        self.__screen = screen

    def getScreen(self):
        return self.__screen

    def setPrice(self, price):
        self.__price = price

    def getPrice(self):
        return self.__price

    def setCpu(self, cpu):
        self.__cpu = cpu

    def getCpu(self):
        return self.__cpu

    def setMemory(self, memory):
        self.__memory = memory

    def getMemory(self):
        return self.__memory

    def setStandby(self, standby):
        self.__standby = standby

    def getStandby(self):
        return self.__standby

    def codeWord(self, code):
        print("打了", code, "字")

    def playGame(self, game):
        print("在玩", game)

    def watchTv(self, hour):
        print("看了", hour, "小时")

    def showMe(self):
        print("屏幕大小", self.__screen, "寸", "价格", self.__price, "CPU", self.__cpu, "内存大小", self.__memory, "待机时长",
              self.__standby, "小时")


s = Laptop()

s.setScreen(24)
s.setPrice(16000)
s.setCpu("i9")
s.setMemory("16G")
s.setStandby(8)

s.showMe()
s.codeWord(2500)
s.playGame("cs")
s.watchTv(2)
