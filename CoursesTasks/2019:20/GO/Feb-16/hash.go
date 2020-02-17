package main

import (
	"crypto/md5"
	"encoding/hex"
	"flag"
	"fmt"
	"io"
	"os"
)

func md5File(filePath string) {
	var returnMD5String string

	file, err := os.Open(filePath)
	if err != nil {
		fmt.Fprintln(os.Stdout, err)
		os.Exit(1)
	}
	defer file.Close()

	hash := md5.New()
	if _, err := io.Copy(hash, file); err != nil {
		fmt.Fprintln(os.Stdout, err)
		os.Exit(1)
	}

	hashInBytes := hash.Sum(nil)[:16]

	returnMD5String = hex.EncodeToString(hashInBytes)

	fmt.Fprintln(os.Stdout, filePath, "::", returnMD5String)
}

func main() {
	flag.Parse()
	md5File(flag.Arg(0))
}
