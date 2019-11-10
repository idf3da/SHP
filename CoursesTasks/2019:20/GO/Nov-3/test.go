package main

import (
	"fmt"
)

func main() {
	ch1 := make(chan int)

	go func(in chan int) {
		val := <-in
		fmt.Println(val)
	}(ch1)

	ch1 <- 42

	fmt.Scanln()
}
