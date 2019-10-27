package main

import "fmt"

func sum(k int) (uint16, uint16) {
	var n uint16
	m := 0
	if k == 0 {
		return 1, 0
	}
	for k > 0 {
		m += k % 10
		k /= 10
		n++
	}
	return (uint16)(n), (uint16)(m)
}

func main() {
	var a, b, c, d, e int

	fmt.Scan(&a, &b, &c, &d, &e)

	fmt.Println(sum(a))
	fmt.Println(sum(b))
	fmt.Println(sum(c))
	fmt.Println(sum(d))
	fmt.Println(sum(e))

}
