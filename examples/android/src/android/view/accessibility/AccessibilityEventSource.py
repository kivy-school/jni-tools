from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AccessibilityEventSource"]

class AccessibilityEventSource(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/accessibility/AccessibilityEventSource"
    sendAccessibilityEvent = JavaMethod("(I)V")
    sendAccessibilityEventUnchecked = JavaMethod("(Landroid/view/accessibility/AccessibilityEvent;)V")