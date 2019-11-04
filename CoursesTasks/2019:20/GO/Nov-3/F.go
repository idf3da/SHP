package main

import (
	"fmt"
)

func main() {
	var n, i uint16
	fmt.Scan(&n)
	arr := make([]int32, n)

	for i = 0; i < n; i++ {
		fmt.Scan(&arr[i])
	}

	r := make([]uint16, 0, n)

	for i = 0; i < n; i++ {
		if arr[i]%2 == 0 {
			r = append(r, i)
		}
	}

	for i, el := range r {
		arr = append(arr[:el-(uint16)(i)], arr[el+1-(uint16)(i):n]...)
	}

	arr = arr[:len(arr)-len(r)+1]

	if len(arr) == 0 {
		fmt.Println("There are no elements")
	} else {
		for _, el := range arr {
			fmt.Print(el, " ")
		}
	}

}
