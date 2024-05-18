
document.getElementById('toggleButton').addEventListener('click', function() {
    const describeImage = document.getElementById('describeRefImg') ;
    const button = document.getElementById('toggleButton') ;

    describeImage.style.opacity = 1 ; // Make the image opaque
    button.classList.add('hidden') ;  // Hide the button
}) ;