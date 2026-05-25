from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Enumeration"]

class Enumeration(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/Enumeration"
    hasMoreElements = JavaMethod("()Z")
    nextElement = JavaMethod("()Ljava/lang/Object;")
    asIterator = JavaMethod("()Ljava/util/Iterator;")