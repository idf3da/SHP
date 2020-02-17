package main

import (
	"fmt"
	"net"
)

func Reverse(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

func handler(conn net.Conn) {
	var s string
	for {
		fmt.Fscan(conn, &s)
		fmt.Println("Got:", s)
		fmt.Fprintln(conn, Reverse(s))
		fmt.Println("Sent:", Reverse(s))
	}
	conn.Close()
}

func main() {
	l, err := net.Listen("tcp", "localhost:3113")
	if err != nil {
		panic(err)
	}

	for {
		conn, err := l.Accept()
		if err != nil {
			panic(err)
		}
		handler(conn)

	}

	l.Close()
}
