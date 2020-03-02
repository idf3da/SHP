package main

import (
    "fmt"
    "flag"
    "io/ioutil"
    "os"
)

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
        if file.IsDir() {
            continue
        }
        name := file.Name()
        fmt.Println(name)
    }
}
