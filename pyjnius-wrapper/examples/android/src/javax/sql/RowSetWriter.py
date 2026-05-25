from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RowSetWriter"]

class RowSetWriter(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "javax/sql/RowSetWriter"
    writeData = JavaMethod("(Ljavax/sql/RowSetInternal;)Z")