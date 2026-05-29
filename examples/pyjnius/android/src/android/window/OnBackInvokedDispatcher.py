from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OnBackInvokedDispatcher"]

class OnBackInvokedDispatcher(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/window/OnBackInvokedDispatcher"
    PRIORITY_DEFAULT = JavaStaticField("I")
    PRIORITY_OVERLAY = JavaStaticField("I")
    registerOnBackInvokedCallback = JavaMethod("(ILandroid/window/OnBackInvokedCallback;)V")
    unregisterOnBackInvokedCallback = JavaMethod("(Landroid/window/OnBackInvokedCallback;)V")