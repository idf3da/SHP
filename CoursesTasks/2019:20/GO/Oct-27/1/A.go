package main

import "fmt"

func main() {
	var n, x, y int
	var s int64

	fmt.Scan(&n)

	arr := make([]int16, n)

	for i := 0; i < n; i++ {
		fmt.Scan(&arr[i])
	}

	fmt.Scan(&x, &y)

	for i := x; i < y+1; i++ {
		s += (int64)(arr[i])
	}

	fmt.Println(s)

}
