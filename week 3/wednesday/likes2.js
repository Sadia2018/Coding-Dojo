var count1 = document.querySelector("#count")
var numLikesCount = 3
function likeBtn(element){
    numLikesCount++
    count1.innerText = numLikesCount
}

var count2 = document.querySelector("#increase")
var numLikesIncrease = 3
function likeBtn1(element){
    numLikesIncrease++
    count2.innerText = numLikesIncrease
}

var count = document.querySelector("#likeMore")
var numLikesLikeMore = 3
function likeBtn2(element){
    numLikesLikeMore++
    count.innerText = numLikesLikeMore
}
