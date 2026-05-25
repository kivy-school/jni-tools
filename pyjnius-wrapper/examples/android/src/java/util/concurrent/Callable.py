from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Callable"]

class Callable(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/Callable"
    call = JavaMethod("()Ljava/lang/Object;")