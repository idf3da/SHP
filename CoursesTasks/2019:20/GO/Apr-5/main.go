package main

import (
	"bufio"
	"flag"
	"fmt"
	"os"
	"strconv"
	"strings"
	"path/filepath"
	"sync"
)


var (
	recursiveFlag = flag.Bool("r", false, "Recursive search: for directories")
	printLineNum = flag.Bool("n", false, "Print line number in output")
	wg = sync.WaitGroup{}
)

type fileScanResult struct {
	file       string
	lineNumber int
	line       string
}

type dirScanResult struct {
	scannerFiles []fileScanResult
	mu sync.Mutex
}

func main() {
	flag.Parse()

	if flag.NArg() < 2 {
		exit("usage: go-search <path> <pattern> to search")
	}

	path := flag.Arg(0)
	pattern := flag.Arg(1)

	info, err := os.Stat(path)
	if err != nil {
		panic(err)
	}

	result := dirScanResult{scannerFiles: make([]fileScanResult, 0, 0)}
	
	if info.IsDir() && !*recursiveFlag {
		exit("%s: is a directory", info.Name())
	} else if info.IsDir() && *recursiveFlag {
		processDirectory(path, pattern, &result)
	} else {
		wg.Add(1)
		scanFile(path, pattern, &result)
	}

	wg.Wait()

	if *printLineNum {
		for _, line := range result.scannerFiles {
			fmt.Println(line.file+":"+strconv.Itoa(line.lineNumber)+":"+line.line)
		}
	} else {
		for _, line := range result.scannerFiles {
			fmt.Println(line.file+":"+line.line)
		}
	}
	
}

func exit(format string, val ...interface{}) {
	if len(val) == 0 {
		fmt.Println(format)
	} else {
		fmt.Printf(format, val)
		fmt.Println()
	}
	os.Exit(1)
}

func scanFile(fpath, pattern string, resultArr *dirScanResult)  {
	f, err := os.Open(fpath)
	if err != nil {
		exit("Error opening file: %s", err)
	}
	defer f.Close()

	scanner := bufio.NewScanner(f)
	scanner.Split(bufio.ScanLines)
	result := make([]fileScanResult, 0, 1)
	
	lineNum := 1
	for scanner.Scan() {
		line := scanner.Text()
		if strings.Contains(line, pattern) {
			result = append(result, fileScanResult{
				file: fpath,
				lineNumber: lineNum,
				line: line,
			})
		}
		lineNum++
	}
	if err := scanner.Err(); err != nil {
		exit("Error while scanning: %s", err)
	}

	resultArr.mu.Lock()
	resultArr.scannerFiles = append(resultArr.scannerFiles, result...)
	resultArr.mu.Unlock()

	wg.Done()
}

func processDirectory(dir string, pattern string, result *dirScanResult) {
	err := filepath.Walk(dir,
		func(path string, info os.FileInfo, err error) error {
			if err != nil {
				return err
			}
			if dir == path {
				return nil
			}
			wg.Add(1)
			go scanFile(path, pattern, result)
			return nil
		})
	if err != nil {
		exit("Error processing directory %s: %s", dir, err)
	}
}