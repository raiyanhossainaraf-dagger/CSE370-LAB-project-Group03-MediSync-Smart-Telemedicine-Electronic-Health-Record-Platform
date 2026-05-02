// ================= USER AUTH =================

function getUser() {
    try {
        return JSON.parse(localStorage.getItem("user"));
    } catch {
        return null;
    }
}

function requireAuth() {
    const user = getUser();

    if (!user) {
        alert("Please login first");
        window.location.href = "login.html";
        return null;
    }

    return user;
}

function requireRole(role) {
    const user = requireAuth();
    if (!user) return null;

    if (user.role !== role) {
        alert("Access denied");
        window.location.href = "index.html";
        return null;
    }

    return user;
}

function logout() {
    localStorage.removeItem("user");
    window.location.href = "login.html";
}


// ================= HELPER =================

async function fetchData(url) {
    try {
        const response = await fetch(url);
        if (!response.ok) throw new Error(response.status);
        return await response.json();
    } catch (err) {
        console.error(err);
        alert("Server error");
        return [];
    }
}

function getStatusClass(status) {
    if (status === "Approved") return "approved";
    if (status === "Pending") return "pending";
    if (status === "Rejected") return "rejected";
    return "";
}

function showToast(message) {
    const toast = document.createElement("div");
    toast.innerText = message;

    toast.style.position = "fixed";
    toast.style.bottom = "20px";
    toast.style.right = "20px";
    toast.style.background = "#1abc9c";
    toast.style.color = "white";
    toast.style.padding = "10px 15px";
    toast.style.borderRadius = "8px";
    toast.style.zIndex = "9999";

    document.body.appendChild(toast);
    setTimeout(() => toast.remove(), 2000);
}


// ================= ADMIN DASHBOARD =================

async function loadAdminDashboard() {
    const user = requireRole("admin");
    if (!user) return;

    const table = document.getElementById("tableBody");
    if (!table) return;

    table.innerHTML = `<tr><td colspan="7">Loading...</td></tr>`;

    // ✅ FIXED API
    const data = await fetchData("http://127.0.0.1:8000/admin/info");

    if (!data || data.length === 0) {
        table.innerHTML = `<tr><td colspan="7">No data</td></tr>`;
        return;
    }

    table.innerHTML = "";

    let totalParticipants = new Set();
    let totalTrials = new Set();
    let approved = 0;

    data.forEach(item => {

        totalParticipants.add(item.participant);
        totalTrials.add(item.trial);

        if (item.status === "Approved") approved++;

        const statusClass = getStatusClass(item.status);

        table.innerHTML += `
            <tr>
                <td>${item.participant}</td>
                <td>${item.trial}</td>
                <td>${item.phase}</td>
                <td><span class="status ${statusClass}">${item.status}</span></td>
                <td>${item.researcher}</td>
                <td>
                    <button onclick="approveEnrollment(${item.id})" class="btn-approve">Approve</button>
                    <button onclick="rejectEnrollment(${item.id})" class="btn-reject">Reject</button>
                    <button onclick="deleteEnrollment(${item.id})" class="btn-delete">Delete</button>
                </td>
            </tr>
        `;
    });

    document.getElementById("totalParticipants").innerText = totalParticipants.size;
    document.getElementById("totalTrials").innerText = totalTrials.size;
    document.getElementById("approvedCount").innerText = approved;
}

// ================= CREATE TRIAL =================

async function createTrial() {
    const trial_name = document.getElementById("trialName").value;
    const phase = document.getElementById("trialPhase").value;
    const researcher_id = parseInt(document.getElementById("researcherId").value);

    const participant_ids = document.getElementById("participants").value
        .split(",")
        .map(id => parseInt(id.trim()))
        .filter(id => !isNaN(id));

    const response = await fetch("http://127.0.0.1:8000/admin/create-trial", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            trial_name,
            phase,
            researcher_id,
            participants: participant_ids
        })
    });

    if (!response.ok) {
        const data = await response.json();
        alert(data.detail);
        return;
    }

    showToast("Trial created");
    window.location.href = "admin_dashboard.html";
}


// ================= UPDATE STATUS =================

async function updateStatus(id, status) {
    const response = await fetch(
        `http://127.0.0.1:8000/enrollment/update-status/${id}?status=${status}`,
        { method: "PUT" }
    );

    if (!response.ok) {
        alert("Update failed");
        return;
    }

    showToast("Status updated");
    loadAdminDashboard();
}


