package main

import "fmt"

func main() {

	var n, i, negI, posI uint8
	var flag1 bool
	flag1 = true
	fmt.Scan(&n)

	arr := make([]int16, n)

	for i = 0; i < n; i++ {
		fmt.Scan(&arr[i])
	}

	for i = 0; i < n; i++ {
		if flag1 {
			if arr[i] < 0 {
				negI = i
				flag1 = false
			}
		}
		if arr[i] >= 0 {
			posI = i
		}
	}
	arr[posI], arr[negI] = arr[negI], arr[posI]

	for i = 0; i < n; i++ {
		fmt.Print(&arr[i], " ")
	}

}
