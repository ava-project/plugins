//go.go
package main

import (
		"C"
		"fmt"
)

//export hello
func hello(str string) {
	fmt.Println("hello", str)
}

func main() {

}
