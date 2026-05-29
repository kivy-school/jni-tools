from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WebMessagePort"]

class WebMessagePort(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/WebMessagePort"
    postMessage = JavaMethod("(Landroid/webkit/WebMessage;)V")
    setWebMessageCallback = JavaMultipleMethod([("(Landroid/webkit/WebMessagePort$WebMessageCallback;)V", False, False), ("(Landroid/webkit/WebMessagePort$WebMessageCallback;Landroid/os/Handler;)V", False, False)])
    close = JavaMethod("()V")

    class WebMessageCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/webkit/WebMessagePort$WebMessageCallback"
        __javaconstructor__ = [("()V", False)]
        onMessage = JavaMethod("(Landroid/webkit/WebMessagePort;Landroid/webkit/WebMessage;)V")