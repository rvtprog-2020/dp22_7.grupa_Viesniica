username = 'Guest'

function Login() {
    let log = document.getElementById("log").value;
    let pass = document.getElementById("pass").value;

    if (log == "admin") {
        if (pass == "admin") {
            username = 'Admin';
            document.location.href = "/mainpage2.html";
        }
    }
    if (log == "client") {
        if (pass == "client") {
            username = 'Client';
            document.location.href = "/mainpage2.html";
        }

    }
    else {
        document.location.href = "/sign_in.html";
    }
}

