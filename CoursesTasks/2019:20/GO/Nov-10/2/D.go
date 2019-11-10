package main

import (
	"fmt"
)

func main() {
	var n, i, minI uint8
	var min int8
	fmt.Scan(&n)
	arr := make([]int8, n)

	for i = 0; i < n; i++ {
		fmt.Scan(&arr[i])
	}

	min = arr[0]
	minI = 0

	for i = 0; i < n; i++ {
		if arr[i] < min {
			min = arr[i]
			minI = i
		}
	}

	copy(arr[1:minI+1], arr[:minI])
	arr[0] = min

	for _, el := range arr {
		fmt.Print(el, " ")
	}

}
