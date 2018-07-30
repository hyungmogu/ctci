const Calculate = {
  sum(inputArray) {
    if(inputArray.length === 0){
      return 0
    }    
    return inputArray.reduce((sum, value) => {
      return sum + value;
    })
  },

  factorial(inputNumber) {
    if (inputNumber === 0) {
      return 1;
    }
    for (let iteration = inputNumber - 1; iteration >= 1; iteration--) {
      inputNumber = inputNumber * iteration; 
    }

    return inputNumber;
  },

  add(inputOne, inputTwo) {
    return inputOne + inputTwo;
  },

  subtract(inputOne, inputTwo) {
    return inputOne - inputTwo;
  },

  multiply(inputOne, inputTwo) {
    return inputOne * inputTwo;
  },

  divide(dividend, divisor) {
    if(divisor === 0) {
      throw new Error('the quotient of a number and 0 is undefined');
    } else {
      return dividend / divisor;
    }
  },

  absoluteValue(input) {
    if(input < 0) {
      return -input;
    } else {
      return input;
    }
  },

  exponential(base, exponent) {
    output = 1;

    if (exponent === 0) {
      return output;
    }

    for (let i = 0; i < exponent; i++) {
      output *= base;
    }

    return output;
  },

  max(arr) {
    output = Number.MIN_VALUE;

    if (arr.length === 0) {
      throw new Error('Array is empty.');
    } 

    arr.forEach(element => {
      output = element > output ? element : output;
    }) 

    return output;
  },

  min(arr) {
    output = Number.MAX_VALUE;

    if (arr.length === 0) {
      throw new Error('Array is empty.');
    }

    arr.forEach(element => {
      output = element < output ? element : output;
    });

    return output;
  },

  average(arr) {
    let arr_end = arr.length - 1;
    let arr_start = 0;

    if (arr.length === 0) {
      throw new Error('Array is empty.');
    }  

    let middle_idx = parseInt(Math.floor((arr_end + arr_start)/2));

    return arr[middle_idx];
  }
}





module.exports = Calculate;