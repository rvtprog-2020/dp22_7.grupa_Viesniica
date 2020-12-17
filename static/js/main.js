username = 'Guest'

function Login() {
    let log = document.getElementById("log").value;
    let pass = document.getElementById("pass").value;

    if (log == "admin") {
        if (pass == "admin") {
            document.location.href = "/mainpage2.html";
            username = 'Admin';
        }
    }
    else if (log == "client") {
        if (pass == "client") {
            document.location.href = "/mainpage2.html";
            username = 'Client';
        }
    }
    else {
        document.location.href = "/sign_in.html";
    }
}

function sign_out() {
    document.location.href = "/"
    username = "Guest"
}

function Chose1() {
    if (username == "Client" || useername == "Admin") {
        document.location.href = "/mainpage2.html"
    }
    else {
        document.location.href = "/catologue.html"
    }
}