// ================= DELETE TRIAL =================

async function deleteTrial(trial_id) {
    if (!confirm("Delete this trial?")) return;

    const response = await fetch(
        `http://127.0.0.1:8000/admin/delete-trial/${trial_id}`,
        { method: "DELETE" }
    );

    const data = await response.json();

    if (!response.ok) {
        alert(data.detail);
        return;
    }

    showToast("Trial deleted");
    loadAdminDashboard();
}


// ================= RESEARCHERS =================

async function loadResearchers() {
    requireRole("admin");

    const table = document.getElementById("researcherTable");
    if (!table) return;

    table.innerHTML = `<tr><td colspan="5">Loading...</td></tr>`;

    const data = await fetchData("http://127.0.0.1:8000/admin/researchers");

    table.innerHTML = "";

    data.forEach(r => {
        table.innerHTML += `
            <tr>
                <td>${r.id}</td>
                <td>${r.name}</td>
                <td>${r.specialization || "-"}</td>
                <td>${r.email || "-"}</td>
                <td>
                    <button onclick="deleteResearcher(${r.id})" class="btn-delete">Delete</button>
                </td>
            </tr>
        `;
    });
}


async function addResearcher() {
    const name = document.getElementById("r_name").value;
    const specialization = document.getElementById("r_spec").value;
    const email = document.getElementById("r_email").value;

    if (!name) return alert("Name required");

    const res = await fetch("http://127.0.0.1:8000/admin/add-researcher", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, specialization, email })
    });

    if (res.ok) {
        showToast("Researcher added");
        loadResearchers();

        document.getElementById("r_name").value = "";
        document.getElementById("r_spec").value = "";
        document.getElementById("r_email").value = "";
    } else {
        alert("Error adding researcher");
    }
}


async function deleteResearcher(id) {
    if (!confirm("Delete this researcher?")) return;

    const res = await fetch(`http://127.0.0.1:8000/admin/delete-researcher/${id}`, {
        method: "DELETE"
    });

    const data = await res.json();

    if (!res.ok) {
        alert(data.detail);
        return;
    }

    showToast("Deleted");
    loadResearchers();
}


// ================= PARTICIPANTS =================

async function loadParticipants() {
    requireRole("admin");

    const table = document.getElementById("participantTable");
    if (!table) return;

    table.innerHTML = `<tr><td colspan="6">Loading...</td></tr>`;

    const data = await fetchData("http://127.0.0.1:8000/admin/participants");

    table.innerHTML = "";

    data.forEach(p => {
        table.innerHTML += `
            <tr>
                <td>${p.id}</td>
                <td>${p.name}</td>
                <td>${p.age}</td>
                <td>${p.gender}</td>
                <td>${p.medical_history || "-"}</td>
                <td>
                    <button onclick="deleteParticipant(${p.id})" class="btn-delete">Delete</button>
                </td>
            </tr>
        `;
    });
}


async function addParticipant() {
    const name = document.getElementById("p_name").value;
    const age = parseInt(document.getElementById("p_age").value);
    const gender = document.getElementById("p_gender").value;
    const medical_history = document.getElementById("p_history").value;

    if (!name || !age) return alert("Name and Age required");

    const res = await fetch("http://127.0.0.1:8000/admin/add-participant", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, age, gender, medical_history })
    });

    if (res.ok) {
        showToast("Participant added");
        loadParticipants();

        document.getElementById("p_name").value = "";
        document.getElementById("p_age").value = "";
        document.getElementById("p_gender").value = "";
        document.getElementById("p_history").value = "";
    } else {
        alert("Error adding participant");
    }
}


async function deleteParticipant(id) {
    if (!confirm("Delete this participant?")) return;

    const res = await fetch(`http://127.0.0.1:8000/admin/delete-participant/${id}`, {
        method: "DELETE"
    });

    const data = await res.json();

    if (!res.ok) {
        alert(data.detail);
        return;
    }

    showToast("Deleted");
    loadParticipants();
}

// ================= RESEARCHER DASHBOARD =================

