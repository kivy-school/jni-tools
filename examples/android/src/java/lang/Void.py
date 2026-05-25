from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Void"]

class Void(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/Void"
    TYPE = JavaStaticField("Ljava/lang/Class;")