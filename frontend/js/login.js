function login() {

    const username = document.getElementById("username").value;

    fetch("http://127.0.0.1:8000/auth/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username: username })
    })
    .then(res => res.json())
    .then(data => {

        if (data.role) {
            localStorage.setItem("user", JSON.stringify(data));

            if (data.role === "admin")
                window.location.href = "admin_dashboard.html";

            if (data.role === "researcher")
                window.location.href = "researcher_dashboard.html";

            if (data.role === "participant")
                window.location.href = "participant_dashboard.html";
        } else {
            alert("Invalid login");
        }
    });
}