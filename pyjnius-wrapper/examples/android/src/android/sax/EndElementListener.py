from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EndElementListener"]

class EndElementListener(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/sax/EndElementListener"
    end = JavaMethod("()V")