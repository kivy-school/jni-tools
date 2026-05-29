from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LoggingPermission"]

class LoggingPermission(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/logging/LoggingPermission"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;)V", False)]