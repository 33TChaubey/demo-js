// //2. Write a JavaScript program to find the maximum number in an array. 

// // array = [10,20,30,40,50,60]

// function find_max(array){
//     let max = 0;
//     for (let i = 0; i < array.length; i++){
//         if (array[i] > max){
//             max = array[i] 
        
        
//         }
//     }
//     return max;
// }

// console.log(find_max(array))

//3. Write a JavaScript function to check if a given string is a palindrome (reads the same forwards and backwards). 


// function rev_str(array){
//     let str = "";
//     for (let i = array.length - 1;  i>=0; i--){
//         str += array[i];
//     }
//     return str;
// }

// let array = "hui";
// console.log(rev_str(array));


//Write a JavaScript program to calculate the factorial of a given number. 

// function factorial(n){
//     let fact = 1;
//     for (let i = 1; i <= n; i++){
//         fact *= i;
//     }
//     return fact
// }

// console.log(factorial(5));

//7. Write a JavaScript function to check if a given number is prime. 

// function isPrime(n){
//     for (let i =2; i < n; i++){
//         if (n % i == 0){
//             return false
//         }
//     }
//     return true
// }

// console.log(isPrime(5))

//8. Write a JavaScript program to find the largest element in a nested array. 
// Implement a function that groups elements in an array based on a given condition. For example, grouping even and odd numbers into separate arrays. 

    // function group(array){
    //     let odd = [];
    //     let even = [];
    //     for (let i = 0; i < array.length - 1; i++){
    //         if (array[i] % 2 ==0){
    //             even.push(array[i]);
    //         }else{
    //             odd.push(array[i]);
    //         }
    //     }
    //     return [even, odd]
    // }
    // array = [1,2,3,4,5,6,7,8,9,10];
    // let result = group(array);
    // console.log(result[0], result[1]);
