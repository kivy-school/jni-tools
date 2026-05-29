from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ReadRecordsRequestUsingIds"]

class ReadRecordsRequestUsingIds(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/ReadRecordsRequestUsingIds"
    getRecordIdFilters = JavaMethod("()Ljava/util/List;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/ReadRecordsRequestUsingIds$Builder"
        __javaconstructor__ = [("(Ljava/lang/Class;)V", False)]
        addClientRecordId = JavaMethod("(Ljava/lang/String;)Landroid/health/connect/ReadRecordsRequestUsingIds$Builder;")
        addId = JavaMethod("(Ljava/lang/String;)Landroid/health/connect/ReadRecordsRequestUsingIds$Builder;")
        build = JavaMethod("()Landroid/health/connect/ReadRecordsRequestUsingIds;")