package main

import "fmt"

type Personal_data struct {
	Name  string
	Age   uint8
	Phone string
}

func main() {

	var n, i uint8
	var name, surname string

	fmt.Scan(&n)

	arr := make([]Personal_data, n)

	for ; i < n; i++ {
		fmt.Scan(&name, &surname)
		arr[i].Name = name + " " + surname
		fmt.Scan(&arr[i].Age)
		fmt.Scan(&arr[i].Phone)
	}

	for i = 0; i < n; i++ {
		fmt.Print(arr[i].Name, ", ", arr[i].Age, " let, tel.: ", arr[i].Phone)
		fmt.Println()
	}

}
