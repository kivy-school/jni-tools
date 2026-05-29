from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AbstractSet"]

class AbstractSet(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/AbstractSet"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    removeAll = JavaMethod("(Ljava/util/Collection;)Z")