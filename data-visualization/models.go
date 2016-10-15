package main

type Blog struct {
    Url string `json:"url"`
    Title string `json:"title"`
    Content string `json:"content"`
    Key string `json:"key"`
    Date string `json:"date"`
}

type Blogs []Blog

type Link struct {
    From string `json:"from"`
    To string `json:"to"`
    Dist int `json:"dist"`
}

type Links []Link
