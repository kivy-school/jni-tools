from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UnrecoverableEntryException"]

class UnrecoverableEntryException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/UnrecoverableEntryException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]