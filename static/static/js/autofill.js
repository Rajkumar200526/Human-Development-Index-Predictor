document.getElementById("country").addEventListener("change", function () {

    const country = this.value;

    if (country === "") return;

    fetch("/country/" + encodeURIComponent(country))

    .then(response => response.json())

    .then(data => {

        document.getElementById("life").value = data.life;

        document.getElementById("expected").value = data.expected;

        document.getElementById("mean").value = data.mean;

        document.getElementById("gni").value = data.gni;

    });

});