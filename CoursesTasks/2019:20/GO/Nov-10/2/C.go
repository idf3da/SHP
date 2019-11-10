package main

import "fmt"

func main() {

	var n, i uint8
	var min int32
	fmt.Scan(&n)

	arr := make([]int32, n)

	for i = 0; i < n; i++ {
		fmt.Scan(&arr[i])
	}

	min = arr[0]

	for _, el := range arr {
		if el < min {
			min = el
		}
	}

	fmt.Println(min)

}
