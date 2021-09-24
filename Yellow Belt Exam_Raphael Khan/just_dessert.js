function remove(element) {
    element.remove()
}

var increaseThis1 = document.getElementById("moreLikes")
var numLikes1 = 68
function like1() {
    numLikes1++
    increaseThis1.innerText = numLikes1
}

var increaseThis2 = document.getElementById("macarons_like")
var numLikes2 = 212
function like2() {
    numLikes2++
    increaseThis2.innerText = numLikes2
}

var increaseThis3 = document.getElementById("creme_brule_like")
var numLikes3 = 33
function like3() {
    numLikes3++
    increaseThis3.innerText = numLikes3
}

function search(event) {
    event.preventDefault()
    var searchTerm = document.getElementById("searchBar").value
    alert(`You are searching for "${searchTerm}"`)
}