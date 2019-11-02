package main

import "fmt"

func changeAngle(angle *byte, left bool, right bool) {
	if left {
		if *angle < 3 && *angle >= 0 {
			*angle++
		} else {
			*angle = 0
		}
	}
	if right {
		if *angle > 0 {
			*angle--
		} else {
			*angle = 3
		}
	}
}

func main() {
	var a, b, n, x, y, i int
	var angle byte
	angle = 0
	fmt.Scan(&a, &b, &n)

	x, y = 0, 0

	for i = 0; i < n; i++ {
		changeAngle(&angle, i%a == 0, i%b == 0)
		switch angle {
		case 0:
			x++
		case 1:
			y++
		case 2:
			x--
		case 3:
			y--
		}
	}
	fmt.Println(x, y)
}
