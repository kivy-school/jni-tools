from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Comparable"]

class Comparable(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/Comparable"
    compareTo = JavaMethod("(Ljava/lang/Object;)I")