from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GetChars"]

class GetChars(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/GetChars"
    getChars = JavaMethod("(II[CI)V")