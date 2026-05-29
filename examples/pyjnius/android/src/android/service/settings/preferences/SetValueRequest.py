from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SetValueRequest"]

class SetValueRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/settings/preferences/SetValueRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getScreenKey = JavaMethod("()Ljava/lang/String;")
    getPreferenceValue = JavaMethod("()Landroid/service/settings/preferences/SettingsPreferenceValue;")
    getPreferenceKey = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/service/settings/preferences/SetValueRequest$Builder"
        __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Landroid/service/settings/preferences/SettingsPreferenceValue;)V", False)]
        build = JavaMethod("()Landroid/service/settings/preferences/SetValueRequest;")