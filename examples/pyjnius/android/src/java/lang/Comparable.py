from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Comparable"]

class Comparable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/Comparable"
    compareTo = JavaMethod("(Ljava/lang/Object;)I")