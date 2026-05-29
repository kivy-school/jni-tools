from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EndTextElementListener"]

class EndTextElementListener(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/sax/EndTextElementListener"
    end = JavaMethod("(Ljava/lang/String;)V")