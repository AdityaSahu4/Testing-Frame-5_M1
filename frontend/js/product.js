function saveProduct() {
    const category = document.getElementById("category").value;
    const type = document.getElementById("type").value;
    const power = document.getElementById("power").value;

    if (!category || !type || !power) {
        alert("Please fill all product details.");
        return;
    }

    const productDetails = {
        category,
        type,
        power
    };

    localStorage.setItem("productDetails", JSON.stringify(productDetails));

    // Go to next step
    window.location.href = "tsd.html";
}

/* =========================
   Back Navigation
========================= */
function goBack() {
    window.history.back();
}
