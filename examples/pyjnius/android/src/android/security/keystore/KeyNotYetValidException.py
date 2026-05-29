from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyNotYetValidException"]

class KeyNotYetValidException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/keystore/KeyNotYetValidException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False)]