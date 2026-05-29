from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RecursiveAction"]

class RecursiveAction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/RecursiveAction"
    __javaconstructor__ = [("()V", False)]
    getRawResult = JavaMultipleMethod([("()Ljava/lang/Void;", False, False), ("()Ljava/lang/Object;", False, False)])