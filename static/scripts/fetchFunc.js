export function loadLastTemperature() {
    fetch("/api/last")
        .then(response => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          return response.json(); // This returns a Promise
        })
        .then(data => {
          const lastTemperatureContainer = document.getElementById("last_temperature");
          lastTemperatureContainer.textContent = data.value; // Display the JSON data
        })
        .catch(error => {
          // Handle errors
          console.error('There was a problem with the fetch operation:', error);
        });
}

export function loadAllTemperatures() {
    const tableBody = document.getElementsByTagName("tbody")[0];
    fetch("/api/get_all_temps")
        .then(response => {
          if (!response.ok)
            throw new Error('Network response was not ok');

          loadNumberOfRecords();
          return response.json();
        })
        .then(data => {
            fillTableBodyWith(data);
        })
        .catch(error => {
          // Handle errors
          console.error('There was a problem with the fetch operation:', error);
        });
}

export function load_N() {
    const tableBody = document.getElementsByTagName("tbody")[0];
    const loadLast_n_Input = document.getElementById("load_n_input");

    const number = parseInt(loadLast_n_Input.value);
    if (isNaN(number) || number < 0) {
        throw new Error("Invalid value!");
    }

    fetch("/api/last/" + number)
        .then(response => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }

          // loadNumberOfRecords();
          return response.json(); // This returns a Promise
        })
        .then(data => {
            fillTableBodyWith(data);
        })
        .catch(error => {
          // Handle errors
          console.error('There was a problem with the fetch operation:', error);
        });
}

export function delete_last_N() {
    const deleteLast_n_Input = document.getElementById("delete_n_input");
    const number = parseInt(deleteLast_n_Input.value);
    if (isNaN(number) || number < 0) {
        throw new Error("Invalid value!");
    }

    fetch("/api/delete_oldest/" + number, {
                    method: 'POST'
        })
        .then(response => {
            if (!response.ok)
                throw new Error('Network response was not ok');

            loadNumberOfRecords();
            return response.json();
        })
        .then(data => {
            fillTableBodyWith(data);
        })
        .catch(error => {
          // Handle errors
          console.error('There was a problem with the fetch operation:', error);
        });
}

function loadNumberOfRecords() {
    const numberOfRecords_Bold = document.getElementById("n_of_records");
    fetch("/api/number_of_records")
        .then(response => {
            if (response.status !== 200) {
                throw new Error("Network response was not ok!");
            }
            return response.json();
        })
        .then(data => {
            numberOfRecords_Bold.innerText = data.value;
        })
        .catch(error => {
          // Handle errors
          console.error('There was a problem with the fetch operation:', error);
        });
}

function fillTableBodyWith(temperatures) {
    const tableBody = document.getElementsByTagName("tbody")[0];
    tableBody.replaceChildren();

    for (const record of temperatures) {
          const row = document.createElement("tr");
          const timeCell = document.createElement("td");
          timeCell.innerText = record.timestamp;
          const valueCell = document.createElement("td");
          valueCell.innerText = record.value;
          const deleteCell = document.createElement("td");
          const deleteBtn = document.createElement("button");
          deleteBtn.onclick = function () {
              fetch("/api/delete/" + record.timestamp)
                  .then(response => {
                      if (response.status === 200) {
                          console.log(`Record ${record.timestamp} successfully deleted`);
                          loadAllTemperatures();
                      } else {
                          console.log("Deletion was unsuccessful. Status " + response.status);
                      }
                  })
          };
          deleteBtn.classList.add("btn", "btn-primary");
          deleteBtn.innerText = "Delete";
          deleteCell.appendChild(deleteBtn);
          row.append(timeCell, valueCell, deleteCell);
          tableBody.appendChild(row);
      }
}