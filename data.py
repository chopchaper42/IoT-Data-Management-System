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
        # for a in self.data:
        #     id = a["id"]
            # if a["name"] == make:
            #     print("Error - make already exist! " + str(a))
            #     return
        time = datetime.now().strftime("%d.%m.%Y %-H:%-M:%-S")
        self.temps.append({"timestamp": time, "value": temp})
        self.save()

    # def edit(self, id, name):
    #     # for a in self.data:
    #     #     if a["id"] == id:
    #     #         a["name"] = name
    #     self.save()

    # def item(self, id):
    #     for car in self.temps:
    #         if car["id"] == id:
    #             return car

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

    def save(self):
        with open("temps.json", "w") as f:
            json.dump(self.temps, f)


