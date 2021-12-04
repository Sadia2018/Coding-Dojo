function pushVariable(array, newValue){
    array[array.length] = newValue
    return array
}

arrayExample=[1,2,3,4]
console.log(pushVariable(arrayExample,5))

function loop(limit){
    for(i=0; i<limit ;i++){
        console.log(i)
    }
}

loop(5)