from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FunctionalInterface"]

class FunctionalInterface(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/FunctionalInterface"