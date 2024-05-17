// Check for saved theme in local storage on page load
window.onload = function() {
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', savedTheme);
    document.getElementById('theme-link').href = `/static/css/${savedTheme}.css`;
    document.getElementById('theme-toggle-button').checked = savedTheme === 'dark';
    document.getElementById('theme-toggle-button').innerHTML = savedTheme === 'dark' ? '<i class="fas fa-sun"></i> Light Mode' : '<i class="fas fa-moon"></i> Dark Mode';
};  