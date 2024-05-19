
document.getElementById('toggleButton').addEventListener('click', function() {
    const describeImage = document.getElementById('describeRefImg') ;
    const button = document.getElementById('toggleButton') ;

    describeImage.style.opacity = 1 ; // Make the image opaque
    button.classList.add('hidden') ;  // Hide the button
}) ;



/////////////////////////////////////////////////////



document.getElementById("submit-btn").addEventListener("click", function(event) {
    event.preventDefault(); // Prevent the form from submitting immediately

    // Get form fields
    var form = document.getElementById("diabetes-form");
    var pregnancies = form.pregnancies.value;
    var glucose = form.glucose.value;
    var diastolic = form.diastolic.value;
    var triceps = form.triceps.value;
    var insulin = form.insulin.value;
    var bmi = form.bmi.value;
    var dpf = form.dpf.value;
    var age = form.age.value;

    // Check if all fields are filled
    if (pregnancies && glucose && diastolic && triceps && insulin && bmi && dpf && age) {
        // All fields are filled, proceed with GIF display and form submission
        let resultDiv = document.getElementById("resultdiv");
        resultDiv.style.backgroundImage = "url('/static/images/FOURTH-DESIGN/fourthDesignGif.gif')";

        setTimeout(function() {
            // resultDiv.style.backgroundImage = "url('/static/images/endingPic.png')";
            form.submit(); // Submit the form after the GIF is shown
        }, 7000);
    } else {
        // If any field is empty, alert the user
        alert("Please fill in all the fields before submitting.");
    }

    
});

const resultText = document.getElementById('result-text').innerHTML ;
const resultDiv = document.getElementById('resultdiv') ;
const body = document.querySelector('body') ;
if(resultText == "Diabetic" || resultText == "Non-Diabetic"){
    resultDiv.style.backgroundImage = "url('/static/images/FOURTH-DESIGN/endingPic.png')" ;
    
}
