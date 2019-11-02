package main

import (
	"fmt"
	"math"
)

func main() {
	var x1, y1, x2, y2, r1, r2 int64
	fmt.Scan(&x1, &y1, &r1)
	fmt.Scan(&x2, &y2, &r2)

	dist := math.Sqrt(math.Pow((float64)(x2-x1), 2) + math.Pow((float64)(y2-y1), 2))

	if (dist >= (float64)(r1+r2)) || (dist < (float64)(math.Abs((float64)(r1-r2)))) {
		fmt.Println("NO")
	} else {
		fmt.Println("YES")
	}
}
