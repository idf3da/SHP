package main

import (
	"fmt"
	"log"
	"os"
	"strconv"
)

func _checkBasic(err error) {
	if err != nil {
		log.Fatal(err)
	}
}

func main() {
	f, err := os.Open("input.txt")
	defer f.Close()
	_checkBasic(err)
	var a float64
	_, err = fmt.Fscanln(f, &a)

	r := 3.14 * a * a

	str := strconv.FormatFloat(r, 'f', 6, 64)

	f, err = os.Create("output.txt")
	_checkBasic(err)

	_, err = fmt.Fprint(f, str)

}
