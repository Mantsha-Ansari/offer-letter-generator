AOS.init();

function generateOfferLetter() {
    // Collect form data
    const name = document.getElementById('name').value;
    const position = document.getElementById('position').value;
    const salary = document.getElementById('salary').value;
    const joiningDate = document.getElementById('joiningDate').value;
    const email = document.getElementById('email').value;

    const formData = new FormData();
    formData.append('name', name);
    formData.append('position', position);
    formData.append('salary', salary);
    formData.append('joining_date', joiningDate);
    formData.append('email', email);

    fetch('http://127.0.0.1:5000/add_candidate', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);  // Show success message
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function previewOfferLetter() {
    let name = prompt("Enter the candidate's name to preview:");
    if (!name) return;

    // Open file in new tab
    window.open(`http://127.0.0.1:5000/preview_offer_letter?name=${encodeURIComponent(name)}`, '_blank');
}

// send email
function sendEmail() {
    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let statusText = document.getElementById("emailStatus");

    if (!name || !email) {
        alert("Please enter candidate's name and email!");
        return;
    }

    fetch('http://127.0.0.1:5000/send_email', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name: name, email: email })
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            statusText.innerText = "✅ " + data.message;
        } else {
            statusText.innerText = "❌ " + data.error;
        }
    })
    .catch(error => {
        console.error("Error:", error);
        statusText.innerText = "❌ Error sending email.";
    });
}

   