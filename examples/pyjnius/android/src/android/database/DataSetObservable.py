from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DataSetObservable"]

class DataSetObservable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/DataSetObservable"
    __javaconstructor__ = [("()V", False)]
    notifyChanged = JavaMethod("()V")
    notifyInvalidated = JavaMethod("()V")