function saveStandards() {
    const selected = [];

    document.querySelectorAll('input[type="checkbox"]:checked')
        .forEach(cb => selected.push(cb.value));

    if (selected.length === 0) {
        alert("Please select at least one testing standard.");
        return;
    }

    localStorage.setItem("testingStandards", JSON.stringify(selected));

    // Go to final page
    window.location.href = "quotation.html";
}
/* =========================
   Back Navigation
========================= */
function goBack() {
    window.history.back();
}
