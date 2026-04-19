USE clinical_trial_db;

-- Show all trials
SELECT * FROM trial;

-- Show all participants
SELECT * FROM participant;

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