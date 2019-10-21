package main

import "fmt"

func main() {
	var a, b, c int32
	fmt.Scan(&a, &b, &c)
	if a > b {
		if a < c {
			fmt.Println(a)
		} else if b > c {
			fmt.Println(b)
		} else {
			fmt.Println(c)
		}
	} else {
		if a > c {
			fmt.Println(a)
		} else if b < c {
			fmt.Println(b)
		} else {
			fmt.Println(c)
		}
	}
}
