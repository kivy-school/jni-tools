from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WebViewRenderProcess"]

class WebViewRenderProcess(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/WebViewRenderProcess"
    __javaconstructor__ = [("()V", False)]
    terminate = JavaMethod("()Z")