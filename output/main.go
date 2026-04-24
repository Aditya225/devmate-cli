go
// FILE: main.go
package main

import (
    "log"
    "net/http"
    "github.com/gorilla/mux"
    "your_project/database"
    "your_project/routes"
)

func main() {
    database.Connect()
    r := mux.NewRouter()
    routes.UserRoutes(r)
    log.Println("Server starting on port 8080...")
    if err := http.ListenAndServe(":8080", r); err != nil {
        log.Fatal(err)
    }
}

// FILE: models/user.go
package models

type User struct {
    ID    uint   `json:"id"`
    Name  string `json:"name"`
    Email string `json:"email"`
}

// FILE: database/database.go
package database

import (
    "database/sql"
    "log"
    _ "github.com/lib/pq"
)

var DB *sql.DB

func Connect() {
    var err error
    DB, err = sql.Open("postgres", "user=username dbname=mydb sslmode=disable")
    if err != nil {
        log.Fatalf("Failed to connect to the database: %v", err)
    }
    if err = DB.Ping(); err != nil {
        log.Fatalf("Failed to ping the database: %v", err)
    }
}

// FILE: routes/user.go
package routes

import (
    "your_project/controllers"
    "github.com/gorilla/mux"
)

func UserRoutes(r *mux.Router) {
    r.HandleFunc("/users", controllers.CreateUser).Methods("POST")
    r.HandleFunc("/users/{id}", controllers.GetUser).Methods("GET")
    r.HandleFunc("/users/{id}", controllers.UpdateUser).Methods("PUT")
    r.HandleFunc("/users/{id}", controllers.DeleteUser).Methods("DELETE")
}

// FILE: controllers/userController.go
package controllers

import (
    "encoding/json"
    "net/http"
    "github.com/gorilla/mux"
    "your_project/models"
    "your_project/database"
    "log"
)

func CreateUser(w http.ResponseWriter, r *http.Request) {
    var user models.User
    if err := json.NewDecoder(r.Body).Decode(&user); err != nil {
        http.Error(w, err.Error(), http.StatusBadRequest)
        return
    }
    err := database.DB.QueryRow(
        "INSERT INTO users (name, email) VALUES ($1, $2) RETURNING id",
        user.Name, user.Email).Scan(&user.ID)
    if err != nil {
        http.Error(w, err.Error(), http.StatusInternalServerError)
        return
    }
    w.WriteHeader(http.StatusCreated)
    json.NewEncoder(w).Encode(user)
}

func GetUser(w http.ResponseWriter, r *http.Request) {
    params := mux.Vars(r)
    var user models.User
    err := database.DB.QueryRow("SELECT id, name, email FROM users WHERE id=$1", params["id"]).Scan(&user.ID, &user.Name, &user.Email)
    if err != nil {
        http.Error(w, err.Error(), http.StatusNotFound)
        return
    }
    json.NewEncoder(w).Encode(user)
}

func UpdateUser(w http.ResponseWriter, r *http.Request) {
    params := mux.Vars(r)
    var user models.User
    if err := json.NewDecoder(r.Body).Decode(&user); err != nil {
        http.Error(w, err.Error(), http.StatusBadRequest)
        return
    }
    _, err := database.DB.Exec("UPDATE users SET name=$1, email=$2 WHERE id=$3", user.Name, user.Email, params["id"])
    if err != nil {
        http.Error(w, err.Error(), http.StatusInternalServerError)
        return
    }
    user.ID, _ = strconv.Atoi(params["id"]) // Convert id back to int
    json.NewEncoder(w).Encode(user)
}

func DeleteUser(w http.ResponseWriter, r *http.Request) {
    params := mux.Vars(r)
    _, err := database.DB.Exec("DELETE FROM users WHERE id=$1", params["id"])
    if err != nil {
        http.Error(w, err.Error(), http.StatusInternalServerError)
        return
    }
    w.WriteHeader(http.StatusNoContent)
}