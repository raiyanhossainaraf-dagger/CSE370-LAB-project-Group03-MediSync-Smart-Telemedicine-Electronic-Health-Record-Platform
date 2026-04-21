USE clinical_trial_db;
-- SHOW ALL TABLES
SHOW TABLES;

-- DESCRIBE ALL TABLES


DESCRIBE researcher;

DESCRIBE admin_sponsor;

DESCRIBE participant;

DESCRIBE trial;

DESCRIBE eligibility_criteria;

DESCRIBE enrollment;

DESCRIBE observation;

DESCRIBE medication;

DESCRIBE side_effect;


-- OPTIONAL: VIEW ALL DATA


SELECT * FROM researcher;

SELECT * FROM admin_sponsor;

SELECT * FROM participant;

SELECT * FROM trial;

SELECT * FROM eligibility_criteria;

SELECT * FROM enrollment;

SELECT * FROM observation;

SELECT * FROM medication;

SELECT * FROM side_effect;

-- Show enrollments
SELECT p.name, t.trial_name, e.status
FROM enrollment e
JOIN participant p ON e.participant_id = p.participant_id
JOIN trial t ON e.trial_id = t.trial_id;

-- Show trials with researcher names
SELECT t.trial_name, t.phase, r.name AS researcher
FROM trial t
JOIN researcher r ON t.researcher_id = r.researcher_id;

-- Show medication list
SELECT t.trial_name, m.drug_name, m.dosage
FROM medication m
JOIN trial t ON m.trial_id = t.trial_id;