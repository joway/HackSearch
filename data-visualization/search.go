package main

import (
    "encoding/json"
    "fmt"
    "io/ioutil"
    "net/http"
    "strconv"
)

type shards struct {
    Failed, Successful, Total int
}

type source struct {
    Title, Content, Url string
}

type record struct {
    Type string `json:"_type"`
    Index string `json:"_index"`
    Id string `json:"_id"`
    Source source `json:"_source"`
    Score float64 `json:"_score"`
}

type hits struct {
    Hits []record
    Max_score float64
    Total int
}

type searchData struct {
    Shards shards `json:"_shards"`
    Hits hits
    Took int
    Timed_out bool
}

func SearchGET(w http.ResponseWriter, r *http.Request) {
    unableToSearchForQuery := "Unable to search for query"

    var page int
    if pageStr := r.FormValue("page") ; pageStr == "" {
        page = 1
    } else {
        pageTemp, err := strconv.ParseInt(pageStr, 10, 0)
        if err != nil {
            fmt.Println(err)
            http.Error(w, unableToSearchForQuery, 500)
            return
        }
        page = int(pageTemp)
    }

    resp, err := http.Get(fmt.Sprintf("http://hack.joway.wang:8000/hack/search/?query=%s&&page=%d", r.FormValue("q"), page))
    if err != nil {
        fmt.Println(err)
        http.Error(w, unableToSearchForQuery, 500)
        return
    }
    defer resp.Body.Close()

    bodyStr, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        fmt.Println(err)
        http.Error(w, unableToSearchForQuery, 500)
        return
    }

    var j = []byte(bodyStr)
    var body searchData
    err = json.Unmarshal(j, &body)
    if err != nil {
        fmt.Println(err)
        http.Error(w, unableToSearchForQuery, 500)
        return
    }

    str := "<ul>"
    total := int(body.Took)
    for i := 0; i < total; i++ {
        record := body.Hits.Hits[i]
        title := record.Source.Title
        content := record.Source.Content
        url := record.Source.Url
        str += fmt.Sprintf("<li><a href=\"%s\"><h3 class=\"title\">%s</h3></a><p class=\"content\">%s</p><a class=\"url\" href=\"%s\">%s</a></li>", url, title, content, url, url)
    }
    str += "</ul>"

    header, err := ioutil.ReadFile("html/header.html")
    if err != nil {
        fmt.Println(err)
        http.Error(w, unableToSearchForQuery, 500)
        return
    }

    footer, err := ioutil.ReadFile("html/footer.html")
    if err != nil {
        fmt.Println(err)
        http.Error(w, unableToSearchForQuery, 500)
        return
    }

    fmt.Fprintf(w, "%s", string(header) + str + string(footer))
}
