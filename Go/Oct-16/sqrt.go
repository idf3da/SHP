package main

import (
	"fmt"
	"math"
	"time"
)

func sqrt(x float64) float64 {
	var z float64 = x
	for i := 0; i < 10; i++ {
		z = z - (z*z-x)/(2*z)
	}

	return z
}

func main() {

	var vl float64 = 1337

	t1 := time.Now()
	fmt.Println(sqrt(vl))
	el1 := time.Since(t1)

	t2 := time.Now()
	fmt.Println(math.Sqrt(vl))
	el2 := time.Since(t2)

	fmt.Println()

	fmt.Println("My sqrt:", el1)
	fmt.Println("Google's sqrt:", el2)

	if el1 > el2 {
		fmt.Println("Harvard doesn't want to")
		fmt.Println("Know your location.")
	}

}
