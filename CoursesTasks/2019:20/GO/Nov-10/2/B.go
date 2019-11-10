package main

import "fmt"

func main() {

	var n, i uint32
	var max, min int32
	fmt.Scan(&n)

	arr := make([]int32, n)

	for i = 0; i < n; i++ {
		fmt.Scan(&arr[i])
	}

	min, max = arr[0], arr[0]

	for _, el := range arr {
		if el > max {
			max = el
		} else if el < min {
			min = el
		}
	}

	fmt.Println((float32)(min+max) / 2.0)

}
