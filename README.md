# 🚆 Train Reservation System (Backend API)

## 📌 Project Overview

This project is a backend system built using **Django** and **Django REST Framework** that simulates a real-world train reservation system.

It allows users to search trains, manage passengers, and book seats while ensuring that **overbooking is prevented using dynamic seat availability logic**.

The main focus of this project is to implement **real-time seat tracking, validation, and clean API design**.

---

## ⚙️ Key Features

* 🔍 Search trains based on source, destination, and departure date
* 🎟️ Book multiple seats in a single reservation
* 🚫 Prevent overbooking using backend validation
* 📊 Dynamic calculation of available seats using database aggregation
* 🔄 Full CRUD operations for Train, Passenger, and Reservation
* 📡 RESTful API design using Django REST Framework
* ⚠️ Meaningful error responses with available seat information
* 🧠 Clean code structure with proper separation (models, serializers, views, urls)

---

## 🧠 Core Logic (Important)

The system dynamically calculates available seats using aggregation:

* Total booked seats are calculated using `Sum()`
* Available seats = `total_seats - booked_seats`
* Validation ensures that requested seats do not exceed available seats

This prevents overbooking and ensures data consistency.

---

## 🛠️ Tech Stack

* Python 🐍
* Django
* Django REST Framework
* SQLite (default database)
* Git & GitHub

---

## 📂 Project Structure
``` text
trainServices/
│
├── trainServices/
│   ├── settings.py
│   ├── urls.py
│
├── trainApp/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
├── manage.py
```
## 🔗 API Endpoints

### 🚆 Train APIs

* `GET /trainServices/trains/` → Get all trains
* `POST /trainServices/trains/` → Create a new train

### 👤 Passenger APIs

* `GET /trainServices/passengers/` → Get all passengers
* `POST /trainServices/passengers/` → Add a passenger

### 🎟️ Reservation APIs

* `POST /trainServices/reservations/` → Book seats
* `GET /trainServices/reservations/` → View reservations

### 🔍 Custom Search API

* `POST /trainServices/find_trains/`
  → Filters trains using:

  * source
  * destination
  * departure_date

---

## ▶️ How to Run the Project

1. Clone the repository:

```bash
git clone <your-repo-link>
```

2. Navigate to the project folder:

```bash
cd trainServices
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Run the server:

```bash
python manage.py runserver
```

---

## 📊 Example API Response

### ✅ Successful Booking

```json
{
  "id": 3,
  "seats_booked": 5,
  "train": 3,
  "passenger": 1,
  "available_seats": 5
}
```

### ❌ Overbooking Error

```json
{
  "error": "Not enough seats available",
  "available_seats": 2
}
```

---

## 💡 Key Learnings

* Implemented real-world business logic (seat booking system)
* Used aggregation (`Sum`) for dynamic data calculation
* Applied serializer-level validation for data integrity
* Improved debugging and problem-solving skills
* Designed clean and scalable REST APIs

---

## 🚀 Future Improvements

* 🔐 Add authentication (JWT login/signup)
* ⏳ Implement waitlist system
* 🌐 Build frontend (React or HTML)
* 📈 Add filtering (only trains with available seats)

---

## 🙌 Conclusion

This project helped me understand how real-world backend systems work, especially in handling bookings and validations.

It strengthened my knowledge of Django, REST APIs, and database handling, and improved my ability to build scalable backend systems.

---
