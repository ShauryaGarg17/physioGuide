// ...existing code...

firebase.auth().onAuthStateChanged(user => {
    if (!user) {
        // User is not logged in, redirect to home page
        window.location.href = '/';
    }
});

// ...existing code...
