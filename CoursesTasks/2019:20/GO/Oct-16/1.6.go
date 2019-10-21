package main

import "fmt"

func main() {
	var n uint16
	fmt.Scan(&n)
	if n%10 > n/10 {
		fmt.Println("one")
	} else {
		fmt.Println("dec")
	}
}
