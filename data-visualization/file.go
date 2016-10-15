package main

import (
    "fmt"
    "io/ioutil"
    "net/http"
    "strings"
)

func IndexGET(w http.ResponseWriter, r *http.Request) {
    unableToFetchHTMLFile := "Unable to fetch HTML file"

    htmlFile, err := ioutil.ReadFile("html/index.html")

    if err != nil {
        fmt.Println(err)
        http.Error(w, unableToFetchHTMLFile, 500)
    }

    fmt.Fprintf(w, "%s", htmlFile)
}

func FileGET(w http.ResponseWriter, r *http.Request) {
    unableToFetchFile := "Unable to fetch file"

    filename := "." + r.RequestURI

    file, err := ioutil.ReadFile(filename)

    if err != nil {
        fmt.Println(err)
        http.Error(w, unableToFetchFile, 500)
    }

    var contentType string

    switch splitList := strings.Split(filename, "."); splitList[len(splitList)-1] {
        case "css":
            contentType = "text/css"
        case "js":
            contentType = "text/javascript"
        default:
            contentType = "text/plain"
    }

    w.Header().Add("Content-Type", contentType)

    fmt.Fprintf(w, "%s", file)
}
