from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AndroidException"]

class AndroidException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/AndroidException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/Exception;)V", False)]