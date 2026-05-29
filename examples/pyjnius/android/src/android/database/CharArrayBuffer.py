from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CharArrayBuffer"]

class CharArrayBuffer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/CharArrayBuffer"
    __javaconstructor__ = [("(I)V", False), ("([C)V", False)]
    data = JavaField("[C")
    sizeCopied = JavaField("I")