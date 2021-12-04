// ADD TO THE FRONT OF AN ARRAY

// var arr = [5,8,10,12]
// arr[4] = arr[3]
// arr[3] = arr[2]
// arr[2] = arr[1]
// arr[1] = arr[0]
// arr[0] = 25

for ( i = 0; i < arr.length; i++)
    {
        arr[arr.length - i] = arr[arr.length - 1 - i]
    }
arr[0] = 40
console.log(arr)

// MAKE IT POP AT THE FRONT 
var arr = [5,8,10,12]
var aux = arr[0]


function popFront(arr){
    for (i = 0; i < arr.length - 1; i++)
    {
        arr[i] = arr[i +1];
    }
        console.log(arr)
        console.log(aux)
}

popFront(arr);


//PUSH A NEW VALUE AT A GIVEN INDEX 
function pushVariable(array,index,newValue){
    array[index] = newValue
    return array
}

console.log(pushVariable(arr,2,20))

function popFront(arr){
    var newArray = []
    // newArray.length = arr.length - 1
    for (i = 0; i < arr.length - 1; i++)
    {
        newArray[i] = arr[i +1];
    }
    return newArray
}
console.log(popFront(arr))

