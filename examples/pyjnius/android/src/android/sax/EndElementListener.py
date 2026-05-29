from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EndElementListener"]

class EndElementListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/sax/EndElementListener"
    end = JavaMethod("()V")