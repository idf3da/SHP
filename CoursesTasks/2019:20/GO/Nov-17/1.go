package main

import (
	"fmt"
)

func main() {

	s := [5]string{"asd", "asd", "fgh", "fgh", "123"}

	var words = make(map[string]int)

	for _, v := range s {
		if _, ok := words[v]; ok {
			words[v]++
		} else {
			words[v] = 1
		}
	}

	fmt.Println(words)

}
