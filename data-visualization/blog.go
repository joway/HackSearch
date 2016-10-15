package main

import (
    "database/sql"
    "encoding/json"
    "fmt"
    "net/http"
    "strings"
    "time"

    _ "github.com/Go-SQL-Driver/MySQL"
)

type edge struct {
    First, Second string
}

func allBlogs(w http.ResponseWriter, r *http.Request) Blogs {
    unableToFetchBlogData := "Unable to fetch blog data"

    db, err := sql.Open("mysql", user + ":" + passwd + "@tcp(" + host + ":" + port + ")/" + db + "?charset=utf8")
    defer db.Close()

    if err != nil {
        fmt.Println(err)
        http.Error(w, unableToFetchBlogData, 500)
        return nil
    }

    rows, err := db.Query("SELECT url, title, content, keyset, created_at FROM " + table)

    if err != nil {
        fmt.Println(err)
        http.Error(w, unableToFetchBlogData, 500)
        return nil
    }

    var blogs Blogs

    for rows.Next() {
        var urlStr, titleStr, contentStr, keyStr, dateStr sql.NullString
        if err := rows.Scan(&urlStr, &titleStr, &contentStr, &keyStr, &dateStr); err != nil {
            fmt.Println(err)
            continue
        }

        url := urlStr.String
        title := titleStr.String
        content := contentStr.String
        key := keyStr.String
        date := dateStr.String

        blogs = append(
            blogs,
            Blog {
                url,
                title,
                content,
                key,
                date,
            },
        )
    }

    return blogs
}

func KeywordFrequencyGET(w http.ResponseWriter, r *http.Request) {
    unableToSendBlogData := "Unable to send blog data"

    blogs := allBlogs(w, r)
    if blogs == nil {
        return
    }

    keyMap := make(map[string]int)

    for i := 0; i < len(blogs); i++ {
        createTime, err := time.Parse("2006-01-02", blogs[i].Date)
        if err != nil {
            fmt.Println(err)
            continue
        }

        nowTime := time.Now()
        yearAgo := time.Date(nowTime.Year() - 1, nowTime.Month(), nowTime.Day(), 0, 0, 0, 0, time.UTC)

        if createTime.Before(yearAgo) {
            continue
        }

        keys := strings.Split(blogs[i].Key, " ")
        for j := 0; j < len(keys); j++ {
            if keys[j] != "" {
                keyMap[keys[j]]++
            }
        }
    }

    if err := json.NewEncoder(w).Encode(keyMap); err != nil {
        fmt.Println(err)
        http.Error(w, unableToSendBlogData, 500)
        return
    }
}

func KeywordLinksGET(w http.ResponseWriter, r *http.Request) {
    unableToSendBlogData := "Unable to send blog data"

    blogs := allBlogs(w, r)
    if blogs == nil {
        return
    }

    keyMap := make(map[edge]int)

    for i := 0; i < len(blogs); i++ {
        keys := strings.Split(blogs[i].Key, " ")
        for j := 0; j < len(keys); j++ {
            for k := j + 1; k < len(keys); k++ {
                if keys[j] != "" && keys[k] != "" {
                    keyMap[edge{keys[j], keys[k]}]++
                }
            }
        }
    }

    var links Links

    for pair, value := range keyMap {
        links = append(
            links,
            Link {
                pair.First,
                pair.Second,
                value,
            },
        )
    }

    if err := json.NewEncoder(w).Encode(links); err != nil {
        fmt.Println(err)
        http.Error(w, unableToSendBlogData, 500)
        return
    }
}
