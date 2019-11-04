package main

import "fmt"

func max(a, b int16) int16 {
	if a > b {
		return a
	}
	return b
}

func main() {
	var n, i, sb, sa int16
	fmt.Scan(&n)

	amount := make([]int16, n)
	limit := make([]int16, n)

	for i = 0; i < n; i++ {
		fmt.Scan(&amount[i])
	}
	for i = 0; i < n; i++ {
		fmt.Scan(&limit[i])
	}

	for i = 0; i < n; i++ {
		sb += max(amount[i]-limit[i], 0)
	}
	sa = sb
	for i = 0; i < n; i++ {
		if amount[i] == 0 {
			sa -= limit[i]
		} else if max(limit[i]-amount[i], 0) > 0 {
			sa--
		}
	}
	if sa < 0 {
		sa = 0
	}
	fmt.Println(sb, " ", sa)

}
