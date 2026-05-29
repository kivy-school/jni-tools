from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ReferenceQueue"]

class ReferenceQueue(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/ref/ReferenceQueue"
    __javaconstructor__ = [("()V", False)]
    remove = JavaMultipleMethod([("()Ljava/lang/ref/Reference;", False, False), ("(J)Ljava/lang/ref/Reference;", False, False)])
    poll = JavaMethod("()Ljava/lang/ref/Reference;")