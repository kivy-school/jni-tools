from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NoCopySpan"]

class NoCopySpan(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/NoCopySpan"

    class Concrete(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/text/NoCopySpan$Concrete"
        __javaconstructor__ = [("()V", False)]