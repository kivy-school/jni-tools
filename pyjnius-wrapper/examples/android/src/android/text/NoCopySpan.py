from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NoCopySpan"]

class NoCopySpan(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/NoCopySpan"

    class Concrete(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/text/NoCopySpan/Concrete"
        __javaconstructor__ = [("()V", False)]