package main

import "fmt"

func myJoin(sep string, str ...string) string {
	res := ""

	for i, el := range str {
		res += el
		if i != len(str)-1 {
			res += sep
		}
	}

	return res
}

func main() {

	fmt.Println(myJoin("-", "8", "800", "555", "3535"))

}
