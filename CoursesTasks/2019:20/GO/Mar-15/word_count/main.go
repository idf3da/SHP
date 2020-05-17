package main

import (
    "io/ioutil"
    "path"
    "fmt"
)

const dirName = "files"

func main() {
    files, err := ioutil.ReadDir(dirName)
    if err != nil {
        panic(err)
    }

    for _, f := range files {
        fullPath := path.Join(dirName, f.Name())
        fmt.Println(fullPath)
    }

}
