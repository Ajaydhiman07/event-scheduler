# 🗓️ Event Scheduler API

A simple Flask-based RESTful API to schedule, manage, and search events. This app uses a JSON file (`events.json`) to persist data and supports full CRUD operations. Ideal for small-scale event tracking or testing API integrations with Postman.

---

## 🚀 Features

- ✅ Create new events  
- 🔍 Retrieve all or search events  
- ✏️ Update events by ID  
- 🗑️ Delete events by ID  
- 🔁 Support for recurring events (daily/weekly)  

---

## 🛠️ Tech Stack

- Python 3.10+  
- Flask 3.x  
- JSON for storage  
- Postman for testing  

---

## 📁 Project Structure

```
📦 event-scheduler/
├── app.py              # Main Flask application
├── events.json         # Data file to store all events
├── requirements.txt    # All required Python packages
└── README.md           # Project documentation
```

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Ajaydhiman07/event-scheduler.git
cd event-scheduler
```

### 2. Create & Activate a Virtual Environment

```bash
python -m venv venv
.\venv\Scripts\activate
    # On Windows
```

### 3. Install the Requirements

```bash
pip install -r requirements.txt
```

### 4. Run the Flask App

```bash
python app.py
```

Visit: [http://localhost:5000](http://localhost:5000)

---

## 🔌 API Endpoints

| Method | Endpoint                      | Description                   |
|--------|-------------------------------|-------------------------------|
| GET    | `/events`                     | Get all events                |
| GET    | `/events/search?q=term`       | Search events by keyword      |
| POST   | `/events`                     | Create a new event            |
| PUT    | `/events/<event_id>`          | Update an event by ID         |
| DELETE | `/events/<event_id>`          | Delete an event by ID         |

### 📥 Sample JSON for POST/PUT

```json
{
  "title": "Project Review",
  "description": "Final round sync",
  "start_time": "2025-07-01T10:00",
  "end_time": "2025-07-01T11:00",
  "recurrence": "weekly"
}
```

---

## ❗ Notes

- Make sure `events.json` file exists in the same directory as `app.py`
- The Flask app is meant for **development/testing**, not production

---

## 🙋‍♂️ Author

**Ajay Kumar**  
📧 [Ajaydhiman07 on GitHub](https://github.com/Ajaydhiman07)

---

## 📄 License

This project is licensed under the MIT License.
