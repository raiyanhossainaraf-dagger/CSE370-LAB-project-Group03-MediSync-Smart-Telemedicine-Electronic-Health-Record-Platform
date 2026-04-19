USE clinical_trial_db;

INSERT INTO researcher (name, specialization, contact, email)
VALUES
('Dr. Ahmed Khan', 'Cardiology', '01711111111', 'ahmed@trial.com'),
('Dr. Sarah Ali', 'Oncology', '01822222222', 'sarah@trial.com');

INSERT INTO admin_sponsor (name, role)
VALUES
('John Sponsor', 'Sponsor'),
('Admin User', 'Administrator');

INSERT INTO participant (name, age, gender, medical_history, allergy_info)
VALUES
('Raiyan Hossain', 24, 'Male', 'Diabetes', 'Penicillin'),
('Nusrat Jahan', 30, 'Female', 'Hypertension', 'None');

INSERT INTO trial
(trial_name, drug_name, phase, start_date, end_date, duration, researcher_id, admin_id)
VALUES
('Heart Recovery Trial', 'CardioPlus', 'Phase I', '2026-05-01', '2026-08-01', 90, 1, 1),
('Cancer Response Trial', 'OncoHeal', 'Phase II', '2026-06-01', '2026-12-01', 180, 2, 2);

INSERT INTO enrollment
(trial_id, participant_id, enrollment_date, status)
VALUES
(1,1,'2026-05-02','Approved'),
(2,2,'2026-06-03','Pending');