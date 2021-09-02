//2. a=5; b=6 yenidən təyin etmeden ele edin ki c.log(a) yazanda 6 digersinde 5 cixsin

// //my way
let a = 5;
let b = 6;
let c;

c = a;
a = b;
b = c;

console.log(a);
console.log(b);

//after research

//first way
// let a;
// let b;

// [a, b] = [b,a];

// console.log(a);
// console.log(b);

//second way
// let a = 1;
// let b = 2;

// a = a + b;
// b = a - b;
// a = a - b;

// console.log(a);
// console.log(b);

//a++ və ++a arasındakı fərq
//code example
var x = 10;
var y = 20;
//pre-increment operator
x = ++x;
document.write("++x = " + x);
//post-increment operator
y = y++;
document.write("<br> y++ = " + y);

var x1 = 10;
x1++;
document.write("<br>" + x1);

var y1 = 20;
++y1;
document.write("<br>" + y1);
