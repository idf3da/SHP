package main

import (
	"fmt"
	"strconv"
	"sync"
)

func num2bi(n int) string {
	return strconv.FormatInt(int64(n), 2)
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

func GenerateCombinations(alphabet string, length int) <-chan string {
	c := make(chan string)
	go func(c chan string) {
		defer close(c)

		AddLetter(c, "", alphabet, length)
	}(c)

	return c
}
func AddLetter(c chan string, combo string, alphabet string, length int) {
	if length <= 0 {
		return
	}

	var newCombo string
	for _, ch := range alphabet {
		newCombo = combo + string(ch)
		c <- newCombo
		AddLetter(c, newCombo, alphabet, length-1)
	}
}

func brute(f <-chan string, expected int, resH int, resS string, res []string, c int) {
	for combination := range f {
		hash := hashing(combination)

		fmt.Println(combination, c)

		if hash == expected {
			resH = hash
			resS = combination
			res = append(res, combination)
		}
	}
}

func main() {

	var resH, lenght, expected int
	var resS, dict string
	var wg sync.WaitGroup
	// var memoryAccess sync.Mutex

	res := make([]string, 0)
	wg.Add(2)

	lenght = 3
	dict = "123"
	expected = 22369

	f := GenerateCombinations(dict, lenght)

	// go brute(f, expected, resH, resS, res, 1)
	// go brute(f, expected, resH, resS, res, 2)

	for i, el := range f {
		fmt.Println(i, el)
	}

	wg.Wait()

	fmt.Println("Done: ", resH, resS)
	fmt.Println(res)
}
