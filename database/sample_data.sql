USE clinical_trial_db;

-- ==========================================
-- SAMPLE DATA FOR RESEARCHER
-- ==========================================

INSERT INTO researcher (name, specialization, email) VALUES
('Dr. Ahmed Khan', 'Cardiology', 'ahmed.khan@gmail.com'),
('Dr. Sarah Ali', 'Oncology', 'sarah.ali@gmail.com'),
('Dr. Imran Hossain', 'Neurology', 'imran.h@gmail.com'),
('Dr. Nusrat Jahan', 'Dermatology', 'nusrat.j@gmail.com'),
('Dr. Farhan Rahman', 'Endocrinology', 'farhan.r@gmail.com');

-- ==========================================
-- SAMPLE DATA FOR ADMIN_SPONSOR
-- ==========================================

INSERT INTO admin_sponsor (name, email) VALUES
('Dagger', 'dagger@gmail.com'),
('Maria Admin', 'maria@gmail.com'),
('Rafid', 'rafid@gmail.com'),
('Nafiz', 'nafiz@gmail.com');

-- ==========================================
-- SAMPLE DATA FOR PARTICIPANT
-- ==========================================

INSERT INTO participant (name, age, gender, medical_history) VALUES
('Rafi Islam', 28, 'Male', 'Hypertension'),
('Nadia Akter', 35, 'Female', 'Diabetes'),
('Mofiz Nafiz', 42, 'Male', 'Asthma'),
('Mim Rahman', 31, 'Female', 'Migraine'),
('Tanvir Hasan', 26, 'Male', 'No prior disease');

-- ==========================================
-- SAMPLE DATA FOR TRIAL
-- ==========================================

INSERT INTO trial (
trial_name, drug_name, phase, start_date, end_date, duration,
researcher_id, admin_id
) VALUES
('Heart Recovery Trial', 'CardioPlus', 'Phase I', '2026-05-01', '2026-08-01', 90, 1, 1),
('Cancer Immunity Study', 'OncoSafe', 'Phase II', '2026-06-01', '2026-12-01', 180, 2, 2),
('Brain Memory Test', 'NeuroMax', 'Phase I', '2026-07-01', '2026-10-01', 90, 3, 3),
('Skin Allergy Trial', 'DermaHeal', 'Phase III', '2026-08-01', '2027-02-01', 180, 4, 4),
('Sugar Control Study', 'GlucoFix', 'Phase II', '2026-09-01', '2027-03-01', 180, 5, 3);

-- ==========================================
-- SAMPLE DATA FOR ELIGIBILITY_CRITERIA
-- ==========================================

INSERT INTO eligibility_criteria (
trial_id, min_age, max_age, required_condition, exclusions
) VALUES
(1, 25, 50, 'Heart Disease', 'Pregnant women'),
(2, 30, 65, 'Cancer', 'Kidney failure'),
(3, 20, 45, 'Memory Loss', 'Mental illness'),
(4, 18, 55, 'Skin Allergy', 'Severe infection'),
(5, 25, 60, 'Diabetes', 'Liver disease');

-- ==========================================
-- SAMPLE DATA FOR ENROLLMENT
-- ==========================================

INSERT INTO enrollment (
trial_id, participant_id, enrollment_date, status
) VALUES
(1, 1, '2026-05-03', 'Approved'),
(2, 2, '2026-06-05', 'Pending'),
(3, 3, '2026-07-08', 'Approved'),
(4, 4, '2026-08-10', 'Rejected'),
(5, 5, '2026-09-12', 'Approved');

-- ==========================================
-- SAMPLE DATA FOR OBSERVATION
-- ==========================================

INSERT INTO observation (
trial_id, participant_id, visit_date,
blood_pressure, temperature, notes
) VALUES
(1, 1, '2026-05-10', '120/80', 98.6, 'Stable'),
(2, 2, '2026-06-15', '130/85', 99.1, 'Mild weakness'),
(3, 3, '2026-07-20', '118/78', 98.4, 'Normal'),
(4, 4, '2026-08-18', '125/82', 99.0, 'Skin irritation'),
(5, 5, '2026-09-20', '122/80', 98.7, 'Improving');

-- ==========================================
-- SAMPLE DATA FOR MEDICATION
-- ==========================================

INSERT INTO medication (
trial_id, drug_name, dosage, frequency, researcher_id
) VALUES
(1, 'CardioPlus', '50mg', 'Twice Daily', 1),
(2, 'OncoSafe', '100mg', 'Once Daily', 2),
(3, 'NeuroMax', '25mg', 'Twice Daily', 3),
(4, 'DermaHeal', '10mg', 'Once Daily', 4),
(5, 'GlucoFix', '75mg', 'Twice Daily', 5);

INSERT INTO side_effect (trial_id, effect_type, severity, duration) VALUES
(1, 'Headache', 'Mild', 2),
(2, 'Nausea', 'Moderate', 4),
(3, 'Dizziness', 'Mild', 1),
(4, 'Skin Rash', 'Severe', 7),
(5, 'Fatigue', 'Moderate', 5);