package main

import (
	"fmt"
)

func sum(k uint32) uint16 {
	var n uint16
	var m uint32
	if k == 0 {
		return 0
	}
	for k > 0 {
		m += k % 10
		k /= 10
		n++
	}
	return (uint16)(m)
}

func main() {
	var arr [5]uint32
	var s uint16

	for i := 0; i < 5; i++ {
		fmt.Scan(&arr[i])
	}

	for i := 0; i < 5; i++ {
		s += (sum(arr[i]))
	}

	fmt.Println(s)
}
