package main

import (
	"fmt"
	"math"
)

func main() {
	var n uint16
	fmt.Scan(&n)

	a := make([]float32, n)

	for i := 0; i < (int)(n); i++ {
		fmt.Scan(&a[i])
	}

	for i, el := range a {
		if el > 10 {
			a[i] = (float32)(math.Sqrt((float64)(a[i])))
		}
	}
	for _, el := range a {
		fmt.Printf("%.6f ", el)
	}
}
