package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

type Dial struct{ value, zeros int }

func NewDial(v int) *Dial { return &Dial{value: v % 100} }

func Abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func (d *Dial) Left(n int) {
	// fmt.Println("Turning left:", n)
	if d.value-n <= 0 {
		add := (n - d.value) / 100
		if d.value != 0 {
			add++
		}
		d.zeros += add
		// if add > 0 {
		//	fmt.Println("Crossed zero", add, "times, bringing the zero count to", d.zeros)
		// }
	}
	d.value = (d.value - n) % 100
	if d.value < 0 {
		d.value += 100
	}
}

func (d *Dial) Right(n int) {
	// fmt.Println("Turning right:", n)
	if d.value+n >= 100 {
		add := (n - (100 - d.value)) / 100
		if d.value != 0 || n >= 100 {
			add++
		}
		d.zeros += add
		// if add > 0 {
		// 	fmt.Println("Crossed zero", add, "times, bringing the zero count to", d.zeros)
		// }
	}
	d.value = (d.value + n) % 100
}

func main() {
	d := NewDial(50)
	sc := bufio.NewScanner(os.Stdin)

	for sc.Scan() {
		mov := sc.Text()
		if mov == "" {
			break
		}
		// fmt.Println("Read ", mov)
		dir := mov[0]
		n, _ := strconv.Atoi(mov[1:])
		switch dir {
		case 'L':
			d.Left(n)
		case 'R':
			d.Right(n)
		}
		// fmt.Println("The value is:", d.value)
	}

	fmt.Println("The password is:", d.zeros)
}
