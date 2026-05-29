from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UFormat"]

class UFormat(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/UFormat"
    __javaconstructor__ = [("()V", False)]