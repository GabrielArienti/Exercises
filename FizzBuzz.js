console.log('This application was developed in a JavaScript course.')
console.log('Insert a number and if is divisible by 3, it returns Fizz, if is divisible by 5 returns Buzz, and if is divisible by both numbers, return FizzBuzz.')



const output = fizzBuzz(15)
console.log('Result: ' + output)

function fizzBuzz(input) {
    if (typeof input !== 'number')
        return 'Please, insert a valid value';

    else if (input % 3 === 0 && input % 5 === 0)
        return 'FizzBuzz';

    else if (input % 3 === 0)
        return 'Fizz'

    else if (input % 5 === 0)
        return 'Buzz'

    else
        return (input)
}
