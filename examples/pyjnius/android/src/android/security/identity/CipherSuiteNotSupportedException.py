from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CipherSuiteNotSupportedException"]

class CipherSuiteNotSupportedException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/identity/CipherSuiteNotSupportedException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False)]