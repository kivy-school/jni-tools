package com.example.fixture;

/** Outer with a Builder-style nested class. */
public class Content {

    public String body;

    public Content(String body) {
        this.body = body;
    }

    /** Builder for {@link Content}. */
    public static class Builder {
        private String body;

        public Builder setBody(String body) {
            this.body = body;
            return this;
        }

        public Content build() {
            return new Content(this.body);
        }
    }
}
