package main

import (
	"flag"
	"fmt"
	"math/rand"
	"time"
)

var (
	seed  = flag.Int("seed", 0, "seed for random generator. unix(now) be default")
	start = flag.Int("start", 1, "Starting number of sides on dice")
	end   = flag.Int("end", 6, "Ending number of sides on dice")
	n     = flag.Int("n", 1, "Number of times to throw a dice.")
	rflag = flag.Bool("norepeat", false, "Check if numbers should not repeat")
)

// Фукнция должна вернуть число из интервала [l,r]
//func randInterval
//	return 0
//}

func numInArray(a int, arr []int) bool {
	for _, i := range arr {
		if i == a {
			return true
		}
	}
	return false
}

func randInterval(l, r int) int {
	flag.Parse()
	if *seed == 0 {
		rand.Seed(time.Now().UTC().UnixNano())
	} else {
		rand.Seed(int64(*seed))
	}
	if l == 0 {
		return rand.Intn(r + 1) //Невключая?
	} else { //Это вообще почему так?
		return rand.Intn(r) + l
	}
}

func main() {
	flag.Parse()
	if *start > *end {
		fmt.Println("ERROR: left boundary can't be greater than right one.")
	} else {
		if !*rflag {
			for i := 0; i < *n; i++ {
				fmt.Println(randInterval(*start, *end))
			}
		} else if *start+*end >= *n {
			if *seed == 0 {
				var c int
				arr := make([]int, *n)
				for c < *n {
					randVar := randInterval(*start, *end)
					if !numInArray(randVar, arr) {
						fmt.Print(randVar, " ")
						arr[c] = randVar
						c++
					}
				}
			} else {
				fmt.Println("If you specify the seed you won't get variative numbers.")
			}
		} else {
			fmt.Println("Your range of numbers is less than num. of throws.")
		}
	}

}
