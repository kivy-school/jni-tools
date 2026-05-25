from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InheritableThreadLocal"]

class InheritableThreadLocal(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/InheritableThreadLocal"
    __javaconstructor__ = [("()V", False)]
    childValue = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")