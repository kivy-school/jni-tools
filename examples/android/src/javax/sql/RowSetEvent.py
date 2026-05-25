from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RowSetEvent"]

class RowSetEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/sql/RowSetEvent"
    __javaconstructor__ = [("(Ljavax/sql/RowSet;)V", False)]