`
Jamie is a programmer, and James' girlfriend. She likes diamonds, and wants a diamond string from James. Since James doesn't know how to make this happen, he needs your help.

Task
You need to return a string that looks like a diamond shape when printed on the screen, using asterisk (*) characters. Trailing spaces should be removed, and every line must be terminated with a newline character (\n).

Return null/nil/None/... if the input is an even number or negative, as it is not possible to print a diamond of even or negative size.

Examples
A size 3 diamond:

 *
***
 *
...which would appear as a string of " *\n***\n *\n"

A size 5 diamond:

  *
 ***
*****
 ***
  *
...that is:

"  *\n ***\n*****\n ***\n  *\n"
`;

function diamond(n) {
  if (n <= 0 || n % 2 === 0) return null;

  let diamondStr = "";
  const mid = Math.floor(n / 2);

  for (let i = 0; i < n; i++) {
    let stars = n - Math.abs(mid - i) * 2;
    let spaces = Math.abs(mid - i);
    diamondStr += " ".repeat(spaces) + "*".repeat(stars) + "\n";
  }

  return diamondStr;
}

console.log(diamond(1));
console.log(diamond(3));
console.log(diamond(5));
console.log(diamond(7));
console.log(diamond(2));
