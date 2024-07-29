/*
Given the string representations of two integers, return the string representation of the sum of those integers.

For example:

sumStrings('1','2') // => '3'
A string representation of an integer will contain no characters besides the ten numerals "0" to "9".

I have removed the use of BigInteger and BigDecimal in java

Python: your solution need to work with huge numbers (about a milion digits), converting to int will not work.
*/
function sumStrings(a, b) {
  a = a.replace(/^0+/, "");
  b = b.replace(/^0+/, "");

  if (!a) return b;
  if (!b) return a;

  if (a.length < b.length) {
    [a, b] = [b, a];
  }

  b = b.padStart(a.length, "0");

  let carry = 0;
  let result = [];

  for (let i = a.length - 1; i >= 0; i--) {
    let digitSum = parseInt(a[i]) + parseInt(b[i]) + carry;
    carry = Math.floor(digitSum / 10);
    result.push(digitSum % 10);
  }

  if (carry) {
    result.push(carry);
  }

  result.reverse();

  return result.join("");
}

console.log(sumStrings("1", "2"));
