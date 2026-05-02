# Clinical Trial Management System

## Project Overview

The **Clinical Trial Management System (CTMS)** is a web-based database management application developed to streamline and digitize the administration of clinical research trials. The system is designed to support researchers, participants, and administrative personnel by providing an organized platform for trial creation, participant enrollment, eligibility screening, medication tracking, adverse event reporting, and clinical observations.

This project has been developed as an academic final project for the Database Management System course and demonstrates the practical implementation of relational database concepts, normalization, role-based access control, and full-stack system design.

---

## Objectives

The main objectives of this project are:

- To manage clinical trial records in an efficient and structured manner.
- To automate participant eligibility verification based on predefined criteria.
- To track medication schedules, observations, and trial progress.
- To record adverse events and side effects during trial periods.
- To provide separate dashboards for Admins, Researchers, and Participants.
- To demonstrate practical DBMS concepts through a real-world healthcare application.

---

## Unique Features

This system includes multiple advanced features that distinguish it from basic management systems:

### 1. Smart Eligibility Matching
Participants are automatically evaluated against trial criteria such as age range, medical condition, and exclusion rules before enrollment.

### 2. Adverse Event Monitoring
The system allows real-time reporting of symptoms, severity levels, outcomes, and side effects throughout the trial.

### 3. Role-Based Access Control
Separate functionalities are provided for Admin, Researcher, and Participant users.

---

## User Roles and Functionalities

### Admin
- Manage users and system access
- Creating clinical trials
- Managing clinical trials
- Generate reports and analytics
- Manages researchers and participants

### Researcher
- Administrating medications
- Record observations and trial progress
- Submit final trial reports
- Creating eligibility criteria 
- Observing real time reported side effects 

### Participant
- Apply for available trials
- View enrollment status
- Access visit schedules
- Report symptoms and side effects
- View assigned medications

---

## System Modules

- Authentication & Authorization
- Trial Management
- Participant Enrollment
- Eligibility Verification
- Observation Recording
- Medication Management
- Reporting & Analytics

---

## Database Design

The system follows a relational database structure with normalized tables.

### Main Entities

- Researcher
- Participant
- Admin
- Trial
- EligibilityCriteria
- Enrollment
- Observation
- Medication
- AdverseEvent
- SideEffect

---

## Technologies Used

### Backend
- Python
- FastAPI

### Database
-  MySQL

### Frontend
- HTML
- CSS
- JavaScript


---

## Project Folder Structure

```bash
ClinicalTrial-Management-System/
│── app/
│── frontend/
│── migrations/
│── tests/
│── uploads/
│── .env
│── README.md
│── requirements.txt
│── run.py