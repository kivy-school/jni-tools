from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ValueCallback"]

class ValueCallback(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/ValueCallback"
    onReceiveValue = JavaMethod("(Ljava/lang/Object;)V")