from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CursorWindowAllocationException"]

class CursorWindowAllocationException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/CursorWindowAllocationException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]