let numbers = [23, 45, 67, 78, 21, 89, 34];

//odd numbers
function OddNums(array) {
  for (let i = 0; i < array.length; i++) {
    if (numbers[i] % 2 !== 0 || numbers[i] !== 0) {
      console.log(numbers[i], i);
    }
  }
}

OddNums(numbers);

console.log("-----------------------------------------");

//Even numbers
function EvenNums(array) {
  for (let i = 0; i < array.length; i++) {
    if (numbers[i] % 2 == 0) {
      console.log(numbers[i], i);
    }
  }
}

EvenNums(numbers);

console.log("-----------------------------------------");

//Sum of Nums
function SumOfArguments(array) {
  let sum = 0;
  for (let i = 0; i < array.length; i++) {
    sum += array[i];
  }
  console.log(sum);
}

SumOfArguments(numbers);

console.log("-----------------------------------------");

//Sum of Odd Numbers
function SumOfOddNums(array) {
  let sum = 0;
  for (let i = 0; i < array.length; i++) {
    if (numbers[i] % 2 !== 0) {
      console.log(numbers[i]);
      sum += numbers[i];
    }
  }
  console.log("-----------------------------------------");
  console.log(sum);
}
SumOfOddNums(numbers);
