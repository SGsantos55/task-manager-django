document.addEventListener("DOMContentLoaded", function () {
    // Error handling for incorrect login (if needed for front-end validation)
    let form = document.querySelector('form');
    let username = document.getElementById('username');
    let password = document.getElementById('password');

    form.addEventListener('submit', function(event) {
        if (!username.value || !password.value) {
            event.preventDefault();  // Prevent form submission
            alert('Please fill in both fields');
        }
    });
});
