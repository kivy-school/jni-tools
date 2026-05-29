from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Session2Command"]

class Session2Command(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/Session2Command"
    __javaconstructor__ = [("(I)V", False), ("(Ljava/lang/String;Landroid/os/Bundle;)V", False)]
    COMMAND_CODE_CUSTOM = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getCustomExtras = JavaMethod("()Landroid/os/Bundle;")
    getCommandCode = JavaMethod("()I")
    getCustomAction = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Result(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/Session2Command$Result"
        __javaconstructor__ = [("(ILandroid/os/Bundle;)V", False)]
        RESULT_ERROR_UNKNOWN_ERROR = JavaStaticField("I")
        RESULT_INFO_SKIPPED = JavaStaticField("I")
        RESULT_SUCCESS = JavaStaticField("I")
        getResultCode = JavaMethod("()I")
        getResultData = JavaMethod("()Landroid/os/Bundle;")