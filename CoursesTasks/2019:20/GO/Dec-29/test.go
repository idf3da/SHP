package main

import (
	"bytes"
	"flag"
	"fmt"
	"image"
	"io"
	"io/ioutil"
	"os"

	"image/color"
	_ "image/jpeg"
	_ "image/png"

	"github.com/buger/goterm"
	color2 "github.com/fatih/color"
	"github.com/nfnt/resize"
)

var (
	output    = flag.String("o", "", "-o to output in file")
	fromASCII = flag.String("ascii", "", "-ascii to convert from ascii to img")
	noscale   = flag.Bool("noscale", false, "-noscale to set scale to 50x200")
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

// stackoverflow
func lineCounter(r io.Reader) (int, int, error) {
	buf := make([]byte, 32*1024)
	var lines, rows int
	lineSep := []byte{'\n'}

	fmt.Println()

	for {
		c, err := r.Read(buf)
		lines += bytes.Count(buf[:c], lineSep)

		switch {
		case err == io.EOF:
			return lines, rows, nil

		case err != nil:
			return lines, rows, err
		}
	}
}

func FromAscii(file string) {

	inpF, err := os.Open(file)
	b, err := ioutil.ReadAll(inpF)
	if err != nil {
		fmt.Println("Error while reading ascii file: ", err)
	}

	// res := make([][]rune, img.Bounds().Dy())

	// for i := range res {
	// 	res[i] = make([]rune, img.Bounds().Dx())
	// }

	// for i := range res {
	// 	for j := range res[i] {
	// 		res[i][j] = convertPixel(img.At(j, i))
	// 	}
	// }
	// return res

	pixels := make([]byte, 100*100) // slice of your gray pixels, size of 100x100

	img := image.NewGray(image.Rect(0, 0, 100, 100))
	img.Pix = pixels

	fmt.Println(string(b))
}

func PrintImg(ascii [][]rune, o io.Writer) {
	for i := range ascii {
		for j := range ascii[i] {
			fmt.Fprint(o, string(ascii[i][j]))
		}
		fmt.Fprintln(o)
	}
}

func main() {
	flag.Parse()

	// Print with default helper functions
	color2.Cyan("Prints text in cyan.")

	// A newline will be appended automatically
	color2.Blue("Prints %s in blue.", "text")

	// These are using the default foreground colors
	color2.Red("We have red")
	color2.Magenta("And many others ..")

	if *fromASCII == "" {
		var terminalHeight, terminalWidth int

		if flag.NArg() < 1 {
			fmt.Println("Usage: asciimg <image>")
			os.Exit(0)
		}

		imgName := flag.Arg(0)

		img, err := openImage(imgName)
		if err != nil {
			panic(err)
		}

		terminalHeight = goterm.Height()
		terminalWidth = goterm.Width()

		if *noscale {
			terminalHeight = 50
			terminalWidth = 200
		}

		ascii := ToAscii(img, uint(terminalHeight), uint(terminalWidth))

		var o io.Writer

		if *output != "" {
			outF, err := os.Create(*output)
			if err != nil {
				fmt.Println("Error occured while opening file: ", err)
			}
			o = outF
		} else {
			o = os.Stdout
		}

		PrintImg(ascii, o)
	} else {
		FromAscii(*fromASCII)
	}

}
