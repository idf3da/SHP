package main

import (
	"fmt"
)

func FUN(slice []int32, x, y, z uint16) []int32 {
	slice2 := make([]int32, 0, len(slice))
	x--
	y--
	for i := x; i < y; i++ {
		if i%z == 0 {
			slice2 = append(slice2, slice[i])
		}
	}
	return slice2
}

func arrRevPrint(arr []int32) {
	for i := len(arr) - 1; i >= 0; i-- {
		fmt.Print(arr[i], " ")
	}
	fmt.Println()
}

func main() {
	var n, i, x, y, z uint16
	fmt.Scan(&n)
	arr := make([]int32, n, n+9)

	for i = 0; i < n; i++ {
		fmt.Scan(&arr[i])
	}

	fmt.Scan(&x, &y, &z)

	arrRevPrint(FUN(arr, x, y, 1))
	arrRevPrint(FUN(arr, x, y, z))
}
