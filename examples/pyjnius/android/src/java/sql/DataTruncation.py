from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DataTruncation"]

class DataTruncation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/sql/DataTruncation"
    __javaconstructor__ = [("(IZZII)V", False), ("(IZZIILjava/lang/Throwable;)V", False)]
    getIndex = JavaMethod("()I")
    getParameter = JavaMethod("()Z")
    getRead = JavaMethod("()Z")
    getDataSize = JavaMethod("()I")
    getTransferSize = JavaMethod("()I")