package main

import (
	"fmt"
	"log"
	"os"
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

	fmt.Println("float:", a)

	r := 3.14 * a * a

	f, err = os.Create("output.txt")
	_checkBasic(err)

	_, err = fmt.Fprintln(f, r)

}
