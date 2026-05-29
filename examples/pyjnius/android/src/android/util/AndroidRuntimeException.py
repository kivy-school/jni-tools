from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AndroidRuntimeException"]

class AndroidRuntimeException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/AndroidRuntimeException"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/Exception;)V", False), ("()V", False)]