package main

import (
	"flag"
	"fmt"
	"io/ioutil"
	"os"
	"strconv"
)

var (
	d      = flag.String("d", ".", "Directory to process")
	a      = flag.Bool("a", false, "Print all info")
	h      = flag.Bool("h", false, "Toggle human-readable file size")
	sorted = flag.String("sort", "name", "Sort by: name, date, size")
)

func sortFilesBy(files *[]os.FileInfo) {
	flag.Parse()

	if *sorted == "date" {
		var (
			n      = len(*files)
			sorted = false
		)
		for !sorted {
			swapped := false
			for i := 0; i < n-1; i++ {
				if (*files)[i].ModTime().After((*files)[i+1].ModTime()) {
					(*files)[i+1], (*files)[i] = (*files)[i], (*files)[i+1]
					swapped = true
				}
			}
			if !swapped {
				sorted = true
			}
			n = n - 1
		}
	} else if *sorted == "size" {
		var (
			n      = len(*files)
			sorted = false
		)
		for !sorted {
			swapped := false
			for i := 0; i < n-1; i++ {
				if (*files)[i].Size() > (*files)[i+1].Size() {
					(*files)[i+1], (*files)[i] = (*files)[i], (*files)[i+1]
					swapped = true
				}
			}
			if !swapped {
				sorted = true
			}
			n = n - 1
		}
	}

}

func hrSize(fsize int64) string {
	flag.Parse()

	if *h {
		if fsize < 1024 {
			return strconv.FormatInt(fsize, 10) + "B"
		} else {
			newFSize := float64(fsize) / 1024.0

			if newFSize < 1024.0 {
				return strconv.FormatFloat(newFSize, 'f', 1, 64) + "KB"

			} else {
				newFSize /= 1024.0

				if newFSize < 1024.0 {
					return strconv.FormatFloat(newFSize, 'f', 1, 64) + "MB"

				} else {
					newFSize /= 1024.0

					if newFSize < 1024 {
						return strconv.FormatFloat(newFSize, 'f', 1, 64) + "GB"
					} else {
						return strconv.FormatFloat(newFSize/1024.0, 'f', 1, 64) + "TB"
					}
				}
			}
		}
	}

	return strconv.FormatInt(fsize, 10)

}

func printAll(file os.FileInfo) {
	time := file.ModTime().Format("Jan 06 15:4")
	fSize := hrSize(int64(file.Size()))
	fmt.Printf("%v %s %s \n", fSize, time, file.Name())
}

func main() {
	flag.Parse()
	files, _ := ioutil.ReadDir(*d)

	if *sorted != "name" {
		sortFilesBy(&files)
	}

	for _, file := range files {
		if *a {
			printAll(file)
		} else {
			fmt.Println(file.Name())
		}
	}
}
