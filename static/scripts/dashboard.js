import {loadLastTemperature, loadAllTemperatures, load_N, delete_last_N} from "./fetchFunc.js";

const lastTemperatureParagraph = document.getElementById("last_temperature");
const loadLast_n_Button = document.getElementById("load_n_button");
const loadAll_Button = document.getElementById("load_all_button");
const deleteLast_n_Button = document.getElementById("delete_n_button");
const table = document.getElementById("table");
const tableBody = table.querySelector("tbody");



function initPage() {
    loadLastTemperature();
    loadAllTemperatures();
    console.log("initialized");
}

loadLast_n_Button.onclick = load_N;
loadAll_Button.onclick = loadAllTemperatures;
deleteLast_n_Button.onclick = delete_last_N;

window.onload = initPage;
