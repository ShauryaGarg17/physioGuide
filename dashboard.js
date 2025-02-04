// ...existing code...

// Function to redirect to exercise page
function redirectToExercisePage() {
  window.location.href = '/exercise-page';
}

// Add event listener to the "chest" button
document.getElementById('chest-button').addEventListener('click', redirectToExercisePage);

// ...existing code...
