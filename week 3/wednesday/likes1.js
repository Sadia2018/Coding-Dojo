var count = document.querySelector("#count")
var numLikes = 3
function likeBtn() {
    numLikes++
    count.innerText = numLikes
}