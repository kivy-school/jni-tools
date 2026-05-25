from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ProcessingInstruction"]

class ProcessingInstruction(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/ProcessingInstruction"
    getTarget = JavaMethod("()Ljava/lang/String;")
    getData = JavaMethod("()Ljava/lang/String;")
    setData = JavaMethod("(Ljava/lang/String;)V")