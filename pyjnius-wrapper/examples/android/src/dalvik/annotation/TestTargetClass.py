from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TestTargetClass"]

class TestTargetClass(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "dalvik/annotation/TestTargetClass"
    value = JavaMethod("()Ljava/lang/Class;")