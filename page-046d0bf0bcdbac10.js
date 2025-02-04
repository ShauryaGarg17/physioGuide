// ...existing code...

firebase.auth().onAuthStateChanged(user => {
    if (user) {
        console.log('User is logged in:', user.uid);
        // ...existing code...
    } else {
        console.log('User is not logged in, redirecting to home page');
        window.location.href = '/';
    }
});

// Add error handling for Firebase errors
someFirebaseFunction().catch(error => {
    if (error.code === 'permission-denied') {
        console.error('FirebaseError: Missing or insufficient permissions.');
    } else {
        console.error('FirebaseError:', error.message);
    }
});

// ...existing code...
