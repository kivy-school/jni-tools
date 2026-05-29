from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TestTarget"]

class TestTarget(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "dalvik/annotation/TestTarget"
    conceptName = JavaMethod("()Ljava/lang/String;")
    methodArgs = JavaMethod("()[Ljava/lang/Class;")
    methodName = JavaMethod("()Ljava/lang/String;")