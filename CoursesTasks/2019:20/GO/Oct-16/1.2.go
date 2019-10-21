package main

import (
	"fmt"
)

func main() {

	var c, x, s, index int

	fmt.Scan(&c)

	for i := 0; i < c; i++ {
		fmt.Scan(&x)
		if x > s {
			index = i + 1
		}
		s += x

	}
	fmt.Println(index)
}
