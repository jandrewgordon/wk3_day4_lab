from models.event import Event
from events_app import app
from flask import render_template, request, redirect
from models.events import events, append_event, remove_event

@app.route('/')
def index():
    return render_template('index.html', title='Events', events=events)

@app.route('/add-event')
def add_event():
    return render_template('add-event.html', title="Add Event")

@app.route('/', methods=['POST'])
def add_event_to_list():
    event_name = request.form['event_name']
    event_date = request.form['event_date']
    event_guests = request.form['event_guests']
    event_location = request.form['event_location']
    event_description = request.form['event_description']
    if request.form['recurring'] == 'y':
        recurring = True
    else:
        recurring = False
    new_event = Event(event_date, event_name, event_guests, event_location, event_description, recurring)
    append_event(new_event)
    return redirect('/')

@app.route('/delete/<event_number>', methods=['POST'])
def delete_event(event_number):
    remove_event(event_number)
    return redirect('/')

    
    
