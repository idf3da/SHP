package main

import (
    "fmt"
)

type Operation interface {
    Do(int, int) int
}

type PlusOperation struct {
    plus bool
}

func (so PlusOperation) Do(a,b int) int {
    if so.plus {
        return a + b
    } else {
        return a - b
    }
}

type MultiplyOperation struct {
}

func (mo MultiplyOperation) Do(a,b int) int {
    return a * b
}

func DoCalc(op Operation, a int, b int) int {
    return op.Do(a,b)
}

func main() {
    var a,b int
    var op rune
    fmt.Scanf("%d %c %d", &a, &op, &b)
    var oper Operation
    if op == '+' {
        oper = PlusOperation{true}
    }
    if op == '-' {
        oper = PlusOperation{false}
    }
    if op == '*' {
        oper = MultiplyOperation{}
    }
    fmt.Println(DoCalc(oper, a, b))
}
