package main

import "fmt"

func main() {

	var j, s string
	var c uint16

	fmt.Scan(&j, &s)

	for _, Jtype := range j {
		for _, Jmine := range s {
			if Jtype == Jmine {
				c++
			}
		}
	}

	fmt.Println(c)

}
