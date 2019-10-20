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
)

// Фукнция должна вернуть число из интервала [l,r]
//func randInterval
//	return 0
//}

func randInterval(l, r int) int {
	flag.Parse()
	if *seed == 0 {
		rand.Seed(time.Now().Unix())
	} else {
		rand.Seed(int64(*seed))
	}
	return rand.Intn(r) + l
}

func main() {
	flag.Parse()
	fmt.Println(randInterval(*start, *end))
}
