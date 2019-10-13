package main

import (
	"fmt"
)

func oddCount(a, b uint32) byte {
	var res byte
	odd1, odd2 := 0, 0
	for a > 0 {
		n := a % 10
		if n != 0 {
			if n%2 != 0 {
				odd1++
			}
			n = b % 10
			if n%2 != 0 {
				odd2++
			}
		}
		a /= 10
	}

	if odd1 > odd2 {
		res = 1
	} else if odd1 < odd2 {
		res = 2
	} else if odd1 == odd2 {
		res = 0
	}

	return res
}

func main() {

	var a, b uint32

	fmt.Scan(&a, &b)

	fmt.Print(oddCount(a, b))

}
