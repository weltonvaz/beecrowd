package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	caseNumber := 1

	for {
		fmt.Printf("Caso #%d:\n", caseNumber)

		// Ler o primeiro número
		if !scanner.Scan() {
			break
		}
		n1 := scanner.Text()

		// Ler o segundo número
		if !scanner.Scan() {
			break
		}
		n2 := scanner.Text()

		// Contar as subsequências
		qtd := strings.Count(n2, n1)
		if qtd == 0 {
			fmt.Println("Nao existe subsequencia")
		} else {
			fmt.Printf("Qtd.Subsequencias: %d\n", qtd)
			pos := strings.LastIndex(n2, n1) + 1
			fmt.Printf("Pos: %d\n", pos)
		}

		fmt.Println()
		caseNumber++
	}
}
