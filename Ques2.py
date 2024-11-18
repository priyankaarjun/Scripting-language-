function createCounter(n) {
    let count = n;
    return function() {
        return count++;
    };
}

// Example usage:
const counter = createCounter(10);
console.log(counter()); // Output: 10
console.log(counter()); // Output: 11
console.log(counter()); // Output: 12
