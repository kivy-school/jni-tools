from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UpdateLayout"]

class UpdateLayout(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/UpdateLayout"