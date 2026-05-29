from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OnBackInvokedCallback"]

class OnBackInvokedCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/window/OnBackInvokedCallback"
    onBackInvoked = JavaMethod("()V")