package main

import (
    "fmt"
    "log"
    "net/http"
)

func main() {
    fmt.Println("Data Visualization Server")
    router := NewRouter()

    log.Fatal(http.ListenAndServe(":5101", router))
}
