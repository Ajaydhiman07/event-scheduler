from flask import Flask, jsonify, request
from datetime import datetime, timedelta
from uuid import uuid4
import json
import os
import threading
import time


app = Flask(__name__)

DATA_FILE = 'events.json'

# Load events from file
def load_events():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        try:
            data = json.load(f)
            return data if isinstance(data, list) else []
        except json.JSONDecodeError:
            return []


# Save events to file
def save_events(events):
    with open(DATA_FILE, 'w') as f:
        json.dump(events, f, indent=4)

# Sort by start_time
def sort_events(events):
    return sorted(events, key=lambda e: e['start_time'])

# Load initial events
events = load_events()

@app.route('/events', methods=['POST'])
def create_event():
    global events
    data = request.get_json()
    required = ['title', 'description', 'start_time', 'end_time']
    if not all(k in data for k in required):
        return jsonify({'error': 'Missing fields'}), 400

    try:
        datetime.fromisoformat(data['start_time'])
        datetime.fromisoformat(data['end_time'])
    except ValueError:
        return jsonify({'error': 'Invalid datetime format'}), 400

    event = {
        'id': str(uuid4()),
        'title': data['title'],
        'description': data['description'],
        'start_time': data['start_time'],
        'end_time': data['end_time'],
        'recurrence': data.get('recurrence')
    }
    events.append(event)
    save_events(events)
    return jsonify(event), 201

@app.route('/events', methods=['GET'])
def get_events():
    return jsonify(sort_events(events)), 200

@app.route('/events/<event_id>', methods=['PUT'])
def update_event(event_id):
    global events
    data = request.get_json()
    for event in events:
        if event['id'] == event_id:
            event.update({k: v for k, v in data.items() if k in event})
            save_events(events)
            return jsonify(event), 200
    return jsonify({'error': 'Event not found'}), 404

@app.route('/events/<event_id>', methods=['DELETE'])

def delete_event(event_id):
    global events  # ← this is important!
    original_len = len(events)
    events = [e for e in events if e['id'] != event_id]
    if len(events) == original_len:
        return jsonify({'error': 'Event not found'}), 404
    save_events(events)
    return jsonify({'message': 'Deleted'}), 200



@app.route('/events/search', methods=['GET'])
def search_events():
    query = request.args.get('q', '').lower()
    results = [e for e in events if query in e['title'].lower() or query in e['description'].lower()]
    return jsonify(results), 200

import threading
import time

def check_reminders():
    while True:
        now = datetime.now()
        upcoming = [
            e for e in events
            if datetime.fromisoformat(e['start_time']) <= now + timedelta(hours=1)
            and datetime.fromisoformat(e['start_time']) > now
        ]
        for e in upcoming:
            print(f"[Reminder] Upcoming: {e['title']} at {e['start_time']}")
        time.sleep(60)

# Start the thread
threading.Thread(target=check_reminders, daemon=True).start()


if __name__ == '__main__':
    app.run(debug=True)
