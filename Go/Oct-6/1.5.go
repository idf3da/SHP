package main

import "fmt"

func main() {

	var x float32
	var s byte

	fmt.Scan(&x)

	x *= 1000

	for i := 0; i < 3; i++ {
		s += x % 10
		x /= 10
	}

	fmt.Println(s)

}
