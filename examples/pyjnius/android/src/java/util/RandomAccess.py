from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RandomAccess"]

class RandomAccess(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/RandomAccess"