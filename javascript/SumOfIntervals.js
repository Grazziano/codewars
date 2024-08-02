/**
Write a function called sumIntervals/sum_intervals that accepts an array of intervals, and returns the sum of 
all the interval lengths. Overlapping intervals should only be counted once.

Intervals
Intervals are represented by a pair of integers in the form of an array. The first value of the interval will 
always be less than the second value. Interval example: [1, 5] is an interval from 1 to 5. The length of this 
interval is 4.

Overlapping Intervals
List containing overlapping intervals:

[
   [1, 4],
   [7, 10],
   [3, 5]
]
The sum of the lengths of these intervals is 7. Since [1, 4] and [3, 5] overlap, we can treat the interval 
as [1, 5], which has a length of 4.

Examples:
sumIntervals( [
   [1, 2],
   [6, 10],
   [11, 15]
] ) => 9

sumIntervals( [
   [1, 4],
   [7, 10],
   [3, 5]
] ) => 7

sumIntervals( [
   [1, 5],
   [10, 20],
   [1, 6],
   [16, 19],
   [5, 11]
] ) => 19

sumIntervals( [
   [0, 20],
   [-100000000, 10],
   [30, 40]
] ) => 100000030
Tests with large intervals
Your algorithm should be able to handle large intervals. All tested intervals are subsets of the range 
[-1000000000, 1000000000].
 */
function sumIntervals(intervals) {
  if (intervals.length === 0) return 0;

  // Sort intervals based on the starting point
  intervals.sort((a, b) => a[0] - b[0]);

  let totalLength = 0;
  let currentInterval = intervals[0];

  for (let i = 1; i < intervals.length; i++) {
    let [currentStart, currentEnd] = currentInterval;
    let [nextStart, nextEnd] = intervals[i];

    if (nextStart <= currentEnd) {
      // If the intervals overlap, merge them by extending the current interval
      currentInterval[1] = Math.max(currentEnd, nextEnd);
    } else {
      // If they don't overlap, add the length of the current interval to the total
      totalLength += currentEnd - currentStart;
      // Move to the next interval
      currentInterval = intervals[i];
    }
  }

  // Add the length of the last interval
  totalLength += currentInterval[1] - currentInterval[0];

  return totalLength;
}

// Examples
console.log(
  sumIntervals([
    [1, 2],
    [6, 10],
    [11, 15],
  ])
); // Output: 9

console.log(
  sumIntervals([
    [1, 4],
    [7, 10],
    [3, 5],
  ])
); // Output: 7

console.log(
  sumIntervals([
    [1, 5],
    [10, 20],
    [1, 6],
    [16, 19],
    [5, 11],
  ])
); // Output: 19

console.log(
  sumIntervals([
    [0, 20],
    [-100000000, 10],
    [30, 40],
  ])
); // Output: 100000030
