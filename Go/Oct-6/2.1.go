package main

import "fmt"

func main() {
	var x uint16
	fmt.Scan(&x)
	if x <= 13 {
		fmt.Println("childhood")
	} else if x >= 14 && x <= 24 {
		fmt.Println("youth")
	} else if x >= 25 && x <= 59 {
		fmt.Println("adulthood")
	} else if x >= 60 {
		fmt.Println("old ages")
	}
}
