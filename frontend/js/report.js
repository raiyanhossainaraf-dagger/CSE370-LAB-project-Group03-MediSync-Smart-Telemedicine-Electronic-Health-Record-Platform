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

async function submitReport() {
    const user = requireRole("researcher");
    if (!user) return;

    const trial = document.getElementById("repTrial").value;
    const summary = document.getElementById("summary").value;
    const result = document.getElementById("result").value;

    if (!trial || !summary || !result) {
        return alert("Fill all fields");
    }

    const res = await fetch("http://127.0.0.1:8000/dashboard/report", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            trial_id: parseInt(trial),
            researcher_id: user.user_id,
            summary: summary,
            result: result
        })
    });

    const data = await res.json();
    alert(data.message);
}