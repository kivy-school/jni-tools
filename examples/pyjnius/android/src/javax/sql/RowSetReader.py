from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RowSetReader"]

class RowSetReader(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "javax/sql/RowSetReader"
    readData = JavaMethod("(Ljavax/sql/RowSetInternal;)V")