package com.example.fixture;

/** Traffic-light enum with a custom method. */
public enum Color {
    RED,
    GREEN,
    BLUE;

    public String describe() {
        return name().toLowerCase();
    }
}
