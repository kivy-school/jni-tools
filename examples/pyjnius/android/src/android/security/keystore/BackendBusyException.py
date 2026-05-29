from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BackendBusyException"]

class BackendBusyException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/keystore/BackendBusyException"
    __javaconstructor__ = [("(J)V", False), ("(JLjava/lang/String;Ljava/lang/Throwable;)V", False), ("(JLjava/lang/String;)V", False)]
    getBackOffHintMillis = JavaMethod("()J")