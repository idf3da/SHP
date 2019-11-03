package main

import (
	"fmt"
)

func main() {
	var n, i, p uint8
	var m int
	fmt.Scan(&n)

	arr := make([]int, n, n+1)
	for i = 0; i < n; i++ {
		fmt.Scan(&arr[i])
	}

	fmt.Scan(&m)
	fmt.Scan(&p)

	copy(arr[p-1:], arr[p:])

	for _, el := range arr {
		fmt.Print(el, " ")
	}
}
