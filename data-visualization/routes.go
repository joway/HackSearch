package main

import "net/http"

type Route struct {
    Name string
    Method string
    Pattern string
    HandlerFunc http.HandlerFunc
}

type Routes []Route

var routes = Routes {
    Route {
        "Index",
        "GET",
        "/",
        IndexGET,
    },
    Route {
        "Search",
        "GET",
        "/search",
        SearchGET,
    },
    Route {
        "KeywordFrequency",
        "GET",
        "/api/keyword-frequency",
        KeywordFrequencyGET,
    },
    Route {
        "KeywordLinks",
        "GET",
        "/api/keyword-links",
        KeywordLinksGET,
    },
    Route {
        "CSSFile",
        "GET",
        "/css/{filename}",
        FileGET,
    },
    Route {
        "JSFile",
        "GET",
        "/js/{filename}",
        FileGET,
    },
    Route {
        "FontFile",
        "GET",
        "/fonts/{filename}",
        FileGET,
    },
}
