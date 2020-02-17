package main

import (
	"fmt"
)

type A struct {
}

func (a *A) test() int {
	return 1
}

type B struct {
}

func (b *B) test() int {
	return 2
}

type C struct {
	A
	B
}

func main() {
	c := C{}
	fmt.Println(c.test())
}
