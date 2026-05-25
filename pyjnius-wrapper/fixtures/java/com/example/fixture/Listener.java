package com.example.fixture;

/** A simple listener interface. Used to test interface emission. */
public interface Listener {

    /** Called when something happens. */
    void onEvent(String name, int code);

    /** Default helper. */
    default boolean isReady() {
        return true;
    }

    String TAG = "Listener";
}
