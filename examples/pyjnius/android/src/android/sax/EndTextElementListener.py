from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EndTextElementListener"]

class EndTextElementListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/sax/EndTextElementListener"
    end = JavaMethod("(Ljava/lang/String;)V")