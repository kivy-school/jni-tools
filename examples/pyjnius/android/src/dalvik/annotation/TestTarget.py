from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TestTarget"]

class TestTarget(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "dalvik/annotation/TestTarget"
    methodName = JavaMethod("()Ljava/lang/String;")
    conceptName = JavaMethod("()Ljava/lang/String;")
    methodArgs = JavaMethod("()[Ljava/lang/Class;")