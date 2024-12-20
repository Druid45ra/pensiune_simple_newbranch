// static/js/scripts.js

document.addEventListener("DOMContentLoaded", function() {
    const rezervareForm = document.querySelector("form");
    rezervareForm.addEventListener("submit", function(event) {
        const dataSosire = document.getElementById("data_sosire").value;
        const dataPlecare = document.getElementById("data_plecare").value;

        if (new Date(dataSosire) >= new Date(dataPlecare)) {
            alert("Data sosirii trebuie să fie înainte de data plecării.");
            event.preventDefault(); // Previne trimiterea formularului
        }
    });
});