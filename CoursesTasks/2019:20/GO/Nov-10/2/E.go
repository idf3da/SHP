package main

import (
	"fmt"
)

func arrPrint(arr []int64) {
	for _, el := range arr {
		fmt.Print(el, " ")
	}
}

func main() {
	var n, i, s, p uint8
	fmt.Scan(&n)
	arr := make([]int64, n, n+9)

	for i = 0; i < n; i++ {
		fmt.Scan(&arr[i])
	}

	fmt.Scan(&s, &p)

	p--

	arrPrint(arr[:p])
	arrPrint(arr[p+s:])
	arrPrint(arr[p : p+s])

}
