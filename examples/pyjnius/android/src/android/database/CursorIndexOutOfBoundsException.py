from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CursorIndexOutOfBoundsException"]

class CursorIndexOutOfBoundsException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/CursorIndexOutOfBoundsException"
    __javaconstructor__ = [("(II)V", False), ("(Ljava/lang/String;)V", False)]