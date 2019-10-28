package main

import "fmt"

func pow(x, y int) int {
	s := x
	for i := 0; i < y-1; i++ {
		s *= x
	}
	return s
}

func main() {

	var x, y, z int

	fmt.Scan(&x, &y, &z)

	fmt.Println(pow(x, 5) + pow(y, 4) + pow(z, 8))
}
