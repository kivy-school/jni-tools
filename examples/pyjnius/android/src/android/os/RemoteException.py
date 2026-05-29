from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RemoteException"]

class RemoteException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/RemoteException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]
    rethrowFromSystemServer = JavaMethod("()Ljava/lang/RuntimeException;")
    rethrowAsRuntimeException = JavaMethod("()Ljava/lang/RuntimeException;")