username = 'Guest'

let inouts = document.getElementById("inout") 

function Login() {
    let log = document.getElementById("log").value;
    let pass = document.getElementById("pass").value;


    if (log == "admin") {
        if (pass == "admin") {
            document.location.href = "/";
            username = 'Admin';
            document.inouts.innerHTML = "Sign Out"
        }
    }
    else if (log == "client") {
        if (pass == "client") {
            document.location.href = "/";
            username = 'Client';
            document.inouts.innerHTML = "Sign Out"
        }
    }
    else {
        document.location.href = "/sign_in";
        document.inouts.innerHTML = "Sign In"

    }
}

function sign_out() {
    if (username) {
        document.location.href = "/"
        username = "Guest"
    }
    
}

function Chose1() {
    if (username == "Client" || useername == "Admin") {
        document.location.href = "/"
        document.inouts.innerHTML = "Sign Out"
    }
    else {
        document.location.href = "/"
        document.inouts.innerHTML = "Sign In"
    }
}