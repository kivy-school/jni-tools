from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StartElementListener"]

class StartElementListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/sax/StartElementListener"
    start = JavaMethod("(Lorg/xml/sax/Attributes;)V")