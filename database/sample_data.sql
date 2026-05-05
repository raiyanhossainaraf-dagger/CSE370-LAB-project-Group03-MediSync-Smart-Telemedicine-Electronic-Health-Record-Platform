USE clinical_trial_db;

-- ==========================================
-- RESEARCHERS (5)
-- ==========================================
INSERT INTO researcher (name, specialization, email, password) VALUES
('Dr. Ahmed Khan', 'Cardiology', 'ahmed.khan@gmail.com', '123'),
('Dr. Sarah Ali', 'Oncology', 'sarah.ali@gmail.com', '123'),
('Dr. Imran Hossain', 'Neurology', 'imran.h@gmail.com', '123'),
('Dr. Nusrat Jahan', 'Dermatology', 'nusrat.j@gmail.com', '123'),
('Dr. Farhan Rahman', 'Endocrinology', 'farhan.r@gmail.com', '123');

-- ==========================================
-- ADMINS (3)
-- ==========================================
INSERT INTO admin_sponsor (name, email, password) VALUES
('Dagger', 'dagger@gmail.com', '123'),
('Rafid', 'rafid@gmail.com', '123'),
('Nafiz', 'nafiz@gmail.com', '123');

-- ==========================================
-- PARTICIPANTS (10)
-- ==========================================
INSERT INTO participant (name, age, gender, medical_history, password) VALUES
('Rafi Islam', 28, 'Male', 'Hypertension', '123'),
('Nadia Akter', 35, 'Female', 'Diabetes', '123'),
('Mustafiz Nafiz', 42, 'Male', 'Asthma', '123'),
('Mim Rahman', 31, 'Female', 'Migraine', '123'),
('Tanvir Hasan', 26, 'Male', 'No prior disease', '123'),
('Arif Hasan', 40, 'Male', 'Heart Disease', '123'),
('Shila Akter', 29, 'Female', 'Skin Allergy', '123'),
('Rahim Uddin', 50, 'Male', 'Diabetes', '123'),
('Nusrat Islam', 33, 'Female', 'Cancer', '123'),
('Sabbir Ahmed', 27, 'Male', 'Memory Issues', '123');

-- ==========================================
-- TRIALS (10)
-- ==========================================
INSERT INTO trial (trial_name, drug_name, phase, start_date, end_date, duration, researcher_id, admin_id) VALUES
('Heart Recovery Trial', 'CardioPlus', 'Phase I', '2026-05-01', '2026-08-01', 90, 1, 1),
('Cancer Immunity Study', 'OncoSafe', 'Phase II', '2026-06-01', '2026-12-01', 180, 2, 2),
('Brain Memory Test', 'NeuroMax', 'Phase I', '2026-07-01', '2026-10-01', 90, 3, 3),
('Skin Allergy Trial', 'DermaHeal', 'Phase III', '2026-08-01', '2027-02-01', 180, 4, 1),
('Sugar Control Study', 'GlucoFix', 'Phase II', '2026-09-01', '2027-03-01', 180, 5, 2),
('Lung Therapy Study', 'PulmoCare', 'Phase I', '2026-05-10', '2026-08-10', 90, 1, 3),
('Blood Pressure Study', 'HyperSafe', 'Phase II', '2026-06-15', '2026-12-15', 180, 2, 1),
('Cognitive Boost Trial', 'MindMax', 'Phase I', '2026-07-20', '2026-10-20', 90, 3, 2),
('Skin Repair Study', 'SkinFix', 'Phase III', '2026-08-25', '2027-02-25', 180, 4, 3),
('Insulin Response Study', 'InsuCare', 'Phase II', '2026-09-30', '2027-03-30', 180, 5, 1);

-- ==========================================
-- ELIGIBILITY (10)
-- ==========================================
INSERT INTO eligibility_criteria (trial_id, min_age, max_age, required_condition, exclusions) VALUES
(1, 25, 50, 'Heart Disease', 'Pregnancy'),
(2, 30, 65, 'Cancer', 'Kidney failure'),
(3, 20, 45, 'Memory Loss', 'Mental illness'),
(4, 18, 55, 'Skin Allergy', 'Severe infection'),
(5, 25, 60, 'Diabetes', 'Liver disease'),
(6, 30, 60, 'Lung Disease', 'Smoking'),
(7, 35, 70, 'Hypertension', 'Stroke'),
(8, 22, 45, 'Cognitive issues', 'Depression'),
(9, 20, 50, 'Skin damage', 'Allergy'),
(10, 30, 65, 'Diabetes', 'Heart disease');

