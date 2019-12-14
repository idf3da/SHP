package main

import (
	"flag"
	"fmt"
	"io"
	"io/ioutil"
	"os"
)

var (
	decrypt = flag.Bool("decrypt", false, "--decrypt to decrypt")
	encrypt = flag.Bool("encrypt", false, "--encrypt to encrypt")
	key     = flag.String("key", "", "key to encrypt/decrypt (1 byte)")
	input   = flag.String("inp", "", "file to read")
	output  = flag.String("out", "", "file to write")
)

func xor(b *[]byte, key byte) {
	for i := range *b {
		(*b)[i] = (*b)[i] ^ key
	}
}

type xorReader struct {
	key byte
	r   io.Reader
}

func (x *xorReader) Read(b []byte) (int, error) {
	n, e := x.r.Read(b)

	xor(&b, x.key)

	return n, e
}

type xorWriter struct {
	key byte
	w   io.Writer
}

func (x *xorWriter) Write(b []byte) (int, error) {
	// TODO(encrypt) b
	xor(&b, x.key)

	return x.w.Write(append([]byte(">> "), b...))
}

func checkError(e error) {
	if e != nil {
		fmt.Println(e)
		os.Exit(1)
	}
}

func main() {
	flag.Parse()

	if *key == "" {
		fmt.Println("Please provide key to encrypt/decrypt")
		os.Exit(1)
	}

	var i io.Reader
	var o io.Writer

	i = os.Stdin
	o = os.Stdout

	keyByte := (*key)[0]

	if *encrypt {
		w := xorWriter{keyByte, o}

		b, err := ioutil.ReadAll(i)
		checkError(err)

		_, err = w.Write(b)
		checkError(err)
	}

	if *decrypt {
		r := xorReader{keyByte, i}

		b, err := ioutil.ReadAll(&r)
		checkError(err)

		_, err = o.Write(b)
		checkError(err)
	}
}
