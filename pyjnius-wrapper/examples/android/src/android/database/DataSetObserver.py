from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DataSetObserver"]

class DataSetObserver(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/DataSetObserver"
    __javaconstructor__ = [("()V", False)]
    onChanged = JavaMethod("()V")
    onInvalidated = JavaMethod("()V")