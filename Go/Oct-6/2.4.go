package main

import "fmt"

func main() {
	var n uint16
	fmt.Scan(&n)
	fmt.Printf("%v\n", n)
	fmt.Printf("    %v\n", n+1)
	fmt.Printf("        %v", n+2)
}
