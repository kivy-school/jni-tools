from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Runnable"]

class Runnable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/Runnable"
    run = JavaMethod("()V")