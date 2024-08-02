/**
We need to sum big numbers and we require your help.

Write a function that returns the sum of two numbers. The input numbers are strings and the function must return a string.

Example
add("123", "321"); -> "444"
add("11", "99");   -> "110"
Notes
The input numbers are big.
The input is a string of only digits
The numbers are positives
 */
function add(a, b) {
  let carry = 0;
  let result = [];

  // Pad the shorter string with leading zeros
  while (a.length < b.length) a = '0' + a;
  while (b.length < a.length) b = '0' + b;

  // Iterate from the end to the beginning
  for (let i = a.length - 1; i >= 0; i--) {
    let sum = parseInt(a[i]) + parseInt(b[i]) + carry;
    carry = Math.floor(sum / 10);
    result.unshift(sum % 10);
  }

  // If there's a remaining carry, add it to the front
  if (carry > 0) {
    result.unshift(carry);
  }

  return result.join('');
}

// Examples
console.log(add('123', '321'));
console.log(add('11', '99'));
console.log(add('63829983432984289347293874', '90938498237058927340892374089'));
