from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StartElementListener"]

class StartElementListener(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/sax/StartElementListener"
    start = JavaMethod("(Lorg/xml/sax/Attributes;)V")