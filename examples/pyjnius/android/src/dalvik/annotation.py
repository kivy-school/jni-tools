from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class TestTarget(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "dalvik/annotation/TestTarget"
    conceptName = JavaMethod("()Ljava/lang/String;")
    methodArgs = JavaMethod("()[Ljava/lang/Class;")
    methodName = JavaMethod("()Ljava/lang/String;")

class TestTargetClass(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "dalvik/annotation/TestTargetClass"
    value = JavaMethod("()Ljava/lang/Class;")