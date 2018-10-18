// Fibonacci Brain Teaser
// Rpint out all fib numbers up to a certain index

import UIKit

func fibonacci(until n: Int) {
    var last_num: Int = 0
    var last_plus: Int = 1
    for _ in 1...n {
        let this_num = last_plus + last_num
        print(this_num)
        last_plus = last_num
        last_num = this_num
        
    }
}

fibonacci(until: 5)
