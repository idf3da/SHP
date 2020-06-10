package main

import (
	"crypto/md5"
	"encoding/hex"
	"flag"
	"fmt"
	"io"
	"io/ioutil"
	"os"
	"path"
	"sync"
)

var (
	wg = sync.WaitGroup{}
)

func hash_file_md5(filePath string) {
	var returnMD5String string
	file, err := os.Open(filePath)
	if err != nil {
		fmt.Println("Error opening file:", err)
	}
	defer file.Close()
	hash := md5.New()
	if _, err := io.Copy(hash, file); err != nil {
		fmt.Println("Error occured:", err)
	}
	hashInBytes := hash.Sum(nil)[:16]
	returnMD5String = hex.EncodeToString(hashInBytes)

	fmt.Println(filePath, ":", returnMD5String)
	wg.Done()
}

func main() {

	flag.Parse()
	dir := "."
	if flag.NArg() > 0 {
		dir = flag.Arg(0)
	}

	files, err := ioutil.ReadDir(dir)
	if err != nil {
		fmt.Printf("Failed to read directory: %s", err)
	}

	for _, f := range files {
		if f.IsDir() {
			continue
		}

		go hash_file_md5(path.Join(dir, f.Name()))
		wg.Add(1)

	}

	wg.Wait()
}
