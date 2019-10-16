package main

import "fmt"

func main() {
	var n int32
	fmt.Scan(&n)
	if n > 0 {
		n -= 2
	} else if n < 0 {
		n++
	} else {
		n = 10
	}
	fmt.Println(n)
	//That was hard
}
