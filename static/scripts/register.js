const registerBtn = document.getElementById("registration-btn");
const loginInput = document.getElementById("login_input");
const passwordInput = document.getElementById("password_input");


function register() {
    const login = loginInput.value;
    const password = passwordInput.value;

    fetch("/api/register?login=" + login + "&password=" + password)
        .then(response => {
            if (response.ok)
                return response.json();
        })
        .then(data => {

        })

}

registerBtn.onclick = register;