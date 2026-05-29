from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SetValueResult"]

class SetValueResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/settings/preferences/SetValueResult"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    RESULT_DISABLED = JavaStaticField("I")
    RESULT_DISALLOW = JavaStaticField("I")
    RESULT_INTERNAL_ERROR = JavaStaticField("I")
    RESULT_INVALID_REQUEST = JavaStaticField("I")
    RESULT_OK = JavaStaticField("I")
    RESULT_REQUIRE_APP_PERMISSION = JavaStaticField("I")
    RESULT_REQUIRE_USER_CONSENT = JavaStaticField("I")
    RESULT_RESTRICTED = JavaStaticField("I")
    RESULT_UNAVAILABLE = JavaStaticField("I")
    RESULT_UNSUPPORTED = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getResultCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/service/settings/preferences/SetValueResult$Builder"
        __javaconstructor__ = [("(I)V", False)]
        build = JavaMethod("()Landroid/service/settings/preferences/SetValueResult;")