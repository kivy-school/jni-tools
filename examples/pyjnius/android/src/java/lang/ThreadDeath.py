from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ThreadDeath"]

class ThreadDeath(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/ThreadDeath"
    __javaconstructor__ = [("()V", False)]