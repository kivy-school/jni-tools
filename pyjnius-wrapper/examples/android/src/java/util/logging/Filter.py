from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Filter"]

class Filter(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/logging/Filter"
    isLoggable = JavaMethod("(Ljava/util/logging/LogRecord;)Z")