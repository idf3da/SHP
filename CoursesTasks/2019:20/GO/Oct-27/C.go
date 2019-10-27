package main

import "fmt"

func main() {
	var n int
	var s int64

	fmt.Scan(&n)

	arr := make([]int16, n)

	for i := 0; i < n; i++ {
		fmt.Scan(&arr[i])
	}

	for i := 0; i < 5; i++ {
		s += (int64)(arr[i])
	}

	fmt.Println(s)

}
