from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AccessibilityButtonController"]

class AccessibilityButtonController(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/accessibilityservice/AccessibilityButtonController"
    registerAccessibilityButtonCallback = JavaMultipleMethod([("(Landroid/accessibilityservice/AccessibilityButtonController$AccessibilityButtonCallback;)V", False, False), ("(Landroid/accessibilityservice/AccessibilityButtonController$AccessibilityButtonCallback;Landroid/os/Handler;)V", False, False)])
    isAccessibilityButtonAvailable = JavaMethod("()Z")
    unregisterAccessibilityButtonCallback = JavaMethod("(Landroid/accessibilityservice/AccessibilityButtonController$AccessibilityButtonCallback;)V")

    class AccessibilityButtonCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/accessibilityservice/AccessibilityButtonController$AccessibilityButtonCallback"
        __javaconstructor__ = [("()V", False)]
        onClicked = JavaMethod("(Landroid/accessibilityservice/AccessibilityButtonController;)V")
        onAvailabilityChanged = JavaMethod("(Landroid/accessibilityservice/AccessibilityButtonController;Z)V")