-- ==========================================
-- ENROLLMENT (10)
-- ==========================================
INSERT INTO enrollment (trial_id, participant_id, enrollment_date, status) VALUES
(1,1,'2026-05-03','Approved'),
(2,2,'2026-06-05','Pending'),
(3,3,'2026-07-08','Approved'),
(4,4,'2026-08-10','Rejected'),
(5,5,'2026-09-12','Approved'),
(6,6,'2026-05-15','Pending'),
(7,7,'2026-06-20','Approved'),
(8,8,'2026-07-25','Pending'),
(9,9,'2026-08-28','Rejected'),
(10,10,'2026-10-01','Approved');

-- ==========================================
-- OBSERVATION (10)
-- ==========================================
INSERT INTO observation (trial_id, participant_id, visit_date, blood_pressure, temperature, notes) VALUES
(1,1,'2026-05-10','120/80',98.6,'Stable'),
(2,2,'2026-06-15','130/85',99.1,'Weakness'),
(3,3,'2026-07-20','118/78',98.4,'Normal'),
(4,4,'2026-08-18','125/82',99.0,'Skin irritation'),
(5,5,'2026-09-20','122/80',98.7,'Improving'),
(6,6,'2026-05-18','135/88',99.2,'Cough'),
(7,7,'2026-06-25','140/90',98.9,'High BP'),
(8,8,'2026-07-30','115/75',98.3,'Better'),
(9,9,'2026-09-01','120/80',98.6,'Healing'),
(10,10,'2026-10-05','130/85',99.0,'Stable');

-- ==========================================
-- MEDICATION (10)
-- ==========================================
INSERT INTO medication (trial_id, drug_name, dosage, frequency, researcher_id) VALUES
(1,'CardioPlus','50mg','Twice Daily',1),
(2,'OncoSafe','100mg','Once Daily',2),
(3,'NeuroMax','25mg','Twice Daily',3),
(4,'DermaHeal','10mg','Once Daily',4),
(5,'GlucoFix','75mg','Twice Daily',5),
(6,'PulmoCare','60mg','Once Daily',1),
(7,'HyperSafe','80mg','Twice Daily',2),
(8,'MindMax','20mg','Once Daily',3),
(9,'SkinFix','15mg','Twice Daily',4),
(10,'InsuCare','90mg','Once Daily',5);

-- ==========================================
-- SIDE EFFECT (10)
-- ==========================================
INSERT INTO side_effect (trial_id, participant_id, effect_type, severity, duration) VALUES
(1,1,'Headache','Mild',2),
(2,2,'Nausea','Moderate',4),
(3,3,'Dizziness','Mild',1),
(4,4,'Skin Rash','Severe',7),
(5,5,'Fatigue','Moderate',5),
(6,6,'Cough','Mild',3),
(7,7,'High BP','Severe',6),
(8,8,'Memory loss','Moderate',4),
(9,9,'Irritation','Mild',2),
(10,10,'Weakness','Moderate',3);

-- ==========================================
-- REPORT (10)
-- ==========================================
INSERT INTO report (trial_id, researcher_id, summary, result, status, created_at) VALUES
(1,1,'Initial Heart Study','Positive response','Published','2026-05-10 10:00:00'),
(2,2,'Cancer Trial Update','Moderate improvement','Published','2026-06-15 11:00:00'),
(3,3,'Memory Test','Good results','Published','2026-07-20 12:00:00'),
(4,4,'Skin Trial','Effective','Published','2026-08-18 13:00:00'),
(5,5,'Diabetes Study','Stable control','Published','2026-09-20 14:00:00'),
(6,1,'Lung Study','Improving','Published','2026-05-18 15:00:00'),
(7,2,'BP Study','Controlled','Published','2026-06-25 16:00:00'),
(8,3,'Cognitive Study','Better','Published','2026-07-30 17:00:00'),
(9,4,'Skin Repair','Healing','Published','2026-09-01 18:00:00'),
(10,5,'Insulin Study','Effective','Published','2026-10-05 19:00:00');