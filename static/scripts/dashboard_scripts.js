function getInputValue(value) {
    const elem = document.getElementById(value);
    return elem.value;
}

function loadTemperatures() {
    const value = getInputValue("load_n_input");
    const intValue = parseInt(value);
    if (isNaN(intValue)) {temp
        console.log("Error! Input value is NaN");
        const input = document.getElementById("load_n_div");
        const warningP = document.createTextNode("Invalid data!");
        input.after(warningP);
    } else {
        load_n(tempHandler);
        // console.log(data);
    }
}

function load_n(callback) {

    const value = getInputValue("load_n_input");

    const xhr = new XMLHttpRequest();
    const url = "/api/last/" + value;

    xhr.open("GET", url, true);

    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            // Request was successful, parse JSON response
            var data = JSON.parse(xhr.responseText);

            // Do something with the JSON data
            // console.log(data);
            callback(data);
        } else if (xhr.readyState === 4) {
            // Request failed
            console.error('Error fetching data. Status:', xhr.status);
        }
    };

    xhr.send();
}

function tempHandler(data) {
    console.log("From tempHandler:");
    console.log(data);
}