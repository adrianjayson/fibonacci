/*
  Fibonacci Sequence implemented in Javascript
  @Author AJ Catambay
*/

function fibonacci ( sequenceLength ) {
  var current = 0;
  var next = 1;
  var store = 0;
  var fibo = [];
  
  for(var i = 0; i < sequenceLength; i++) { // loops until reached the specified length of sequence
  
    if (i === 0) { // push 0 as the first and current number in the squence
      fibo.push(current);
    } else {
      store = current; // Holds to value of current to get the next value, later.
      current = next; // moves the next number as the current number for the next iteration.
      next = store + current;
      fibo.push(current);
    }
    
  }
  
  return fibo.join(',');
}

//console.log(fibonacci(30));