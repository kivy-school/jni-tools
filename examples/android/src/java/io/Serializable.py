from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Serializable"]

class Serializable(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/Serializable"