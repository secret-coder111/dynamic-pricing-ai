const API_BASE = "http://localhost:8000";

/* ================= DEMAND PREDICTION ================= */
document.getElementById("predict-btn").onclick = async () => {
    const price = Number(document.getElementById("price-input").value);
    const output = document.getElementById("demand-output");

    if (!price || price <= 0) {
        output.innerHTML = "<span style='color:red'>Enter valid price</span>";
        return;
    }

    output.innerText = "Predicting...";

    try {
        const res = await fetch(`${API_BASE}/demand/predict`, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({ price })
        });
        const data = await res.json();
        output.innerHTML = `<strong>${data.demand.toFixed(2)}</strong>`;
    } catch {
        output.innerHTML = "<span style='color:red'>Error</span>";
    }
};

/* ================= STATIC PRICE ================= */
document.getElementById("static-btn").onclick = async () => {
    const out = document.getElementById("static-output");
    out.innerText = "Calculating...";

    try {
        const res = await fetch(`${API_BASE}/pricing/static`);
        const data = await res.json();
        out.innerHTML = `<strong>₹${data.price}</strong>`;
    } catch {
        out.innerText = "Error";
    }
};

/* ================= RL PRICE ================= */
document.getElementById("rl-btn").onclick = async () => {
    const out = document.getElementById("rl-output");
    out.innerText = "Learning...";

    try {
        const res = await fetch(`${API_BASE}/pricing/rl`);
        const data = await res.json();
        out.innerHTML = `<strong>₹${data.price}</strong>`;
    } catch {
        out.innerText = "Error";
    }
};

/* ================= CSV UPLOAD ================= */
document.getElementById("upload-btn").onclick = async () => {
    const fileInput = document.getElementById("csv-file");
    const status = document.getElementById("upload-status");

    if (!fileInput.files.length) {
        status.innerHTML = "<span style='color:red'>Select a CSV file</span>";
        return;
    }

    status.innerText = "Uploading & retraining...";

    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    try {
        const res = await fetch(`${API_BASE}/data/upload-data`, {
            method: "POST",
            body: formData
        });
        const data = await res.json();
        status.innerHTML = `<span style='color:green'>${data.message}</span>`;
        plotPriceComparison();
    } catch {
        status.innerHTML = "<span style='color:red'>Upload failed</span>";
    }
};

/* ================= PRICE COMPARISON ================= */
let comparisonChart = null;

async function plotPriceComparison() {
    try {
        const ml = await (await fetch(`${API_BASE}/pricing/static`)).json();
        const rl = await (await fetch(`${API_BASE}/pricing/rl`)).json();

        const ctx = document.getElementById("priceComparisonChart").getContext("2d");
        if (comparisonChart) comparisonChart.destroy();

        comparisonChart = new Chart(ctx, {
            type: "bar",
            data: {
                labels: ["ML Price", "RL Price"],
                datasets: [{
                    data: [ml.price, rl.price],
                    backgroundColor: ["#7c3aed", "#2563eb"]
                }]
            },
            options: {
                plugins: { legend: { display: false } },
                scales: { y: { beginAtZero: true } }
            }
        });
    } catch {
        console.error("Comparison error");
    }
}

window.onload = plotPriceComparison;
