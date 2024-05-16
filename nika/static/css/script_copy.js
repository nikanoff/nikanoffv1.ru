// function copyUrl(url) {
//     navigator.clipboard.writeText(url)
//         .then(() => {
//             // URL copied successfully
//         })
//         .catch((error) => {
//             console.error('Failed to copy URL:', error);
//         });
// }

// document.querySelectorAll('.copy-btn').forEach(button => {
//     button.addEventListener('click', function() {
//         const path = this.getAttribute('data-path');
//         const url = window.location.origin + path; // Construct full URL with domain and protocol
//         copyUrl(url);
//         toggleCopyState(this);
//     });
// });

// function toggleCopyState(button) {
//     const copyIcon = button.querySelector('.copy-icon');
//     const checkmarkIcon = button.querySelector('.checkmark-icon');

//     copyIcon.style.display = 'none';
//     checkmarkIcon.style.display = 'inline-block';

//     setTimeout(() => {
//         copyIcon.style.display = 'inline-block';
//         checkmarkIcon.style.display = 'none';
//     }, 2000);
// }


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