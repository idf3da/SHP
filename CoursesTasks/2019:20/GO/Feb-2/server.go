package main

import (
	"fmt"
	"net"
)

func main() {
	l, err := net.Listen("tcp", "localhost:3113")
	if err != nil {
		panic(err)
	}
	conn, err := l.Accept()
	if err != nil {
		panic(err)
	}
	
	var a, b int

	fmt.Fscan(conn, &a, &b)

	fmt.Println("Got:", a, b)

	fmt.Fprintln(conn, a, "+", b, "=", a + b)
	fmt.Fprintln(conn, a, "-", b, "=", a - b)

	conn.Close()
	l.Close()
}
