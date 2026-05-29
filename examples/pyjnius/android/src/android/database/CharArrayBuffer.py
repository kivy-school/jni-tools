from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CharArrayBuffer"]

class CharArrayBuffer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/CharArrayBuffer"
    __javaconstructor__ = [("([C)V", False), ("(I)V", False)]
    data = JavaField("[C")
    sizeCopied = JavaField("I")