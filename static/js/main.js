username = "Guest"

function getInfo() {
    let login = document.getElementById('login').value
    let mail = document.getElementById('mail').value
    let password = document.getElementById('password').value


};

async function sendMsg(msgText, msgUser = "Admin"){
    let data = JSON.stringify({"user":msgUser, "msg":msgText})

    let response = await fetch('/sign_up',{
        method: 'POST',
        headers: {'Content-Type':'application/json'},
        body: data
    })

    readChat()
}


