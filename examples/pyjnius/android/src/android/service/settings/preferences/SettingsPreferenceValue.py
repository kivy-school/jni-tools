from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SettingsPreferenceValue"]

class SettingsPreferenceValue(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/settings/preferences/SettingsPreferenceValue"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    TYPE_BOOLEAN = JavaStaticField("I")
    TYPE_DOUBLE = JavaStaticField("I")
    TYPE_INT = JavaStaticField("I")
    TYPE_LONG = JavaStaticField("I")
    TYPE_STRING = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getDoubleValue = JavaMethod("()D")
    getLongValue = JavaMethod("()J")
    getBooleanValue = JavaMethod("()Z")
    getStringValue = JavaMethod("()Ljava/lang/String;")
    getType = JavaMethod("()I")
    getIntValue = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/service/settings/preferences/SettingsPreferenceValue$Builder"
        __javaconstructor__ = [("(I)V", False)]
        setLongValue = JavaMethod("(J)Landroid/service/settings/preferences/SettingsPreferenceValue$Builder;")
        setStringValue = JavaMethod("(Ljava/lang/String;)Landroid/service/settings/preferences/SettingsPreferenceValue$Builder;")
        setBooleanValue = JavaMethod("(Z)Landroid/service/settings/preferences/SettingsPreferenceValue$Builder;")
        setDoubleValue = JavaMethod("(D)Landroid/service/settings/preferences/SettingsPreferenceValue$Builder;")
        setIntValue = JavaMethod("(I)Landroid/service/settings/preferences/SettingsPreferenceValue$Builder;")
        build = JavaMethod("()Landroid/service/settings/preferences/SettingsPreferenceValue;")