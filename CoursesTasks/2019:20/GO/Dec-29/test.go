package main

import (
	"flag"
	"fmt"
	"image"
	"os"
	"os/exec"

	"image/color"
	_ "image/jpeg"
	_ "image/png"

	"github.com/buger/goterm"
	"github.com/nfnt/resize"
)

func openImage(imgName string) (image.Image, error) {
	f, err := os.Open(imgName)
	if err != nil {
		return nil, err
	}

	img, _, err := image.Decode(f)
	if err != nil {
		return nil, err
	}

	return img, nil
}

func convertPixel(c color.Color) rune {
	gc := color.GrayModel.Convert(c)
	r, _, _, _ := gc.RGBA()

	r = r >> 8

	symbols := []rune("@80G#Lft+=;:,.  ")

	return symbols[r/16]
}

func ToAscii(img image.Image, w, h uint) [][]rune {

	img = resize.Resize(w, h, img, resize.Lanczos3)

	res := make([][]rune, img.Bounds().Dy())

	for i := range res {
		res[i] = make([]rune, img.Bounds().Dx())
	}

	for i := range res {
		for j := range res[i] {
			res[i][j] = convertPixel(img.At(j, i))
		}
	}
	return res
}

func PrintImg(ascii [][]rune) {
	for i := range ascii {
		for j := range ascii[i] {
			fmt.Printf("%c", ascii[i][j])
		}
		fmt.Println()
	}
}

func main() {
	flag.Parse()
	if flag.NArg() < 1 {
		fmt.Println("Usage: asciimg <image>")
		os.Exit(0)
	}

	imgName := flag.Arg(0)

	img, err := openImage(imgName)
	if err != nil {
		panic(err)
	}

	for {
		cmd := exec.Command("clear")
		cmd.Stdin = os.Stdin
		terminalHeight := goterm.Height()
		terminalWidth := goterm.Width()

		ascii := ToAscii(img, uint(terminalHeight), uint(terminalWidth))
		PrintImg(ascii)
	}

}
