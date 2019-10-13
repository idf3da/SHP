package main

import (
	"fmt"
)

func main() {

	var x int
	var flag bool = true

	for i := 0; i < 12; i++ {
		fmt.Scan(&x)
		if x == 3 {
			flag = false
		}
	}

	if flag {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}

}
