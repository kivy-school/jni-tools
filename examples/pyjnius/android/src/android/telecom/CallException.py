from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CallException"]

class CallException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telecom/CallException"
    __javaconstructor__ = [("(Ljava/lang/String;I)V", False)]
    CODE_CALL_CANNOT_BE_SET_TO_ACTIVE = JavaStaticField("I")
    CODE_CALL_IS_NOT_BEING_TRACKED = JavaStaticField("I")
    CODE_CALL_NOT_PERMITTED_AT_PRESENT_TIME = JavaStaticField("I")
    CODE_CANNOT_HOLD_CURRENT_ACTIVE_CALL = JavaStaticField("I")
    CODE_ERROR_UNKNOWN = JavaStaticField("I")
    CODE_OPERATION_TIMED_OUT = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getCode = JavaMethod("()I")