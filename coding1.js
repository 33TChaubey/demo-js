// let a = "Hello This is Javascript test string";

// function count_words(str) {
//     let obj = {};
//     // Split the string into words
//     // let words = str.split(' ');

//     // Iterate over each word in the array
//     for (let i = 0; i < str.length; i++) {
//         let ok = str[i];
//         // Check if the word is already in the object
//         if (obj[ok]) {
//             obj[ok] += 1;
//         } else {
//             obj[ok] = 1;
//         }
//     }
//     return obj;
// }

// console.log(count_words(a));
// Outputs


// let a = [1,2,3,4];
// let newArr = [];
// const func = (x) => x *2;
// for(let  i = 0; i < a.length; i++){
//     newArr.push(func(a[i]));
// }

// console.log(newArr);

const matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];


console.log(transposed);

class MatrixClass {
    constructor(matrixData) {
        this.matrixData = matrixData;
    }

    getTransposed() {
        return this.matrixData.map((row, index) => this.matrixData.map(col => col[index]));
    }
}
