from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RowSetWriter"]

class RowSetWriter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/sql/RowSetWriter"
    writeData = JavaMethod("(Ljavax/sql/RowSetInternal;)Z")