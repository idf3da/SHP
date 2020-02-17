package main

import (
	"flag"
	"fmt"
	"io/ioutil"
	"os"
	"os/exec"
)

func main() {
	flag.Parse()
	dir := "."
	if flag.Arg(0) != "" {
		dir = flag.Arg(0)
	}

	files, err := ioutil.ReadDir(dir)
	if err != nil {
		fmt.Println("Failed to list directory: ", err)
		os.Exit(1)
	}
	commands := make([]*exec.Cmd, 0)

	for _, file := range files {
		if file.IsDir() {
			continue
		}
		fileName := dir + "/" + file.Name()
		cmd := exec.Command("./hash", fileName)
		if err := cmd.Start(); err != nil {
			fmt.Println(fileName, "-err-", err)
		} else {
			commands = append(commands, cmd)
		}
	}

	for _, cmd := range commands {
		if err := cmd.Wait(); err != nil {
			fmt.Println(err)
			os.Exit(1)
		}
		out, err := cmd.Output()
		if err != nil {
			fmt.Println(err)
			os.Exit(1)
		}

	}
}
