#Разработайте класс SmartHomeSystem, который предоставляет функциональность для управления различными
# устройствами в умном доме, такими как освещение, климат-контроль, безопасность и т. д.
# Класс должен быть гибким и расширяемым, чтобы можно было легко добавлять новые типы устройств и функциональность.

class SmartHomeSystem():
    def get_command(self)
        pass

class SwitchDevice(): # для включения/выключения
    def turn_off():
        pass

class RegulateDevise(): #для регулировки увеличение-уменьшение света/тепла
    def increase():
        pass

class RegulateColor(): #изменение цвета освещения
    def color():
        pass


class SmartHomeSystemLightin(SmartHomeSystem, SwitchDevice, RegulateDevise, RegulateColor): #освещение
    def __init__(self, command):
        self.command = command
    def get_command(self):
      pass
    def turn_off():
        pass
    def increase():
        pass
    def color():
        pass


class SmartHomeSystemClimateControl(SmartHomeSystem, SwitchDevice, RegulateDevise): #климат-контроль
    def __init__(self, command):
        self.command = command
    def get_command(self):
      pass
    def turn_off():
        pass
    def increase():
        pass


class SmartHomeSystemSafety(SmartHomeSystem, SwitchDevice): #безопасность
    def __init__(self, command):
        self.command = command
    def get_command(self):
      pass
    def turn_off():
        pass







