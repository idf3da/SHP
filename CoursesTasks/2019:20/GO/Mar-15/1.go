package main

import (
	"bufio"
	"flag"
	"fmt"
	"io"
	"log"
	"os"
	"path/filepath"
	"sort"
	"strings"
	"sync"
)

var wg sync.WaitGroup
var c uint64
var words = make(map[string]int)
var mm = sync.RWMutex{}

func countWord(filePath string) {
	defer wg.Done()

	var rdr io.Reader
	var err error

	rdr, err = os.Open(filePath)
	if err != nil {
		panic(err)
	}

	scanner := bufio.NewScanner(rdr)
	scanner.Split(bufio.ScanWords)
	for scanner.Scan() {
		word := scanner.Text()
		word = strings.ToLower(word)

		mm.Lock()
		if _, ok := words[word]; !ok {
			words[word] = 1
		} else {
			words[word]++
		}
		mm.Unlock()
	}
}

func main() {
	flag.Parse()
	dir := "."
	if flag.Arg(0) != "" {
		dir = flag.Arg(0)
	}

	files := make([]string, 0)

	err := filepath.Walk(dir,
		func(path string, info os.FileInfo, err error) error {
			if err != nil {
				return err
			}
			files = append(files, path)
			return nil
		})
	if err != nil {
		log.Println(err)
	}

	wg.Add(len(files))
	for _, file := range files {
		go countWord(file)
	}

	wg.Wait()

	n := map[int][]string{}
	var a []int
	for k, v := range words {
		n[v] = append(n[v], k)
	}
	for k := range n {
		a = append(a, k)
	}
	sort.Sort(sort.IntSlice(a))
	for _, k := range a {
		if k > 1 {
			for _, s := range n[k] {
				fmt.Printf("%s, %d\n", s, k)
			}
		}
	}

}
