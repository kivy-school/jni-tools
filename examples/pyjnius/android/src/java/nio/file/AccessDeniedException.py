from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AccessDeniedException"]

class AccessDeniedException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/AccessDeniedException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False)]