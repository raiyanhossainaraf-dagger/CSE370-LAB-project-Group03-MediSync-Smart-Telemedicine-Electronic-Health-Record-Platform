CREATE DATABASE IF NOT EXISTS clinical_trial_db;
USE clinical_trial_db;

CREATE TABLE researcher (
    researcher_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    specialization VARCHAR(100),
    contact VARCHAR(20),
    email VARCHAR(100) UNIQUE
);

CREATE TABLE admin_sponsor (
    admin_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    role VARCHAR(50)
);

CREATE TABLE participant (
    participant_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    medical_history TEXT,
    allergy_info TEXT
);

CREATE TABLE trial (
    trial_id INT AUTO_INCREMENT PRIMARY KEY,
    trial_name VARCHAR(150),
    drug_name VARCHAR(100),
    phase VARCHAR(20),
    start_date DATE,
    end_date DATE,
    duration INT,
    researcher_id INT,
    admin_id INT,

    FOREIGN KEY (researcher_id) REFERENCES researcher(researcher_id),
    FOREIGN KEY (admin_id) REFERENCES admin_sponsor(admin_id)
);

CREATE TABLE eligibility_criteria (
    criteria_id INT AUTO_INCREMENT PRIMARY KEY,
    trial_id INT,
    min_age INT,
    max_age INT,
    required_condition VARCHAR(100),
    exclusions VARCHAR(255),

    FOREIGN KEY (trial_id) REFERENCES trial(trial_id)
);

CREATE TABLE enrollment (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    trial_id INT,
    participant_id INT,
    enrollment_date DATE,
    status VARCHAR(30),

    FOREIGN KEY (trial_id) REFERENCES trial(trial_id),
    FOREIGN KEY (participant_id) REFERENCES participant(participant_id)
);

CREATE TABLE observation (
    observation_id INT AUTO_INCREMENT PRIMARY KEY,
    trial_id INT,
    participant_id INT,
    visit_date DATE,
    blood_pressure VARCHAR(20),
    temperature DECIMAL(4,1),
    notes TEXT,

    FOREIGN KEY (trial_id) REFERENCES trial(trial_id),
    FOREIGN KEY (participant_id) REFERENCES participant(participant_id)
);

CREATE TABLE medication (
    medication_id INT AUTO_INCREMENT PRIMARY KEY,
    trial_id INT,
    drug_name VARCHAR(100),
    dosage VARCHAR(50),
    frequency VARCHAR(50),

    FOREIGN KEY (trial_id) REFERENCES trial(trial_id)
);

