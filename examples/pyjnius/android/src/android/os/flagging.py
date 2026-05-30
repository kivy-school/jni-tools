from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class AconfigStorageReadException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/flagging/AconfigStorageReadException"
    __javaconstructor__ = [("(ILjava/lang/Throwable;)V", False), ("(ILjava/lang/String;Ljava/lang/Throwable;)V", False), ("(ILjava/lang/String;)V", False)]
    ERROR_CANNOT_READ_STORAGE_FILE = JavaStaticField("I")
    ERROR_CONTAINER_NOT_FOUND = JavaStaticField("I")
    ERROR_GENERIC = JavaStaticField("I")
    ERROR_PACKAGE_NOT_FOUND = JavaStaticField("I")
    ERROR_STORAGE_SYSTEM_NOT_FOUND = JavaStaticField("I")
    getMessage = JavaMethod("()Ljava/lang/String;")
    getErrorCode = JavaMethod("()I")

class AconfigPackage(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/flagging/AconfigPackage"
    getBooleanFlagValue = JavaMethod("(Ljava/lang/String;Z)Z")
    load = JavaStaticMethod("(Ljava/lang/String;)Landroid/os/flagging/AconfigPackage;")