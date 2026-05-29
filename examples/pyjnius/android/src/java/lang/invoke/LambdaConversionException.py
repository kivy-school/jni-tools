from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LambdaConversionException"]

class LambdaConversionException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/invoke/LambdaConversionException"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/Throwable;ZZ)V", False), ("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;)V", False), ("()V", False)]