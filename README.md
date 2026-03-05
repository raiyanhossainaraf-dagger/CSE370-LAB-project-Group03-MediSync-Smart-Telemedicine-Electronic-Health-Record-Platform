# MediSync – Smart Telemedicine & Electronic Health Record Platform

## Overview

**MediSync** is a full-stack web application designed to simulate a modern **telemedicine and electronic health record (EHR) management system**. The platform enables patients, doctors, and administrators to interact through a unified system that manages healthcare workflows such as appointment scheduling, medical record storage, prescription management, and hospital analytics.

The primary objective of this project is to demonstrate the **design and implementation of a database-driven healthcare system** using modern backend technologies and structured database architecture. The system emphasizes **data integrity, role-based access control, and scalable API design**, which are core requirements in real-world healthcare software systems.

This project was developed as part of the **CSE370: Database Systems** course to showcase the practical application of database concepts such as **entity-relationship modeling, normalization, relational constraints, and SQL query optimization**, while integrating them with a modern backend framework.

---

## Objectives

The main objectives of MediSync are:

* To design a **scalable relational database schema** for healthcare data management.
* To implement a **RESTful backend API** using Python.
* To demonstrate **role-based system architecture** for patients, doctors, and administrators.
* To manage **electronic health records (EHR)** efficiently.
* To provide a structured platform for **appointment scheduling and prescription management**.

---

## System Architecture

The application follows a **modular backend architecture** built with FastAPI and SQLAlchemy. The architecture separates responsibilities into layers to ensure maintainability, scalability, and clear project organization.

### Architecture Layers

1. **API Layer** – Handles incoming HTTP requests and API routing.
2. **Service Layer** – Implements business logic and system workflows.
3. **Data Access Layer** – Manages database interactions via ORM models.
4. **Database Layer** – Stores relational data with integrity constraints.

This layered architecture reflects common patterns used in **industry-grade backend systems**.

---

## Key Features

### Patient Module

* Patient registration and secure authentication
* Patient profile management
* Appointment booking with doctors
* Viewing appointment history
* Uploading medical reports and documents

### Doctor Module

* Doctor profile and specialization management
* Doctor availability and scheduling system
* Viewing and managing patient appointments
* Adding consultation notes and diagnoses
* Digital prescription generation

### Admin Module

* Doctor verification and approval system
* Hospital department management
* System-wide appointment monitoring
* Healthcare analytics dashboard
* Activity logging for system events

---

## Database Design

The system is built upon a **relational database schema** designed according to standard database normalization principles. The database structure supports key healthcare workflows while ensuring referential integrity between entities.

### Core Entities

* Users
* Patients
* Doctors
* Departments
* Appointments
* MedicalRecords
* Prescriptions
* Reports
* ActivityLogs

### Key Relationships

* One-to-one relationship between **Users and Patients/Doctors**
* One-to-many relationship between **Doctors and Appointments**
* One-to-many relationship between **Patients and Medical Records**
* One-to-many relationship between **Medical Records and Prescriptions**

The schema enforces **foreign key constraints** to maintain data consistency across all related entities.

---

## Technology Stack

### Backend

* Python
* FastAPI
* SQLAlchemy ORM
* Pydantic

### Database

* PostgreSQL (recommended)
* MySQL (alternative)

### Frontend

* HTML
* CSS
* JavaScript

### Additional Tools

* Uvicorn (ASGI server)
* JWT-based authentication
* RESTful API documentation via Swagger UI

---

## Project Structure

```
medisync/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── config.py
│
│   ├── models/
│   ├── schemas/
│   ├── routers/
│   ├── services/
│   ├── utils/
│
├── uploads/
│
├── frontend/
│
├── tests/
│
├── requirements.txt
├── README.md
└── .env
```

This modular structure separates concerns across multiple components, allowing the application to scale and remain maintainable as new features are added.

---

## API Documentation

FastAPI automatically generates interactive API documentation.

After starting the server, the API documentation can be accessed at:

```
http://127.0.0.1:8000/docs
```

This interface allows developers to test endpoints and inspect request/response schemas.

---

## Installation Guide

### 1. Clone the Repository

```
git clone https://github.com/your-repository/medisync.git
cd medisync
```

### 2. Create a Virtual Environment

```
python -m venv venv
```

Activate the environment:

Mac/Linux:

```
source venv/bin/activate
```

Windows:

```
venv\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file and define the database connection:

```
DATABASE_URL=postgresql://username:password@localhost/medisync
```

### 5. Run the Application

```
uvicorn app.main:app --reload
```

---

## Future Improvements

While the current implementation demonstrates the core features of a telemedicine platform, several improvements can be integrated in future versions:

* Real-time video consultations
* AI-assisted symptom analysis
* Appointment wait-time prediction
* Mobile application integration
* Advanced healthcare analytics dashboards

---

## Educational Value

This project demonstrates practical applications of several **core database concepts**, including:

* Entity-Relationship (ER) modeling
* Relational schema design
* SQL data manipulation and queries
* Referential integrity using foreign keys
* Transaction-based system design

Additionally, it highlights the integration of database systems with **modern backend web frameworks**, providing a strong foundation for real-world software development.

---

## Contributors

This project was developed collaboratively as part of the **CSE370 Database Systems course**. Each contributor was responsible for designing and implementing different system modules, including patient services, doctor services, and administrative management features.

---

## License

This project is intended for **educational and academic purposes**.

---

## Conclusion

MediSync represents a prototype implementation of a **modern healthcare information management system**. By combining structured database design with scalable API architecture, the project demonstrates how real-world medical platforms can be modeled and implemented using contemporary software development technologies.
