async function loadTrials() {

    const table = document.getElementById("trialTable");
    if (!table) return;

    table.innerHTML = "<tr><td colspan='4'>Loading...</td></tr>";

    try {
        const res = await fetch("http://127.0.0.1:8000/trials/");
        const data = await res.json();

        table.innerHTML = "";

        if (!data || data.length === 0) {
            table.innerHTML = "<tr><td colspan='4'>No trials found</td></tr>";
            return;
        }

        data.forEach(t => {
            table.innerHTML += `
                <tr>
                    <td>${t.trial_id}</td>
                    <td>${t.trial_name}</td>
                    <td>${t.drug_name}</td>
                    <td>${t.phase}</td>
                </tr>
            `;
        });

    } catch (err) {
        console.error(err);
        table.innerHTML = "<tr><td colspan='4'>Error loading trials</td></tr>";
    }
}