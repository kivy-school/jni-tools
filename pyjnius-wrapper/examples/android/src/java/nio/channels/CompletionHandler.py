from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CompletionHandler"]

class CompletionHandler(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/CompletionHandler"
    completed = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)V")
    failed = JavaMethod("(Ljava/lang/Throwable;Ljava/lang/Object;)V")