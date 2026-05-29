from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CompletionHandler"]

class CompletionHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/CompletionHandler"
    failed = JavaMethod("(Ljava/lang/Throwable;Ljava/lang/Object;)V")
    completed = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)V")