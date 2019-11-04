package main

import (
	"fmt"
)

func main() {
	var n, i, maxI uint8
	var max int8
	fmt.Scan(&n)
	arr := make([]int8, n)

	for i = 0; i < n; i++ {
		fmt.Scan(&arr[i])
	}

	max = arr[0]
	maxI = 0

	for i = 0; i < n; i++ {
		if arr[i] > max {
			max = arr[i]
			maxI = i
		}
	}

	copy(arr[maxI:], arr[maxI+1:])
	arr[len(arr)-1] = max

	for _, el := range arr {
		fmt.Print(el, " ")
	}

}
