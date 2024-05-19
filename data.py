import json
from datetime import datetime

class Data:

    temps: dict = []

    def __init__(self):
        with open("temps.json", "r") as f:
            self.temps = json.load(f)

    def list(self):
        print("-" * 10 + "Temps: " + "-" * 10)
        for i in self.temps:
            print(i)
        print("-" * 27)

    def add(self, temp):
        time = datetime.now().strftime("%d.%m.%Y %-H:%-M:%-S")
        self.temps.append({"timestamp": time, "value": float(temp)})
        self.save()

    def last(self):
        return self.temps[len(self.temps)-1]

    def last_n(self, n):
        if len(self.temps) <= int(n):
            return self.temps
        return self.temps[-int(n):]

    def del_n_oldest(self, n):
        if len(self.temps) <= int(n):
            self.temps = []
        else:
            self.temps = self.temps[int(n):]
        self.save()

    def delete(self, n):
        index = -1
        for i in range(0, len(self.temps)):
            if self.temps[i]["timestamp"] == n:
                index = i
                break
        if index > 0:
            self.temps.pop(index)
            self.save()
        return self.temps

    def save(self):
        with open("temps.json", "w") as f:
            json.dump(self.temps, f)


