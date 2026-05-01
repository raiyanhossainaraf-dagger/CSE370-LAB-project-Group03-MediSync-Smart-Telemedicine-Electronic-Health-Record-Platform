
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

    const data = await fetchData("http://127.0.0.1:8000/dashboard/admin");

    if (data.length === 0) {
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
                    <button onclick="updateStatus(${item.enrollment_id}, 'Approved')" class="btn-approve">Approve</button>
                    <button onclick="updateStatus(${item.enrollment_id}, 'Rejected')" class="btn-reject">Reject</button>
                    <button onclick="deleteTrial(${item.trial_id})" class="btn-delete">Delete</button>
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

    const participantsInput = document.getElementById("participants").value;

    const participant_ids = participantsInput
        .split(",")
        .map(id => parseInt(id.trim()))
        .filter(id => !isNaN(id));

    try {
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

        const data = await response.json();

        if (!response.ok) {
            alert(data.detail);
            return;
        }

        showToast("Trial created");
        window.location.href = "admin_dashboard.html";

    } catch (err) {
        console.error(err);
        alert("Failed to create trial");
    }
}


// ================= UPDATE STATUS =================

async function updateStatus(id, status) {
    try {
        const response = await fetch(
            `http://127.0.0.1:8000/enrollment/update-status/${id}?status=${status}`,
            { method: "PUT" }
        );

        if (!response.ok) throw new Error();

        showToast("Status updated");
        loadAdminDashboard();

    } catch (err) {
        console.error(err);
        alert("Update failed");
    }
}


// ================= DELETE TRIAL =================

async function deleteTrial(trial_id) {

    if (!confirm("Delete this trial?")) return;

    try {
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

    } catch (err) {
        console.error(err);
        alert("Delete failed");
    }
}


// ================= LOAD RESEARCHERS =================

async function loadResearchers() {
    const user = requireRole("admin");
    if (!user) return;

    const table = document.getElementById("researcherTable");
    if (!table) return;

    table.innerHTML = `<tr><td colspan="4">Loading...</td></tr>`;

    const data = await fetchData("http://127.0.0.1:8000/admin/researchers");

    table.innerHTML = "";

    data.forEach(r => {
        table.innerHTML += `
            <tr>
                <td>${r.id}</td>
                <td>${r.name}</td>
                <td>${r.specialization || "-"}</td>
                <td>${r.email || "-"}</td>
            </tr>
        `;
    });
}


// ================= LOAD PARTICIPANTS =================

async function loadParticipants() {
    const user = requireRole("admin");
    if (!user) return;

    const table = document.getElementById("participantTable");
    if (!table) return;

    table.innerHTML = `<tr><td colspan="5">Loading...</td></tr>`;

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
            </tr>
        `;
    });
}