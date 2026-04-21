function login() {

fetch("http://127.0.0.1:8000/auth/login", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        username: document.getElementById("username").value,
        password: document.getElementById("password").value
    })
})

.then(response => response.json())
.then(data => {
    document.getElementById("result").innerText = data.message;
});

}