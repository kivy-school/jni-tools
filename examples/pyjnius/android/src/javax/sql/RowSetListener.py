from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RowSetListener"]

class RowSetListener(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "javax/sql/RowSetListener"
    rowSetChanged = JavaMethod("(Ljavax/sql/RowSetEvent;)V")
    rowChanged = JavaMethod("(Ljavax/sql/RowSetEvent;)V")
    cursorMoved = JavaMethod("(Ljavax/sql/RowSetEvent;)V")