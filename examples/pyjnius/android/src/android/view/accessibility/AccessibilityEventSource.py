from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AccessibilityEventSource"]

class AccessibilityEventSource(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/accessibility/AccessibilityEventSource"
    sendAccessibilityEvent = JavaMethod("(I)V")
    sendAccessibilityEventUnchecked = JavaMethod("(Landroid/view/accessibility/AccessibilityEvent;)V")