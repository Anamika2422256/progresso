function changeTheme(color) {
    localStorage.setItem("themeColor", color);
    document.documentElement.style.setProperty('--primary', color);
}

// Apply saved theme on page load
window.onload = function () {
    const savedColor = localStorage.getItem("themeColor");
    if (savedColor) {
        document.documentElement.style.setProperty('--primary', savedColor);
    }
};