package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"strings"
)

func _checkBasic(err error) {
	if err != nil {
		log.Fatal(err)
	}
}

func main() {

	var c, c2, third uint8
	var length uint16
	s, err := ioutil.ReadFile("in.txt")
	_checkBasic(err)

	str := strings.Split(string(s), "\n")

	for i, el := range str {
		if len([]byte(el)) != 0 {
			c++
		} else {
			c2++
		}

		length += uint16(len(el))

		if c2 == 2 {
			third = uint8(i)
		}
	}

	f, err := os.Create("out.txt")
	_checkBasic(err)

	fmt.Fprintln(f, c)
	fmt.Fprintln(f, length)
	if c2 > 1 {
		fmt.Fprint(f, str[third])
	} else {
		fmt.Fprint(f, 0)
	}

}
