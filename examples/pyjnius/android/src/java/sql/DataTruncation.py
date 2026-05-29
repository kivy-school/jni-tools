from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DataTruncation"]

class DataTruncation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/sql/DataTruncation"
    __javaconstructor__ = [("(IZZIILjava/lang/Throwable;)V", False), ("(IZZII)V", False)]
    getDataSize = JavaMethod("()I")
    getRead = JavaMethod("()Z")
    getTransferSize = JavaMethod("()I")
    getParameter = JavaMethod("()Z")
    getIndex = JavaMethod("()I")