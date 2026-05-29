from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ReceiverCallNotAllowedException"]

class ReceiverCallNotAllowedException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/ReceiverCallNotAllowedException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]