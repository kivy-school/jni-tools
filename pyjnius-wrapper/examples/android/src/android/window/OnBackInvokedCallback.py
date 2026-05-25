from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OnBackInvokedCallback"]

class OnBackInvokedCallback(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/window/OnBackInvokedCallback"
    onBackInvoked = JavaMethod("()V")