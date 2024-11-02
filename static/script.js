// JavaScript to handle the dark mode toggle
document.addEventListener("DOMContentLoaded", function () {
    const toggle = document.getElementById("toggle");
    
    // Check if dark mode was previously enabled
    if (localStorage.getItem("dark-mode") === "enabled") {
        document.body.classList.add("dark-mode");
        toggle.checked = true;
    }

    // Listen for toggle switch changes
    toggle.addEventListener("change", function () {
        if (toggle.checked) {
            document.body.classList.add("dark-mode");
            localStorage.setItem("dark-mode", "enabled");
        } else {
            document.body.classList.remove("dark-mode");
            localStorage.setItem("dark-mode", "disabled");
        }
    });
});
