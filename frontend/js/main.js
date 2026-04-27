// ================= USER AUTH =================

function getUser() {
    return JSON.parse(localStorage.getItem("user"));
}

function requireAuth() {
    const user = getUser();

    if (!user) {
        alert("Please login first");
        window.location.href = "login.html";
    }

    return user;
}

function requireRole(role) {
    const user = requireAuth();

    if (user.role !== role) {
        alert("Access denied");
        window.location.href = "index.html";
    }

    return user;
}

function logout() {
    localStorage.removeItem("user");
    window.location.href = "login.html";
}


// ================= ADMIN DASHBOARD =================

async function loadAdminDashboard() {
    requireRole("admin");

    try {
        const response = await fetch("http://127.0.0.1:8000/dashboard/admin");
        const data = await response.json();

        console.log(data); // DEBUG

        const table = document.getElementById("tableBody"); // FIXED HERE

        if (!table) return;

        table.innerHTML = "";

        data.forEach(item => {
            table.innerHTML += `
                <tr>
                    <td>${item.participant}</td>
                    <td>${item.trial}</td>
                    <td>${item.phase}</td>
                    <td>${item.status}</td>
                    <td>${item.researcher}</td>
                </tr>
            `;
        });

    } catch (error) {
        console.error("Error loading admin dashboard:", error);
    }
}


// ================= RESEARCHER DASHBOARD =================

async function loadResearcherDashboard() {
    const user = requireRole("researcher");

    const response = await fetch(`http://127.0.0.1:8000/dashboard/researcher/${user.user_id}`);
    const data = await response.json();

    const table = document.getElementById("researcher-table");

    if (!table) return;

    table.innerHTML = "";

    data.forEach(item => {
        table.innerHTML += `
            <tr>
                <td>${item.trial}</td>
                <td>${item.phase}</td>
                <td>${item.participant}</td>
                <td>${item.status}</td>
            </tr>
        `;
    });
}


// ================= PARTICIPANT DASHBOARD =================

async function loadParticipantDashboard() {
    const user = requireRole("participant");

    const response = await fetch(`http://127.0.0.1:8000/dashboard/participant/${user.user_id}`);
    const data = await response.json();

    const table = document.getElementById("participant-table");

    if (!table) return;

    table.innerHTML = "";

    data.forEach(item => {
        table.innerHTML += `
            <tr>
                <td>${item.trial}</td>
                <td>${item.phase}</td>
                <td>${item.status}</td>
            </tr>
        `;
    });
}