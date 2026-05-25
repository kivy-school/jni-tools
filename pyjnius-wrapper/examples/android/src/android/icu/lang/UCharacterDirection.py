from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UCharacterDirection"]

class UCharacterDirection(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/lang/UCharacterDirection"
    toString = JavaStaticMethod("(I)Ljava/lang/String;")