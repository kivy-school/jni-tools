from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["QueryLocationException"]

class QueryLocationException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telecom/QueryLocationException"
    __javaconstructor__ = [("(Ljava/lang/String;ILjava/lang/Throwable;)V", False), ("(Ljava/lang/String;I)V", False), ("(Ljava/lang/String;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    ERROR_NOT_ALLOWED_FOR_NON_EMERGENCY_CONNECTIONS = JavaStaticField("I")
    ERROR_NOT_PERMITTED = JavaStaticField("I")
    ERROR_PREVIOUS_REQUEST_EXISTS = JavaStaticField("I")
    ERROR_REQUEST_TIME_OUT = JavaStaticField("I")
    ERROR_SERVICE_UNAVAILABLE = JavaStaticField("I")
    ERROR_UNSPECIFIED = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getCode = JavaMethod("()I")