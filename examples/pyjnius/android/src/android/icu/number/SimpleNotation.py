from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SimpleNotation"]

class SimpleNotation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/number/SimpleNotation"