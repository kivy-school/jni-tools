from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Filter"]

class Filter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/logging/Filter"
    isLoggable = JavaMethod("(Ljava/util/logging/LogRecord;)Z")