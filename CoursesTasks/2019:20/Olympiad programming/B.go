package main

import "fmt"

func digsSum(x uint) uint {
	var s uint
	for x > 0 {
		s += x % 10
		x /= 10
	}
	return s
}

func main() {
	var x, n uint
	fmt.Scan(&n, &x)

	for digsSum(n) != x {
		n++
	}
	fmt.Println(n)
}
