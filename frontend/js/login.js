function login() {

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    if (!username || !password) {
        alert("Please enter username and password");
        return;
    }

    fetch("http://127.0.0.1:8000/auth/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            username: username,
            password: password
        })
    })
    .then(res => res.json())
    .then(data => {

        if (data.role) {

            // Save session properly
            localStorage.setItem("role", data.role);
            localStorage.setItem("user_id", data.user_id);
            localStorage.setItem("name", data.name);

            // Redirect
            if (data.role === "admin") {
                window.location.href = "admin_dashboard.html";
            }
            else if (data.role === "researcher") {
                window.location.href = "researcher_dashboard.html";
            }
            else if (data.role === "participant") {
                window.location.href = "participant_dashboard.html";
            }

        } else {
            alert("Invalid login");
        }
    })
    .catch(err => {
        console.error(err);
        alert("Server error");
    });
}