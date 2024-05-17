// Function to toggle between light and dark themes
function toggleTheme() {
    const currentTheme = localStorage.getItem('theme') || 'light';
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';

    // Update the theme
    document.documentElement.setAttribute('data-theme', newTheme);

    // Update the theme-specific CSS file
    const themeLink = document.getElementById('theme-link');
    themeLink.href = `/static/css/${newTheme}.css`;

    // Update the theme toggle button text and icon
    const themeToggleButton = document.getElementById('theme-toggle-button');
    themeToggleButton.checked = newTheme === 'dark';
    themeToggleButton.innerHTML = newTheme === 'dark' ? '<i class="fas fa-sun"></i> Light Mode' : '<i class="fas fa-moon"></i> Dark Mode';

    // Store the theme preference in local storage
    localStorage.setItem('theme', newTheme);
}


function copyUrl(url, button) {
    navigator.clipboard.writeText(url)
        .then(() => {
            toggleShareState(button);
        })
        .catch((error) => {
            console.error('Failed to copy URL:', error);
        });
}

function toggleShareState(button) {
    const shareIcon = button.querySelector('.share');
    const checkmarkIcon = button.querySelector('.checkmark');

    shareIcon.style.display = 'none';
    checkmarkIcon.style.display = 'inline-block';

    setTimeout(() => {
        shareIcon.style.display = 'inline-block';
        checkmarkIcon.style.display = 'none';
    }, 2000);
}



