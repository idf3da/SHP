package main

import "fmt"

func oddCounter(x uint32) byte {
	var c byte
	for x > 0 {
		if x%10%2 != 0 {
			c++
		}
		x /= 10
	}
	return c
}

func main() {
	var a, b, c int32
	fmt.Scan(&a, &b, &c)
	switch {
	case a <= b && b <= c:
		a *= a
		b *= b
		c *= c
	case a > b && b > c:
		b, c = a, a
	default:
		a = -a
		b = -b
		c = -c
	}
	fmt.Println(a, b, c)
}
