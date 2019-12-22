package main

import (
	"fmt"
	"strconv"
)

func num2bi(n int) string {
	return strconv.FormatInt(int64(n), 2)
}

func comb(n, m int, emit func([]int)) {
	s := make([]int, m)
	last := m - 1
	var rc func(int, int)
	rc = func(i, next int) {
		for j := next; j < n; j++ {
			s[i] = j
			if i == last {
				emit(s)
			} else {
				rc(i+1, j+1)
			}
		}
		return
	}
	rc(0, 0)
}

func hashing(s string) int {
	var k, sum, i, j int

	sn := make([]string, 0)

	k = 1

	for i = 0; i < len(s); i++ {
		sn = append(sn, num2bi(int(s[i])))
		sum += int(s[i])
	}

	for i = 0; i < sum%255+12; i++ {
		sn = append(sn, sn[0])
		sn = sn[1:]

		for j = 0; j < len(s); j++ {
			k = (k*int(s[j]) + int(s[len(s)-j-1])) % 100000
		}
	}

	return k
}

func main() {
	comb(5, 3, func(c []int) {
		fmt.Println(c)
	})
}
