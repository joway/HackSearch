package main

import (
    "fmt"
    "log"
    "net/http"
)

func main() {
    fmt.Println("Go Webpage Server")
    router := NewRouter()

    log.Fatal(http.ListenAndServe(":5101", router))
}
