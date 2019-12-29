package main

import (
	"crypto/sha1"
	"fmt"
	"os"
	"strconv"
	"sync"
)

func str2b(b string) []byte {

	r := make([]byte, 0)

	for _, el := range b {
		r = append(r, byte(el))
	}

	return r
}

func check(a *[]byte, b *[]byte) bool {
	for i := range *a {
		if (*a)[i] != (*b)[i] {
			return false
		}
	}

	return true
}

func brute1() {
	expected := []byte("a58dc2cfc5a93134666c607fbc5d6e961254214a")

	h := sha1.New()

	for i := 0; i < 100000000/2; i++ {
		h.Write([]byte(strconv.Itoa(i)))
		bs := h.Sum(nil)

		fmt.Println(i, bs)

		if check(&bs, &expected) {
			os.Exit(1)
		}

	}
}

func brute2() {
	expected := []byte("a58dc2cfc5a93134666c607fbc5d6e961254214a")

	h := sha1.New()

	for i := 100000000 / 2; i < 100000000; i++ {
		h.Write([]byte(strconv.Itoa(i)))
		bs := h.Sum(nil)

		fmt.Println(i, bs)

		if check(&bs, &expected) {
			os.Exit(1)
		}

	}
}

func main() {

	var wg sync.WaitGroup
	wg.Add(1)

	go brute1()
	go brute2()

	wg.Wait()
}
