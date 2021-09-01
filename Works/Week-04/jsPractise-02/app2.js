function Foo(...array) {
  let sum = 0;
  for (let i = 0; i < array.length; i++) {
    sum += array[i];
  }
  //return sum;
  console.log(sum);
}
Foo(3, 4, 12, 45, 67, 78);
//console.log(Foo(3, 4, 12, 45, 67, 78))
