from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NotProvisionedException"]

class NotProvisionedException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/NotProvisionedException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]