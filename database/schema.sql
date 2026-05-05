CREATE DATABASE IF NOT EXISTS clinical_trial_db;
USE clinical_trial_db;

-- ================= RESEARCHER =================
CREATE TABLE researcher (
    researcher_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    specialization VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255)
);

-- ================= ADMIN =================
CREATE TABLE admin_sponsor (
    admin_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255)
);

-- ================= PARTICIPANT =================
CREATE TABLE participant (
    participant_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    medical_history TEXT,
    password VARCHAR(255)
);

-- ================= TRIAL =================
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

-- ================= ELIGIBILITY =================
CREATE TABLE eligibility_criteria (
    criteria_id INT AUTO_INCREMENT PRIMARY KEY,
    trial_id INT,
    min_age INT,
    max_age INT,
    required_condition VARCHAR(100),
    exclusions VARCHAR(255),

    FOREIGN KEY (trial_id) REFERENCES trial(trial_id)
);

-- ================= ENROLLMENT =================
CREATE TABLE enrollment (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    trial_id INT,
    participant_id INT,
    enrollment_date DATE,
    status VARCHAR(30) DEFAULT 'Pending',

    FOREIGN KEY (trial_id) REFERENCES trial(trial_id),
    FOREIGN KEY (participant_id) REFERENCES participant(participant_id)
);

-- ================= OBSERVATION =================
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

-- ================= MEDICATION =================
CREATE TABLE medication (
    medication_id INT AUTO_INCREMENT PRIMARY KEY,
    trial_id INT,
    drug_name VARCHAR(100),
    dosage VARCHAR(50),
    frequency VARCHAR(50),
    researcher_id INT,

    FOREIGN KEY (trial_id) REFERENCES trial(trial_id),
    FOREIGN KEY (researcher_id) REFERENCES researcher(researcher_id)
);

-- ================= SIDE EFFECT =================
CREATE TABLE side_effect (
    effect_id INT AUTO_INCREMENT PRIMARY KEY,
    trial_id INT,
    participant_id INT,
    effect_type VARCHAR(100),
    severity VARCHAR(20),
    duration INT,

    FOREIGN KEY (trial_id) REFERENCES trial(trial_id),
    FOREIGN KEY (participant_id) REFERENCES participant(participant_id)
);

-- ================= REPORT =================
CREATE TABLE report (
    report_id INT AUTO_INCREMENT PRIMARY KEY,
    trial_id INT NOT NULL,
    researcher_id INT NOT NULL,
    summary TEXT NOT NULL,
    result TEXT NOT NULL,
    image VARCHAR(255),
    status VARCHAR(20) DEFAULT 'Published',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (trial_id) REFERENCES trial(trial_id),
    FOREIGN KEY (researcher_id) REFERENCES researcher(researcher_id)
);