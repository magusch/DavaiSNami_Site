# -*- coding: utf-8 -*-
from flask import render_template
from app import app,db

from .models import Dev_events

from datetime import datetime,timedelta

today = datetime.utcnow()+timedelta(hours=3)

@app.route('/')
@app.route('/events')
def index():
    events = Dev_events.query.order_by(Dev_events.date_from).limit(12).all()

    return render_template('index.html', events=events, today=today, timedelta=timedelta)

@app.route('/events/<int:month>/<int:day>/')
def event_for_day(month,day):
    date_search=datetime(year=today.year, month=month, day=day)
    events = Dev_events.query\
            .filter(db.func.date(Dev_events.date_to)>=date_search)\
            .filter(db.func.date(Dev_events.date_from)<=date_search)\
            .order_by(Dev_events.date_from).all()
    return render_template('index.html', events=events,today=today, timedelta=timedelta)

@app.route('/events/weekend/')
def event_for_weekend():

    saturday = db.func.date(today + timedelta(5 - today.weekday()))
    sunday = db.func.date(today + timedelta(6 - today.weekday()))

    events = Dev_events.query\
            .filter(db.func.date(Dev_events.date_to) <= sunday)\
            .filter(db.func.date(Dev_events.date_from) >= saturday)\
            .order_by(Dev_events.date_from).all()
    return render_template('index.html', events=events,today=today, timedelta=timedelta)