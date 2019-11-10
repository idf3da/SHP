package main

import (
	"fmt"
)

func main() {
	a := []int{1, 2, 3, 4, 5}
	a = append(a, 6)
	fmt.Println(len(a) + cap(a))
}
