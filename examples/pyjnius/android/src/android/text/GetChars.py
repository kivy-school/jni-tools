from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GetChars"]

class GetChars(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/GetChars"
    getChars = JavaMethod("(II[CI)V")