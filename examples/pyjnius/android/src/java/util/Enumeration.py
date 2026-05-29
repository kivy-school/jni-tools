from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Enumeration"]

class Enumeration(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/Enumeration"
    asIterator = JavaMethod("()Ljava/util/Iterator;")
    hasMoreElements = JavaMethod("()Z")
    nextElement = JavaMethod("()Ljava/lang/Object;")