async function loadResearcherDashboard() {
    const user = requireRole("researcher");
    if (!user) return;

    const table = document.getElementById("researcher-table");
    if (!table) return;

    table.innerHTML = `<tr><td colspan="4">Loading...</td></tr>`;

    const data = await fetchData(
        `http://127.0.0.1:8000/dashboard/researcher/${user.user_id}`
    );

    table.innerHTML = "";

    if (data.length === 0) {
        table.innerHTML = `<tr><td colspan="4">No data available</td></tr>`;
        return;
    }

    data.forEach(item => {
        const statusClass = getStatusClass(item.status);

        table.innerHTML += `
            <tr>
                <td>${item.trial}</td>
                <td>${item.phase}</td>
                <td>${item.participant}</td>
                <td><span class="status ${statusClass}">${item.status}</span></td>
            </tr>
        `;
    });
}

async function loadResearcherEffects() {
    const user = requireRole("researcher");
    if (!user) return;

    const table = document.getElementById("researcherEffects");
    if (!table) return;

    table.innerHTML = "<tr><td colspan='5'>Loading...</td></tr>";

    const data = await fetchData(`http://127.0.0.1:8000/dashboard/effects/${user.user_id}`)

    table.innerHTML = "";

    if (data.length === 0) {
        table.innerHTML = "<tr><td colspan='5'>No reports</td></tr>";
        return;
    }

    data.forEach(e => {
        table.innerHTML += `
            <tr>
                <td>${e.participant}</td>
                <td>${e.trial}</td>
                <td>${e.effect}</td>
                <td>${e.severity}</td>
                <td>${e.duration} days</td>
            </tr>
        `;
    });
}

async function addMedication() {
    const user = getUser();

    const trialId = document.getElementById("medTrial").value;
    const drug = document.getElementById("drugName").value;
    const dosage = document.getElementById("dosage").value;
    const freq = document.getElementById("frequency").value;

    await fetch("http://127.0.0.1:8000/dashboard/medication", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            trial_id: trialId,
            drug_name: drug,
            dosage: dosage,
            frequency: freq,
            researcher_id: user.user_id
        })
    });

    alert("Medication added");
}

async function addObservation() {
    const trial = document.getElementById("obsTrial").value;
    const pid = document.getElementById("obsParticipant").value;
    const date = document.getElementById("visitDate").value;
    const bp = document.getElementById("bp").value;
    const temp = document.getElementById("temp").value;
    const notes = document.getElementById("notes").value;

    await fetch("http://127.0.0.1:8000/dashboard/observation", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            trial_id: trial,
            participant_id: pid,
            visit_date: date,
            blood_pressure: bp,
            temperature: temp,
            notes: notes
        })
    });

    alert("Observation saved");
}

async function submitReport() {
    const user = getUser();

    const trial = document.getElementById("repTrial").value;
    const summary = document.getElementById("summary").value;
    const result = document.getElementById("result").value;

    await fetch("http://127.0.0.1:8000/dashboard/report", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            trial_id: trial,
            researcher_id: user.user_id,
            summary: summary,
            result: result
        })
    });

    alert("Report submitted");
}

async function addCriteria() {
    await fetch("http://127.0.0.1:8000/dashboard/eligibility", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            trial_id: eTrial.value,
            min_age: minAge.value,
            max_age: maxAge.value,
            condition: condition.value,
            exclusions: exclusions.value
        })
    });

    alert("Criteria saved");
}

// ================= PARTICIPANT DASHBOARD =================

async function loadParticipantDashboard() {
    const user = requireRole("participant");
    if (!user) return;

    const table = document.getElementById("participant-table");
    if (!table) return;

    table.innerHTML = `<tr><td colspan="3">Loading...</td></tr>`;

    const data = await fetchData(
        `http://127.0.0.1:8000/dashboard/participant/${user.user_id}`
    );

    table.innerHTML = "";

    if (data.length === 0) {
        table.innerHTML = `<tr><td colspan="3">No data available</td></tr>`;
        return;
    }

    data.forEach(item => {
        const statusClass = getStatusClass(item.status);

        table.innerHTML += `
            <tr>
                <td>${item.trial}</td>
                <td>${item.phase}</td>
                <td><span class="status ${statusClass}">${item.status}</span></td>
            </tr>
        `;
    });
}


async function loadAvailableTrials() {
    const data = await fetchData("http://127.0.0.1:8000/trials/");

    const table = document.getElementById("availableTrials");
    if (!table) return;

    table.innerHTML = "";

    data.forEach(t => {
        table.innerHTML += `
            <tr>
                <td>${t.trial_id}</td>
                <td>${t.trial_name}</td>
                <td>${t.phase}</td>
            </tr>
        `;
    });
}

