from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SuppressLint"]

class SuppressLint(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/annotation/SuppressLint"
    value = JavaMethod("()[Ljava/lang/String;")