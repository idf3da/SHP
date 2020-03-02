package main

import (
    "fmt"
    "flag"
    "os"
    "crypto/md5"
    "io"
)

func main() {
    flag.Parse()
    if flag.NArg() < 1 {
        fmt.Println("usage: ./md5 <file>")
        os.Exit(1)
    }
    fname := flag.Arg(0)
    f, err := os.Open(fname)
    defer f.Close()
    if err != nil {
        fmt.Println("Error: ", err)
        os.Exit(1)
    }

    h := md5.New()
    _, err = io.Copy(h, f)
    if err != nil {
        fmt.Println("Failed to hash file: ", err)
        os.Exit(1)
    }
    hashBytes := h.Sum(nil)
    fmt.Printf("%x", hashBytes)
}
