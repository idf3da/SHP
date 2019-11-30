package main

import "fmt"

type Student struct {
	Name    string
	Surname string
	Math    uint8
	Phys    uint8
	Inf     uint8
}

func main() {

	var n, i, avgMath, avgPhys, avgInf uint8
	var nf float32

	fmt.Scan(&n)
	nf = float32(n)

	arr := make([]Student, n)

	for ; i < n; i++ {
		fmt.Scanln(&arr[i].Name, &arr[i].Surname, &arr[i].Math, &arr[i].Phys, &arr[i].Inf)
	}

	for i = 0; i < n; i++ {
		avgInf += arr[i].Inf
		avgMath += arr[i].Math
		avgPhys += arr[i].Phys
	}

	fmt.Printf("%.6f ", float32(avgMath)/nf)
	fmt.Printf("%.6f ", float32(avgPhys)/nf)
	fmt.Printf("%.6f ", float32(avgInf)/nf)
}
