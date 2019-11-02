package main

import "fmt"

func digsCount(n uint32) int {
	var i int
	for ; n > 0; i++ {
		n /= 10
	}
	return i
}

func main() {
	var n, s1, s2, temp uint32
	fmt.Scan(&n)
	if digsCount(n)%2 == 0 {
		temp = n
		for i := 0; i < digsCount(n)/2; i++ {
			s1 += temp % 10
			temp /= 10
		}
		temp = n
		for i := digsCount(n) / 2; i < digsCount(n); i++ {
			s2 += temp % 10
			temp /= 10
		}
		if s1 == s2 {
			fmt.Println("YES")
		}
	} else {
		fmt.Println("NO")
	}

}
