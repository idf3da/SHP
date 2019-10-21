package main

import "fmt"

func main() {
	var a, b int32
	fmt.Scan(&a, &b)
	if b != 0 && (a%b == 0) || a != 0 && (b%a == 0) {
		fmt.Println("YES")
	} else if a == 0 && b == 0 {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}
}
