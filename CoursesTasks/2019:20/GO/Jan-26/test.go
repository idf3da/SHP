package main

import (
	"encoding/csv"
	"io"
	"os"
)

type QuestionReader interface {
	ParseQuestions(r io.Reader) ([]Question, error)
}

type CsvFile struct {
	r io.Reader
}

type Question struct {
	question string
	answer   string
}

func readCsv(filename string) []Question {
	var questions []Question

	csvfile, err := os.Open(filename)
	if err != nil {
		panic(err)
	}
	defer csvfile.Close()

	r := csv.NewReader(csvfile)
	records, err := r.ReadAll()
	if err != nil {
		panic(err)
	}

	for _, record := range records {
		questions = append(questions, Question{record[0], record[1]})
	}

	// Допишите код здесь
	return questions
}

func main() {
	var total uint16
	var temp string

	// 1
	// questions := []Question{{"1 + 1", "2"}, {"2 + 2", "4"}}
	// for _, question := range questions {
	// 	fmt.Println(question.question, "?")
	// 	fmt.Scanln(&temp)
	// 	if question.answer == temp {
	// 		total++
	// 	}
	// }
	// fmt.Println("You got", total, "/", len(questions))

	// 2
	// questions := readCsv("file.csv")
	// for _, question := range questions {
	// 	fmt.Println(question.question, "?")
	// 	fmt.Scanln(&temp)
	// 	if question.answer == temp {
	// 		total++
	// 	}
	// }
	// fmt.Println("You got", total, "/", len(questions))

	// To be continued....
}
