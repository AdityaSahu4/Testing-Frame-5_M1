const fileInput = document.getElementById("docs");
const fileList = document.getElementById("fileList");

// Show selected file names
fileInput.addEventListener("change", () => {
    fileList.innerHTML = "";

    Array.from(fileInput.files).forEach(file => {
        const li = document.createElement("li");
        li.textContent = file.name;
        fileList.appendChild(li);
    });
});

// Save docs and move to next page
function saveDocs() {
    if (fileInput.files.length === 0) {
        alert("Please upload at least one document.");
        return;
    }

    const documents = Array.from(fileInput.files).map(file => ({
        name: file.name,
        url: `local://${file.name}`  // placeholder URL for now
    }));

    localStorage.setItem("technicalDocs", JSON.stringify(documents));

    // Go to next step
    window.location.href = "requirements.html";
}

/* =========================
   Back Navigation
========================= */
function goBack() {
    window.history.back();
}
