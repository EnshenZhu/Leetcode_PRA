import { countOdds1 } from "./solution1"
import { countOdds2 } from "./solution2"

// execute countOdd1

var startTime = performance.now()

countOdds1(low=2,high=100)   // <---- measured code goes between startTime and endTime
    
var endTime = performance.now()

console.log(`Call to countOdd1 took ${endTime - startTime} milliseconds`)

// execute countOdd2

var startTime = performance.now()

countOdds2(low=2,high=100)   // <---- measured code goes between startTime and endTime
    
var endTime = performance.now()

console.log(`Call to countOdd2 took ${endTime - startTime} milliseconds`)