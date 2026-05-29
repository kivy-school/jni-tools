from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GetValueResult"]

class GetValueResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/settings/preferences/GetValueResult"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    RESULT_DISALLOW = JavaStaticField("I")
    RESULT_INTERNAL_ERROR = JavaStaticField("I")
    RESULT_INVALID_REQUEST = JavaStaticField("I")
    RESULT_OK = JavaStaticField("I")
    RESULT_REQUIRE_APP_PERMISSION = JavaStaticField("I")
    RESULT_UNAVAILABLE = JavaStaticField("I")
    RESULT_UNSUPPORTED = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getResultCode = JavaMethod("()I")
    getValue = JavaMethod("()Landroid/service/settings/preferences/SettingsPreferenceValue;")
    getMetadata = JavaMethod("()Landroid/service/settings/preferences/SettingsPreferenceMetadata;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/service/settings/preferences/GetValueResult$Builder"
        __javaconstructor__ = [("(I)V", False)]
        setValue = JavaMethod("(Landroid/service/settings/preferences/SettingsPreferenceValue;)Landroid/service/settings/preferences/GetValueResult$Builder;")
        build = JavaMethod("()Landroid/service/settings/preferences/GetValueResult;")
        setMetadata = JavaMethod("(Landroid/service/settings/preferences/SettingsPreferenceMetadata;)Landroid/service/settings/preferences/GetValueResult$Builder;")