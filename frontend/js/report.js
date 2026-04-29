fetch("http://127.0.0.1:8000/reports/summary")
.then(res => res.json())
.then(data => {
    document.getElementById("trials").innerText = data.total_trials;
    document.getElementById("participants").innerText = data.total_participants;
})
.catch(err => {
    console.log(err);
    document.getElementById("trials").innerText = "Error";
    document.getElementById("participants").innerText = "Error";
});