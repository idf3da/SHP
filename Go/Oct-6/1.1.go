package main

import "fmt"

func main() {

	for i := 1; i < 15; i++ {
		for j := 1; j < 16; j++ {
			fmt.Printf("%02x ", i*j)
		}
		fmt.Println()
	}

}
