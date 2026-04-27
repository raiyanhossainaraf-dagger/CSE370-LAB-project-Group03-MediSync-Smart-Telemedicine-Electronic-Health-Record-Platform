fetch("http://127.0.0.1:8000/trials/")
.then(res => res.json())
.then(data => {

    let rows = "";

    data.forEach(t => {
        rows += `
        <tr>
            <td>${t.trial_id}</td>
            <td>${t.trial_name}</td>
            <td>${t.drug_name}</td>
            <td>${t.phase}</td>
        </tr>`;
    });

    document.getElementById("trialTable").innerHTML = rows;
});