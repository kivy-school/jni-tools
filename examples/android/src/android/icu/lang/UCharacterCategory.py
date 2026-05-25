from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UCharacterCategory"]

class UCharacterCategory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/lang/UCharacterCategory"
    toString = JavaStaticMethod("(I)Ljava/lang/String;")