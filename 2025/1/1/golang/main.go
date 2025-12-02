package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

type Dial struct{ value, zeros int }

func NewDial(v int) *Dial { return &Dial{value: v % 100} }

func (d *Dial) Left(n int) {
	// fmt.Println("Turning left:", n)
	d.value = (d.value - n + 100) % 100
	if d.value == 0 {
		d.zeros++
	}
	// fmt.Println("The value is:", d.value)
}

func (d *Dial) Right(n int) {
	// fmt.Println("Turning right:", n)
	d.value = (d.value + n) % 100
	if d.value == 0 {
		d.zeros++
	}
	// fmt.Println("The value is:", d.value)
}

func main() {
	d := NewDial(50)
	sc := bufio.NewScanner(os.Stdin)

	for sc.Scan() {
		mov := sc.Text()
		if mov == "" {
			break
		}
		dir := mov[0]
		n, _ := strconv.Atoi(mov[1:])
		if dir == 'L' {
			d.Left(n)
		} else if dir == 'R' {
			d.Right(n)
		}
	}

	fmt.Println("The password is:", d.zeros)
}
