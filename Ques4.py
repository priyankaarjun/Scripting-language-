function createCounter(init) {
    let current = init;

    return {
        increment: function() {
            return ++current;
        },
        decrement: function() {
            return --current;
        },
        reset: function() {
            current = init;
            return current;
        }
    };
}

// Example usage:
const counter = createCounter(5);

console.log(counter.increment()); // Output: 6
console.log(counter.decrement()); // Output: 5
console.log(counter.reset());     // Output: 5
console.log(counter.decrement()); // Output: 4
