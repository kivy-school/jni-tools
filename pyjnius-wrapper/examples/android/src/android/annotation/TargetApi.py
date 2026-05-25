from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TargetApi"]

class TargetApi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/annotation/TargetApi"
    value = JavaMethod("()I")