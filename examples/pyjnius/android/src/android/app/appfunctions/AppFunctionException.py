from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AppFunctionException"]

class AppFunctionException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appfunctions/AppFunctionException"
    __javaconstructor__ = [("(ILjava/lang/String;)V", False), ("(ILjava/lang/String;Landroid/os/Bundle;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    ERROR_APP_UNKNOWN_ERROR = JavaStaticField("I")
    ERROR_CANCELLED = JavaStaticField("I")
    ERROR_CATEGORY_APP = JavaStaticField("I")
    ERROR_CATEGORY_REQUEST_ERROR = JavaStaticField("I")
    ERROR_CATEGORY_SYSTEM = JavaStaticField("I")
    ERROR_CATEGORY_UNKNOWN = JavaStaticField("I")
    ERROR_DENIED = JavaStaticField("I")
    ERROR_DISABLED = JavaStaticField("I")
    ERROR_ENTERPRISE_POLICY_DISALLOWED = JavaStaticField("I")
    ERROR_FUNCTION_NOT_FOUND = JavaStaticField("I")
    ERROR_INVALID_ARGUMENT = JavaStaticField("I")
    ERROR_SYSTEM_ERROR = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getErrorMessage = JavaMethod("()Ljava/lang/String;")
    getErrorCategory = JavaMethod("()I")
    getExtras = JavaMethod("()Landroid/os/Bundle;")
    getErrorCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")