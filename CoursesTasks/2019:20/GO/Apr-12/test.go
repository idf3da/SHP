package main

func kek(ch chan int) {
	ch <- 20
}
func main() {
	ch := make(chan int)
	go kek(ch)
	print(<-ch)
}
