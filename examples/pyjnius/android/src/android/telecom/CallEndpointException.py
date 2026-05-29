from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CallEndpointException"]

class CallEndpointException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telecom/CallEndpointException"
    __javaconstructor__ = [("(Ljava/lang/String;I)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    ERROR_ANOTHER_REQUEST = JavaStaticField("I")
    ERROR_ENDPOINT_DOES_NOT_EXIST = JavaStaticField("I")
    ERROR_REQUEST_TIME_OUT = JavaStaticField("I")
    ERROR_UNSPECIFIED = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getCode = JavaMethod("()I")