// REVERSE THE ORDER OF THE ARRAY
// loop through the array halfway only. 

var myArr = [10,22,31,45,5,10];

function reverseArray(myArr) {
    for ( i = 0; i < myArr.length/2; i++ ){
        var swap = myArr[i];
        myArr[i] = myArr[myArr.length - 1 - i ];
        myArr[myArr.length - 1- i ] = swap;
    }
}
console.log(reverseArray([10,22,31,45,5,10]));

// ROTATE AN ARRAY. 
function rotateArr(arr, moveBy) {
}
    // [1, 2, 3, 4, 5], move to the right by 2
    // [5, 1, 2, 3, 4]  
    /*
        Loop through the amount of rotations needed
            To rotate to the right one:
            1. Create a temp variable that holds the last value.
            2. Move all the items in the array to the right one index.  This is a for loop.
            3. Put the temp value at the beginning of the array.

    */
function rotateArrV2(arr, moveBy) {
    {reverseArr(arr); // Reverse entire array
    var actualMovementsNeeded;
    if (moveBy > 0) {
        actualMovementsNeeded = moveBy % arr.length;
    } else {
        actualMovementsNeeded = Math.abs(moveBy) % arr.length;
    }
    if (moveBy > 0) {
        reverseArr(arr,0,actualMovementsNeeded - 1);
        reverseArr(arr,actualMovementsNeeded, arr.length - 1);
    } else {
        reverseArr(arr,0,arr.length-actualMovementsNeeded - 1);
        reverseArr(arr, arr.length - actualMovementsNeeded,arr.length - 1);
    }
}}

// FILTER RANGE AND ONLY KEEP VALUES IN BETWEEN MIN AND MAX VALUES. 

function filterRangeV2(arr, minVal, maxVal) {
    var nextInd = 0; // Index where the next array value that's from min to max (inclusively) will go
    // Loop through the array
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] >= minVal && arr[i] <= maxVal) {
            arr[nextInd] = arr[i];
            nextInd++; // Increment index for next valid value found
        }
    }
    arr.length = nextInd; // Chop off excess values
}

// CONCAT - COMBINES TWO SEPARATE ARRAYS

function concatArraysV2(arr1, arr2) {
    var newArr = [];
    buildFrom(newArr,arr1); // Add values from first array to the new array
    buildFrom(newArr,arr2); // From second array
    return newArr;
}

function buildFrom(arrayToBuild, arrayFrom) {
    var curInd = arrayToBuild.length; // Starting index
    // Loop to add values to new array
    for (var i = 0; i < arrayFrom.length; i++) {
        arrayToBuild[curInd] = arrayFrom[i];
        curInd++;
    }
}