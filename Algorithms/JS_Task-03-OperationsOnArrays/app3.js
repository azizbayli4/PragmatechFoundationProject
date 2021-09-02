let numbers = [23, 45, 67, 78, 21, 89, 34];
console.log(numbers);
console.log("-----------------------------------------");

//odd numbers
function OddNums(array) {
  for (let i = 0; i < array.length; i++) {
    if (numbers[i] % 2 !== 0 && numbers[i] !== 0) {
      console.log("This is an odd number: " + numbers[i] + " position:" + i);
    }
  }
}

OddNums(numbers);

console.log("-----------------------------------------");

//Even numbers
function EvenNums(array) {
  for (let i = 0; i < array.length; i++) {
    if (numbers[i] % 2 == 0 && numbers[i] !== 0) {
      console.log("This is an even number: " + numbers[i] + " position:" + i);
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
  console.log("Sum of elements: " + sum);
}

SumOfArguments(numbers);

console.log("-----------------------------------------");

//Sum of Odd Numbers
function SumOfOddNums(array) {
  let sum = 0;
  for (let i = 0; i < array.length; i++) {
    if (numbers[i] % 2 !== 0 && numbers[i] !== 0) {
      sum += numbers[i];
    }
  }
  console.log("Sum of odd elements: " + sum);
}
SumOfOddNums(numbers);

console.log("-----------------------------------------");

//Sum of Even Numbers
function SumEvenNums(array) {
  let sum = 0;
  for (let i = 0; i < array.length; i++) {
    if (numbers[i] % 2 == 0 && numbers[i] !== 0) {
      sum += numbers[i];
    }
  }
  console.log("Sum of even elements: " + sum);
}
SumEvenNums(numbers);
