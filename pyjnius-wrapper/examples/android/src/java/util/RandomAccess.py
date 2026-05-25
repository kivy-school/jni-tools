from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RandomAccess"]

class RandomAccess(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/RandomAccess"