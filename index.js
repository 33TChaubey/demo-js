function linearsearch(arr, x){
    for (let i=0; i<arr.length; i++){
        if (arr[i] == x){
            return i
        }
    }
    return -1
}

function binarysearch(arr, x){
    let low = 0
    let high = arr.length - 1
    while (low <= high){
        let mid = Math.floor((low + high)/2)
        if (arr[mid] == x){
            return mid
        }
        else if (arr[mid] < x){
            low = mid + 1
        }
        else {
            high = mid - 1
        }
    }
    return -1
}

console.log("ending search")
module.exports = {linear:linearsearch, binary:binarysearch};