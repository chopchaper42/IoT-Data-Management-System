const lastTemperatureParagraph = document.getElementById("last_temperature");
const loadLast_n_Button = document.getElementById("load_n_button");
const loadLast_n_Input = document.getElementById("load_n_input");
const deleteLast_n_Button = document.getElementById("delete_n_button");
const deleteLast_n_Input = document.getElementById("delete_n_input");
const loadAll_Button = document.getElementById("load_all_button");
const numberOfRecords_Bold = document.getElementById("n_of_records");
const table = document.getElementById("table");

function getLastTemperature() {
    const xhr = new XMLHttpRequest();
    const url = "/api/last/";

    xhr.open("GET", url, true);

    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            // Request was successful, parse JSON response
            var data = JSON.parse(xhr.responseText);

            // Do something with the JSON data
            // console.log(data);
            lastTemperatureParagraph.innerHTML = "<b>" + data["value"] + "</b>";
        } else if (xhr.readyState === 4) {
            // Request failed
            console.error('Error fetching data. Status:', xhr.status);
        }
    };

    xhr.send();
}