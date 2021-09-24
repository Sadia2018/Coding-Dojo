var btn = document.getElementById("btn-change")
function logOut(element) {
    if (btn.innerText == "LOGIN") {
        btn.innerText = "LOGOUT"
    } else {
        btn.innerText = "LOGIN"
    }
}

function vanish(element) {
    element.remove()
}

function popUp(element) {
    alert("Ninja was liked")
}