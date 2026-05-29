from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OnBackInvokedDispatcher"]

class OnBackInvokedDispatcher(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/window/OnBackInvokedDispatcher"
    PRIORITY_DEFAULT = JavaStaticField("I")
    PRIORITY_OVERLAY = JavaStaticField("I")
    PRIORITY_SYSTEM_NAVIGATION_OBSERVER = JavaStaticField("I")
    unregisterOnBackInvokedCallback = JavaMethod("(Landroid/window/OnBackInvokedCallback;)V")
    registerOnBackInvokedCallback = JavaMethod("(ILandroid/window/OnBackInvokedCallback;)V")