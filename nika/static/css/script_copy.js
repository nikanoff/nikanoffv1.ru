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