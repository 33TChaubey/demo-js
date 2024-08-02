import {linear, binary} from './index.js';
let array = [1,2,3,4,5,6,7,8,9];
let x1 = 8;

let x = linear(array, x1);
let x2 = binary(array, x1);

console.log(x);