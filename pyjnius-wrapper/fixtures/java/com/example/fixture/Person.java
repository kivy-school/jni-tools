package com.example.fixture;

/**
 * Represents a person with a name and age.
 * Used as a smoke-test fixture for the pyjnius-wrap generator.
 */
public class Person {

    public static final String SPECIES = "human";

    public String name;
    protected int age;

    public Person(String name) {
        this(name, 0);
    }

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    /** Greet the named recipient. */
    public String greet(String other) {
        return "Hello, " + other + ", I am " + this.name;
    }

    /** Greet with an explicit prefix. */
    public String greet(String prefix, String other) {
        return prefix + ", " + other;
    }

    public static Person anonymous() {
        return new Person("anonymous");
    }

    public int getAge() {
        return age;
    }

    public void addTags(String... tags) {
        // varargs example
    }
}
