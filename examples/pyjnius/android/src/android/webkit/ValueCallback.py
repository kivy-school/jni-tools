from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ValueCallback"]

class ValueCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/ValueCallback"
    onReceiveValue = JavaMethod("(Ljava/lang/Object;)V")