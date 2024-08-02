import json
from flask import Flask, render_template, redirect, url_for, request, session, flash, Response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from Temperature import Temperature
from __main__ import db

class Data:
    def add(self, temp):
        time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        temperature = Temperature(timestamp=time, value=temp)
        db.session.add(temperature)
        db.session.commit()
        print(f'New temperature record added: timestamp: {time}, value: {temp}')

    def last(self):
        return db.session.query(Temperature).order_by(Temperature.id.desc()).first()

    def last_n(self, n):
        return db.session.query(Temperature).order_by(Temperature.id.desc()).limit(n).all()

    def del_n_oldest(self, n):
        oldest_records = db.session.query(Temperature).order_by(Temperature.id.asc()).limit(n).all()
        for record in oldest_records:
            db.session.delete(record)
        db.session.commit()
        return db.session.query(Temperature).all()

    def delete(self, timestamp):
        record = db.session.query(Temperature).filter_by(timestamp=timestamp).first()
        if record:
            db.session.delete(record)
            db.session.commit()
        return db.session.query(Temperature).all()

    def get_all(self):
        return db.session.query(Temperature).all()

    def count(self):
        return db.session.query(Temperature).count()