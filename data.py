import json
from flask import Flask, render_template, redirect, url_for, request, session, flash, Response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from Temperature import Temperature
from __main__ import db

class Data:
    def add(self, temp):
        time = datetime.now().strftime("%d.%m.%Y %-H:%-M:%-S")
        temperature = Temperature(timestamp=time, value=temp)
        db.session.add(temperature)
        db.session.commit()
        print(f'New temperature record added: timestamp: {time}, value: {temp}')

    def last(self):
        # return self.temps[len(self.temps)-1]
        return db.session.query(Temperature).order_by(Temperature.id.desc()).first()


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


