package main

import "fmt"

func a() {
	fmt.Print("A")
	defer b()
}

func b() {
	fmt.Print("B")
	defer c()
}

func c() {
	fmt.Print("C")
	defer a()
}

func main() {
	a()
}
