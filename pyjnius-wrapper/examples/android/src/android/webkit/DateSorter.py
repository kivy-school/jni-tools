from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DateSorter"]

class DateSorter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/DateSorter"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False)]
    DAY_COUNT = JavaStaticField("I")
    getIndex = JavaMethod("(J)I")
    getLabel = JavaMethod("(I)Ljava/lang/String;")
    getBoundary = JavaMethod("(I)J")