async function applyTrial() {
    const user = getUser();
    const trialId = document.getElementById("applyTrialId").value;

    if (!trialId) return alert("Enter Trial ID");

    await fetch(`http://127.0.0.1:8000/enrollment/apply`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            participant_id: user.user_id,
            trial_id: trialId
        })
    });

    alert("Applied successfully");
}

async function loadMedications() {
    const user = requireRole("participant");
    if (!user) return;

    const table = document.getElementById("medicationTable");
    if (!table) return;

    const data = await fetchData(
        `http://127.0.0.1:8000/dashboard/medication/${user.user_id}`
    );

    table.innerHTML = "";

    if (data.length === 0) {
        table.innerHTML = `<tr><td colspan="3">No medications</td></tr>`;
        return;
    }

    data.forEach(m => {
        table.innerHTML += `
            <tr>
                <td>${m.drug_name}</td>
                <td>${m.dosage}</td>
                <td>${m.frequency}</td>
            </tr>
        `;
    });
}


async function loadVisitSchedule() {
    const user = requireRole("participant");
    if (!user) return;

    const table = document.getElementById("scheduleTable");
    if (!table) return;

    table.innerHTML = `<tr><td colspan="3">Loading...</td></tr>`;

    const data = await fetchData(
        `http://127.0.0.1:8000/dashboard/schedule/${user.user_id}`
    );

    table.innerHTML = "";

    if (data.length === 0) {
        table.innerHTML = `<tr><td colspan="3">No visits scheduled</td></tr>`;
        return;
    }

    data.forEach(v => {
        table.innerHTML += `
            <tr>
                <td>${v.trial}</td>
                <td>${v.visit_date}</td>
                <td>${v.notes || "-"}</td>
            </tr>
        `;
    });
}

async function reportEffect() {
    const user = getUser();

    const trialId = document.getElementById("trialSelect").value;
    const effect = document.getElementById("effectType").value;
    const severity = document.getElementById("severity").value;
    const duration = document.getElementById("duration").value;

    if (!trialId || !effect || !severity || !duration) {
        return alert("Fill all fields");
    }

    await fetch(`http://127.0.0.1:8000/side-effect/report`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            participant_id: user.user_id,
            trial_id: trialId,
            effect_type: effect,
            severity: severity,
            duration: duration
        })
    });

    alert("Reported successfully");

    loadReportedEffects(); // refresh table
}


async function loadReportedEffects() {
    const user = requireRole("participant");
    if (!user) return;

    const table = document.getElementById("effectsTable");
    if (!table) return;

    table.innerHTML = "<tr><td colspan='4'>Loading...</td></tr>";

    const data = await fetchData(
        `http://127.0.0.1:8000/side-effect/participant/${user.user_id}`
    );

    table.innerHTML = "";

    if (data.length === 0) {
        table.innerHTML = "<tr><td colspan='4'>No reports</td></tr>";
        return;
    }

    data.forEach(e => {
        table.innerHTML += `
            <tr>
                <td>${e.trial}</td>
                <td>${e.effect}</td>
                <td>${e.severity}</td>
                <td>${e.duration} days</td>
            </tr>
        `;
    });
}

async function loadParticipantTrialsForReport() {
    const user = requireRole("participant");
    if (!user) return;

    const enrollments = await fetchData(
        `http://127.0.0.1:8000/dashboard/participant/${user.user_id}`
    );

    const trials = await fetchData("http://127.0.0.1:8000/trials/");

    const select = document.getElementById("trialSelect");
    select.innerHTML = "";

    enrollments.forEach(e => {
        const t = trials.find(tr => tr.trial_name === e.trial);
        if (t) {
            select.innerHTML += `
                <option value="${t.trial_id}">
                    ${t.trial_name}
                </option>
            `;
        }
    });
}

async function approveEnrollment(id) {
    await fetch(`http://127.0.0.1:8000/admin/approve/${id}`, {
        method: "PUT"
    });
    loadAdminDashboard();
}

async function rejectEnrollment(id) {
    await fetch(`http://127.0.0.1:8000/admin/reject/${id}`, {
        method: "PUT"
    });
    loadAdminDashboard();
}

async function deleteEnrollment(id) {
    await fetch(`http://127.0.0.1:8000/admin/delete-enrollment/${id}`, {
        method: "DELETE"
    });
    loadAdminDashboard();
}

