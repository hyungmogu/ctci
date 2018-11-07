// Sentence Reverse
// You are given an array of characters arr that consists of sequences of characters separated by space characters. Each space-delimited sequence of characters defines a word.
//
// Implement a function reverseWords that reverses the order of the words in the array in the most efficient manner.
//
// Explain your solution and analyze its time and space complexities.
//
// Example:
//
// input:  arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
//                 'm', 'a', 'k', 'e', 's', '  ',
//                 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]
//
// output: [ 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e', '  ',
//           'm', 'a', 'k', 'e', 's', '  ',
//           'p', 'e', 'r', 'f', 'e', 'c', 't' ]
// Constraints:
//
// [time limit] 5000ms
//
// [input] array.character arr
//
// 0 <= arr.length <= 100
// [output] array.character


const arr1 = ['a', 'b'];
const arr2 = ['c', 'd'];
const joinedarray = arr1.concat(arr2);

function reverseWords(arr) {

  let output = [];
  let temp = [];
  let temp_inner = [];
  arr.forEach((character, idx) => {
    if (!spaceIsHit(character)) {
      temp_inner.push(character);
      if (idx === arr.length - 1) {
        temp.push(temp_inner);
        temp_inner = [];
      }
    } else {
      temp.push(temp_inner);
      temp_inner = [];
    }
  });

  let temp_reversed = temp.reverse();

  temp_reversed.forEach((characters,idx) => {
    if (characters.length === 0) {
      output.push(' ');
      return;
    }

    output = output.concat(characters);
    if (idx !== temp_reversed.length - 1) {
      output.push(' ');
    }
  });

  return output;
}

function spaceIsHit(char) {

  if (char.trim() !== '') {
      return false;
  }

  return true;
}