package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
)

func fetchSite(url string) (string, error) {
	resp, err := http.Get(url)
	defer resp.Body.Close()
	data, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return "", err
	}
	return string(data), nil
}

func fetchGoogle(q string) (string, error) {
	return fetchSite("https://www.google.com/search?q=" + q)
}

func fetchYandex(q string) (string, error) {
	return fetchSite("https://yandex.ru/search/?text=" + q)
}

func main() {
	// Используя каналы и селект написать проверку поиска (кто быстрее) на одном запросе.
	// Желательно провести несколько тестов в цикле
	res, err := fetchYandex("test")
	fmt.Println(res, err)
}
