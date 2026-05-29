from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DocTypeNotSupportedException"]

class DocTypeNotSupportedException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/identity/DocTypeNotSupportedException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False)]