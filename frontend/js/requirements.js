function saveRequirements() {
    const selected = [];

    document.querySelectorAll('input[type="checkbox"]:checked')
        .forEach(cb => selected.push(cb.value));

    if (selected.length === 0) {
        alert("Please select at least one testing requirement.");
        return;
    }

    localStorage.setItem("testingRequirements", JSON.stringify(selected));

    // Go to next step
    window.location.href = "standards.html";
}

/* =========================
   Back Navigation
========================= */
function goBack() {
    window.history.back();
}