from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FingerprintGestureController"]

class FingerprintGestureController(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/accessibilityservice/FingerprintGestureController"
    FINGERPRINT_GESTURE_SWIPE_DOWN = JavaStaticField("I")
    FINGERPRINT_GESTURE_SWIPE_LEFT = JavaStaticField("I")
    FINGERPRINT_GESTURE_SWIPE_RIGHT = JavaStaticField("I")
    FINGERPRINT_GESTURE_SWIPE_UP = JavaStaticField("I")
    isGestureDetectionAvailable = JavaMethod("()Z")
    registerFingerprintGestureCallback = JavaMethod("(Landroid/accessibilityservice/FingerprintGestureController$FingerprintGestureCallback;Landroid/os/Handler;)V")
    unregisterFingerprintGestureCallback = JavaMethod("(Landroid/accessibilityservice/FingerprintGestureController$FingerprintGestureCallback;)V")

    class FingerprintGestureCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/accessibilityservice/FingerprintGestureController$FingerprintGestureCallback"
        __javaconstructor__ = [("()V", False)]
        onGestureDetected = JavaMethod("(I)V")
        onGestureDetectionAvailabilityChanged = JavaMethod("(Z)V")