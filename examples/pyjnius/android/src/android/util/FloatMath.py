from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FloatMath"]

class FloatMath(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/FloatMath"