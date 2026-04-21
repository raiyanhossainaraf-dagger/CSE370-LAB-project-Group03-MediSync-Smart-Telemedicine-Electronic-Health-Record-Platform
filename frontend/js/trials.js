fetch("http://127.0.0.1:8000/trials/")
.then(response => response.json())
.then(data => {

    let rows = "";

    data.forEach(trial => {
        rows += `
        <tr>
            <td>${trial.trial_id}</td>
            <td>${trial.trial_name}</td>
            <td>${trial.drug_name}</td>
            <td>${trial.phase}</td>
        </tr>
        `;
    });

    document.getElementById("trialTable").innerHTML = rows;
});