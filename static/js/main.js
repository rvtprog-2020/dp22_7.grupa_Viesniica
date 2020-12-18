username = 'Guest'

function Login() {
    let log = document.getElementById("log").value;
    let pass = document.getElementById("pass").value;

    if (log == "admin") {
        if (pass == "admin") {
            document.location.href = "/";
            username = 'Admin';
        }
    }
    else if (log == "client") {
        if (pass == "client") {
            document.location.href = "/";
            username = 'Client';
        }
    }
    else {
        document.location.href = "/sign_in";
    }
}

function sign_out() {
    document.location.href = "/"
    username = "Guest"
}

function Chose1() {
    if (username == "Client" || useername == "Admin") {
        document.location.href = "/"
    }
    else {
        document.location.href = "/"
    }
}