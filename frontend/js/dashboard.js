const user = JSON.parse(localStorage.getItem("user"));

if (!user) {
    window.location.href = "login.html";
}

// Researcher
if (user.role === "researcher") {

    fetch(`http://127.0.0.1:8000/dashboard/researcher/${user.user_id}`)
    .then(res => res.json())
    .then(data => {

        let html = "";

        data.forEach(d => {
            html += `
            <tr>
                <td>${d.trial_name}</td>
                <td>${d.phase}</td>
                <td>${d.participant_name}</td>
                <td>${d.age}</td>
                <td>${d.gender}</td>
                <td>${d.status}</td>
            </tr>`;
        });

        document.getElementById("tableBody").innerHTML = html;
    });
}

// Participant
if (user.role === "participant") {

    fetch(`http://127.0.0.1:8000/dashboard/participant/${user.user_id}`)
    .then(res => res.json())
    .then(data => {

        let html = "";

        data.forEach(d => {
            html += `
            <tr>
                <td>${d.trial_name}</td>
                <td>${d.phase}</td>
                <td>${d.status}</td>
            </tr>`;
        });

        document.getElementById("tableBody").innerHTML = html;
    });
}