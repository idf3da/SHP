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
	var num1, num2 uint32
	fmt.Scan(&num1, &num2)
	o1, o2 := oddCounter(num1), oddCounter(num2)
	switch {
	case o1 > o2:
		fmt.Println(1)
	case o2 > o1:
		fmt.Println(2)
	case o1 == o2:
		fmt.Println(0)
	default:
		fmt.Println("???")
	}
}
