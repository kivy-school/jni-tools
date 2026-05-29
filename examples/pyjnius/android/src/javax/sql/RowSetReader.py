from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RowSetReader"]

class RowSetReader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/sql/RowSetReader"
    readData = JavaMethod("(Ljavax/sql/RowSetInternal;)V")