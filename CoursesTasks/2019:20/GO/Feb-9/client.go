package main

import (
	"flag"
	"fmt"
	"io/ioutil"
	"net"
	"os"
)

func main() {
	flag.Parse()
	if flag.NArg() < 2 {
		fmt.Printf("usage: %s <host> <port> \n", flag.Arg(0))
		os.Exit(1)
	}
	host := flag.Arg(0)
	port := flag.Arg(1)
	conn, err := net.Dial("tcp", host+":"+port)
	if err != nil {
		fmt.Printf("Failed to connect: %s", err.Error())
		os.Exit(1)
	}
	for {
		var s string
		fmt.Scanln(&s)
		fmt.Fprintln(conn, s)
		res, err := ioutil.ReadAll(conn)
		if err != nil {
			panic(err)
		}
		fmt.Println(string(res))
		res, err = ioutil.ReadAll(conn)
		if err != nil {
			panic(err)
		}
		fmt.Println(string(res))
	}
	conn.Close()
}
