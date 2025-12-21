function switchTraffic(color) {
  const badge = document.getElementById("activeColor");
  badge.textContent = `Active: ${color.toUpperCase()}`;
  badge.className = `badge ${color}`;

  addLog(`Traffic switch requested → ${color.toUpperCase()}`);
}

// LOGS
function addLog(message) {
  const logs = document.getElementById("logs");
  const time = new Date().toLocaleTimeString();
  logs.textContent = `[${time}] ${message}\n` + logs.textContent;
}

// CHARTS
function createLineChart(ctx, label, color) {
  return new Chart(ctx, {
    type: "line",
    data: {
      labels: ["0s", "10s", "20s", "30s", "40s"],
      datasets: [{
        label,
        data: [0.0, 0.02, 0.02, 0.02, 0.02],
        borderColor: color,
        backgroundColor: color + "33",
        tension: 0.4,
        fill: true
      }]
    },
    options: {
      plugins: { legend: { display: false }},
      scales: {
        x: { ticks: { color: "#9ca3af" }},
        y: { ticks: { color: "#9ca3af" }}
      }
    }
  });
}

createLineChart(
  document.getElementById("blueChart"),
  "Blue CPU",
  "#60a5fa"
);

createLineChart(
  document.getElementById("greenChart"),
  "Green CPU",
  "#34d399"
);

// TRAFFIC DISTRIBUTION
new Chart(document.getElementById("trafficChart"), {
  type: "line",
  data: {
    labels: ["t1", "t2", "t3", "t4", "t5"],
    datasets: [
      {
        label: "Blue Traffic %",
        data: [100, 100, 60, 20, 0],
        borderColor: "#60a5fa",
        fill: true
      },
      {
        label: "Green Traffic %",
        data: [0, 0, 40, 80, 100],
        borderColor: "#34d399",
        fill: true
      }
    ]
  }
});
