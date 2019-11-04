package main

import (
	"fmt"
)

func main() {
	var n, i, k uint8
	fmt.Scan(&n)
	arr := make([]int32, n)

	for i = 0; i < n; i++ {
		fmt.Scan(&arr[i])
	}

	fmt.Scan(&k)
	r := make([]uint8, 0, n)

	for i = 0; i < n; i++ {
		if (i+1)%k == 0 {
			r = append(r, i)
		}
	}

	for i, el := range r {
		arr = append(arr[:el-(uint8)(i)], arr[el+1-(uint8)(i):n]...)
	}

	arr = arr[:len(arr)-len(r)+1]

	for _, el := range arr {
		fmt.Print(el, " ")
	}

}
