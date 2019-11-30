package main

import (
	"fmt"
	"strings"
)

type Date struct {
	Day   uint8
	Month uint8
	Year  uint16
}

func main() {

	var d1, d2, d3 Date
	var temp string
	var data []string

	fmt.Scanln(&temp)
	data = strings.Split(temp, ".")

	d1.Day = strings.(data[0])
	d1.Month = uint8(data[1])
	d1.Year = uint8(data[2])

	if ((d2.Year >= d3.Year) && (d3.Year >= d1.Year)) && ((d2.Month >= d3.Month) && (d3.Month >= d1.Month)) && ((d2.Day >= d3.Day) && (d3.Day >= d1.Day)) {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}
}
