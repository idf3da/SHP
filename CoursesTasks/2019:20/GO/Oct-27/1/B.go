package main

import "fmt"

func main() {
	var n, max int
	var s int64

	fmt.Scan(&n)

	arr := make([]int, n)

	for i := 0; i < n; i++ {
		fmt.Scan(&arr[i])
	}
	max = arr[0]

	for i := 1; i < n; i++ {
		if arr[i] > max {
			max = arr[i]
		}
	}
	for i := 0; i < n; i++ {
		if arr[i] != max {
			s += (int64)(arr[i])
		}
	}
	fmt.Println(s)
}
