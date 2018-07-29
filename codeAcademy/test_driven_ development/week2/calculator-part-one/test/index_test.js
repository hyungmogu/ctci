const assert = require('assert');
const Calculate =  require('../index.js')


describe('Calculate', () => {
	describe('.add', () => {
		it ('returns the value of two numbers added together', () => {
			// setup
			const expected1 = 10;
			const expected2 = 5;
			const expected3 = -3;
			const expected4 = 0;

			// exercise
			const result1 = Calculate.add(7,3);
			const result2 = Calculate.add(5,0);
			const result3 = Calculate.add(-5,2);
			const result4 = Calculate.add(4,-4);

			// verify
			assert.equal(result1,expected1);
			assert.equal(result2,expected2);
			assert.equal(result3,expected3);
			assert.equal(result4,expected4);
		});
	});

	describe('.subtract', () => {
		it ('returns the difference of the first number minus the second number', () => {
			const expected1 = -15;
			const expected2 = 17;
			const expected3 = 25;
			const expected4 = 0;
			const expected5 = 0;

			const result1 = Calculate.subtract(-10,5);
			const result2 = Calculate.subtract(7,-10);
			const result3 = Calculate.subtract(-20,-45);
			const result4 = Calculate.subtract(40,40);
			const result5 = Calculate.subtract(0,0);

			assert.equal(result1, expected1);
			assert.equal(result2, expected2);
			assert.equal(result3, expected3);
			assert.equal(result4, expected4);
			assert.equal(result5, expected5);
		});
	});

	describe('.multiply', () => {
		it ('returns the product of two numbers', () => {
			const expected1 = 0;
			const expected2 = 0;
			const expected3 = 0;
			const expected4 = 440;
			const expected5 = -110;
			const expected6 = -60;
			const expected7 = 100;

			const result1 = Calculate.multiply(0,0);
			const result2 = Calculate.multiply(0,1);
			const result3 = Calculate.multiply(-10,0);
			const result4 = Calculate.multiply(-10,-44);
			const result5 = Calculate.multiply(-5,22);
			const result6 = Calculate.multiply(10,-6);
			const result7 = Calculate.multiply(10,10);

			assert.equal(result1, expected1);
			assert.equal(result2, expected2);
			assert.equal(result3, expected3);
			assert.equal(result4, expected4);
			assert.equal(result5, expected5);
			assert.equal(result6, expected6);
			assert.equal(result7, expected7);
		});
	});

	describe('.divide', () => {
		it ('returns the first number divided by the second number', () => {
			const expected = [
				0.0,
				-2.0,
				-2.0,
				50.0,
				0.3333333333333333
			];

			const results = [
				Calculate.divide(0, 10),
				Calculate.divide(-10, 5),
				Calculate.divide(10,-5),
				Calculate.divide(200,4), 
				Calculate.divide(1,3)
			]

			// this approach is cleaner and less finger breaking, but hard to know where the error occured
			results.forEach((result,index) => {
				assert.strictEqual(result, expected[index])
			})

		});

		it ('throws an error when the divisors is 0', () => {
			const expected = Error;

			const result = _ => {Calculate.divide(10,0)};
			assert.throws(result, expected, 'the quotient of a number and 0 is undefined');
		});
	});
	describe('.absoluteValue', () => {
		it ('returns the absolute value of the input number',()=>{
			// setup
			const expected1 = 0;
			const expected2 = 10;
			const expected3 = 5;

			// exercise
			const result1 = Calculate.absoluteValue(0);
			const result2 = Calculate.absoluteValue(-10);
			const result3 = Calculate.absoluteValue(5);

			// verify
			assert.equal(result1, expected1);
			assert.equal(result2, expected2);
			assert.equal(result3, expected3);
		});
	});
});