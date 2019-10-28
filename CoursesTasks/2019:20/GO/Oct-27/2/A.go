package main

import "fmt"

func main() {
	var n, maxI uint16
	var max int16
	fmt.Scan(&n)

	a := make([]int16, n)

	for i := 0; i < (int)(n); i++ {
		fmt.Scan(&a[i])
	}

	max = a[0]
	maxI = 0

	for i, el := range a {
		if el > max {
			max = el
			maxI = (uint16)(i)
		}
	}

	a[2], a[maxI] = a[maxI], a[2]

	for _, el := range a {
		fmt.Print(el, " ")
	}

}
