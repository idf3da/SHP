package main

import (
	"flag"
	"fmt"
	"io/ioutil"
	"os"
)

func readFirstNBytes(filePath string, n uint64) {
	file, err := os.Open(filePath)
	defer file.Close()
	if err != nil {
		panic("Couldn't open: " + filePath)
	}

	buff := make([]byte, n)
	file.Read(buff)

	fmt.Println(filePath, string(buff))
}

func main() {
	flag.Parse()
	dir := "."
	if flag.Arg(0) != "" {
		dir = flag.Arg(0)
	}

	files, err := ioutil.ReadDir(dir)
	if err != nil {
		fmt.Println("Failed to list directory: ", err)
		os.Exit(1)
	}

	for _, file := range files {
		readFirstNBytes(dir+"/"+file.Name(), 32)
	}

}
