package main

import "fmt"

func main() {
	var n int
	var s int64
	var flag bool = false

	fmt.Scan(&n)

	arr := make([]int16, n)

	for i := 0; i < n; i++ {
		fmt.Scan(&arr[i])
	}

	for i := 0; i < n; i++ {
		if arr[i]%2 != 0 {
			flag = true
			s += (int64)(arr[i])
		}
	}

	if flag {
		fmt.Println(s)
	} else {
		fmt.Println("No solution")
	}
}
