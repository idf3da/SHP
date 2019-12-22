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
	f, err := os.Open("in.txt")
	defer f.Close()
	_checkBasic(err)
	var a, b int32
	_, err = fmt.Fscanln(f, &a, &b)

	r1 := a + b
	r2 := a - b
	r3 := a * b

	f, err = os.Create("out.txt")
	_checkBasic(err)

	_, err = fmt.Fprintln(f, r1)
	_, err = fmt.Fprintln(f, r2)
	_, err = fmt.Fprint(f, r3)

}
