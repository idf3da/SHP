package main

import "fmt"

const (
	n = 30
)

func main() {
	jobs := make(chan int, n)
	results := make(chan int, n)

	for i := 0; i < n; i++ {
		go worker(jobs, results)
	}

	for i := 0; i < n; i++ {
		jobs <- i
	}

	for j := 0; j < n; j++ {
		fmt.Println(<-results)
	}
}

func worker(jobs <-chan int, results chan<- int) {
	for n := range jobs {
		results <- fib(n)
	}
}

func fib(n int) int {
	if n <= 1 {
		return n
	}
	return fib(n-1) + fib(n-2)
}

//The new beginning 17/10/2019 19:43
