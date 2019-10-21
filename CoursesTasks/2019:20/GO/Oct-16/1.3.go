package main

import (
	"fmt"
)

func main() {

	var x, z int

	fmt.Scan(&x, &z)

	for i := x; i < z+1; i++ {
		fmt.Println("I want this set with", i, "soldiers!")
	}

}
