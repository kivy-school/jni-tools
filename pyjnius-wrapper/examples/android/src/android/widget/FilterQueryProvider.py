from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FilterQueryProvider"]

class FilterQueryProvider(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/FilterQueryProvider"
    runQuery = JavaMethod("(Ljava/lang/CharSequence;)Landroid/database/Cursor;")