function expect(val) {
    return {
        toBe: function(expected) {
            if (val === expected) {
                return true;
            } else {
                throw new Error("Not Equal");
            }
        },
        notToBe: function(expected) {
            if (val !== expected) {
                return true;
            } else {
                throw new Error("Equal");
            }
        }
    };
}

// Example usage:
try {
    expect(5).toBe(5); // true
    expect(5).notToBe(10); // true
    expect(5).toBe(10); // throws "Not Equal"
} catch (error) {
    console.error(error.message); // Output: "Not Equal"
}
