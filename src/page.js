firebase.auth().onAuthStateChanged(user => {
  if (user) {
    console.log('User is logged in:', user);
    // ...existing code...
  } else {
    console.log('User is not logged in, redirecting to home page');
    window.location.href = '/';
  }
});

try {
  // ...existing code...
} catch (error) {
  if (error.code === 'permission-denied') {
    console.error('FirebaseError: Missing or insufficient permissions.');
    alert('You do not have permission to perform this action.');
  } else {
    console.error('An unexpected error occurred:', error);
  }
}
