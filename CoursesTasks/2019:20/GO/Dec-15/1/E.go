package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"
)

func _checkBasic(err error) {
	if err != nil {
		log.Fatal(err)
	}
}

func main() {

	s, err := ioutil.ReadFile("in.txt")
	_checkBasic(err)

	var index, c uint16

	for i, el := range s {
		if el == 10 {
			index = uint16(i)
			fmt.Println()
			c++
		}
	}

	f, err := os.Create("out.txt")
	_checkBasic(err)

	if c != 0 {
		fmt.Fprint(f, string(s[:index-1]))
	}

}
