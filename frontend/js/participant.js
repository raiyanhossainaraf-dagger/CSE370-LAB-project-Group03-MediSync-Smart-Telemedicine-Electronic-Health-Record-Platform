// frontend/js/participant.js

const user = requireRole("participant");

fetch(`http://127.0.0.1:8000/participants/enrolled/${user.user_id}`)
.then(res => res.json())
.then(data => {

    let html = "";

    if (data.length === 0) {
        html = "<p>No enrollments found</p>";
    }

    data.forEach(e => {
        html += `
        <div class="card">
            <p><b>Trial ID:</b> ${e.trial_id}</p>
            <p><b>Status:</b> ${e.status}</p>
            <p><b>Date:</b> ${e.enrollment_date}</p>
        </div>
        `;
    });

    document.getElementById("enrollments").innerHTML = html;
});