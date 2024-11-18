function mapArray(arr, fn) {
    let result = []; // Initialize an empty array to hold the results
    for (let i = 0; i < arr.length; i++) {
        result.push(fn(arr[i], i)); // Apply the mapping function to each element and index
    }
    return result; // Return the transformed array
}

// Example usage:
const arr = [1, 2, 3];
const fn = (x, index) => x * 2 + index; // A sample transformation function

console.log(mapArray(arr, fn)); // Output: [2, 5, 8]
