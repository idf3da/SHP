package main

import (
	"fmt"
)

func main() {
	var n, i uint8
	var m int32
	fmt.Scan(&n)

	arr := make([]int32, n)
	for i = 0; i < n; i++ {
		fmt.Scan(&arr[i])
	}

	fmt.Scan(&m)
	arr = append(arr, m)

	for _, el := range arr {
		fmt.Print(el, " ")
	}
}
