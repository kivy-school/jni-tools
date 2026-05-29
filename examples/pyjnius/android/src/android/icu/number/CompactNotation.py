from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CompactNotation"]

class CompactNotation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/number/CompactNotation"