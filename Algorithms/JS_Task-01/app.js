//1) a=5; b=6; yenidən təyin etmeden ele edin ki c.log(a) yazanda 6 digerinde 5 cixsin

//my way
let a = 5;
let b = 6;
let temp;

console.log("Before the method:");
console.log(a);
console.log(b);

temp = a;
a = b;
b = temp;

console.log("After applying rechange method:");
console.log(a);
console.log(b);

console.log("-----------------");

//after research

//first way
let c = 5;
let d = 6;

console.log("Before the method:");
console.log(c);
console.log(d);

[c, d] = [d, c];

console.log("After applying rechange method:");
console.log(c);
console.log(d);

//second way
// let a = 1;
// let b = 2;

// a = a + b;
// b = a - b;
// a = a - b;

// console.log(a);
// console.log(b);

console.log("-----------------");

//2) a++ və ++a arasındakı fərq nədir?
//code example
var x = 10;
var y = 20;
console.log(x);
console.log(y);

//pre-increment operator
x = ++x;
console.log("++x = " + x);
//post-increment operator
y = y++;
console.log("y++ = " + y);

console.log("But without initializing");

var x1 = 10;
x1++;
console.log(x1);

var y1 = 20;
++y1;
console.log(y1);
