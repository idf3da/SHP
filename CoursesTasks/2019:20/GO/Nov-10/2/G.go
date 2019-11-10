package main

import (
	"fmt"
)

func arrPrint(arr *[]int32) {
	for _, el := range *arr {
		fmt.Print(el, " ")
	}
	fmt.Println()
}

func main() {
	var n, i, d uint8
	fmt.Scan(&n)
	arr := make([]int32, n)

	for i = 0; i < n; i++ {
		fmt.Scan(&arr[i])
	}

	fmt.Scan(&d)

	arr = append(arr[:d], arr[d+1:]...)

	arrPrint(&arr)

}
