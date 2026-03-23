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

📸 Screenshots

📸 API Root / Base Endpoint

Displays the base API endpoints of the Train Services project, including routes for trains, passengers, and reservations.

<img width="1920" height="1020" alt="api_root" src="https://github.com/user-attachments/assets/5c47326d-f73e-495a-b06d-f95ca3f1b3ff" />

📸 Create Train (POST API)

Creates a new train record by sending JSON data to the API, storing train details such as number, name, route, and schedule.

<img width="1920" height="1020" alt="post_train" src="https://github.com/user-attachments/assets/7371e49e-fd81-4dcc-a19e-3e3b25a381bf" />


📸 Get All Trains (GET API)

Displays a list of all available trains with their details, retrieved using a GET request from the API.

<img width="1920" height="1020" alt="get_all_trains" src="https://github.com/user-attachments/assets/859a5884-95df-4bea-9c8a-0c06bcda699a" />

📸 Filter / Search Trains (GET API)

Retrieves trains based on search criteria such as source, destination, and departure date using query parameters.

<img width="1920" height="1020" alt="find_trains_filter" src="https://github.com/user-attachments/assets/043c86e5-2671-4fa1-a012-59dbb4c7b793" />

📸 Create Passenger (POST API)

Creates a new passenger record by sending user details such as first name, last name, contact information, and email to the API.

<img width="1920" height="1020" alt="post_passenger" src="https://github.com/user-attachments/assets/3c4992ab-d93a-473e-9d69-bd9a83bee6f9" />

📸 Create Reservation (POST API)

Creates a reservation by linking a passenger to a train, while dynamically updating seat availability and booking details.

<img width="1920" height="1020" alt="reserervation_train" src="https://github.com/user-attachments/assets/e464f4b4-3546-48a3-b826-c51b0ec2a882" />

📸 Update Train (PUT API)

Updates the details of a specific train using its primary key, allowing modification of existing records.

<img width="1920" height="1020" alt="put_train" src="https://github.com/user-attachments/assets/7908a9e2-555c-4d03-9edb-008dd4c18315" />

📸 Delete Train (DELETE API)

Deletes a specific train record from the system using its primary key.

<img width="1920" height="1020" alt="delete_train" src="https://github.com/user-attachments/assets/d75bad3e-0213-4786-8c7b-f29238f679e8" />

📸 Handle Overbooking (Validation)

Prevents booking more seats than available by validating seat availability and returning an appropriate error response.

<img width="1920" height="1020" alt="reserervation_train" src="https://github.com/user-attachments/assets/062c08d2-46e9-4886-9256-79fe98a6133c" />

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
