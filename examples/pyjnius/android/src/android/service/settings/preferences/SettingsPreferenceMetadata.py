from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SettingsPreferenceMetadata"]

class SettingsPreferenceMetadata(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/settings/preferences/SettingsPreferenceMetadata"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    DEEPLINK_ONLY = JavaStaticField("I")
    EXPECT_POST_CONFIRMATION = JavaStaticField("I")
    NO_DIRECT_ACCESS = JavaStaticField("I")
    NO_SENSITIVITY = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getLaunchIntent = JavaMethod("()Landroid/content/Intent;")
    getReadPermissions = JavaMethod("()Ljava/util/List;")
    getScreenKey = JavaMethod("()Ljava/lang/String;")
    getSummary = JavaMethod("()Ljava/lang/String;")
    getWritePermissions = JavaMethod("()Ljava/util/List;")
    getWriteSensitivity = JavaMethod("()I")
    isAvailable = JavaMethod("()Z")
    getKey = JavaMethod("()Ljava/lang/String;")
    isEnabled = JavaMethod("()Z")
    getTitle = JavaMethod("()Ljava/lang/String;")
    getExtras = JavaMethod("()Landroid/os/Bundle;")
    isRestricted = JavaMethod("()Z")
    isWritable = JavaMethod("()Z")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/service/settings/preferences/SettingsPreferenceMetadata$Builder"
        __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;)V", False)]
        setAvailable = JavaMethod("(Z)Landroid/service/settings/preferences/SettingsPreferenceMetadata$Builder;")
        setSummary = JavaMethod("(Ljava/lang/String;)Landroid/service/settings/preferences/SettingsPreferenceMetadata$Builder;")
        setLaunchIntent = JavaMethod("(Landroid/content/Intent;)Landroid/service/settings/preferences/SettingsPreferenceMetadata$Builder;")
        setWritePermissions = JavaMethod("(Ljava/util/List;)Landroid/service/settings/preferences/SettingsPreferenceMetadata$Builder;")
        setWriteSensitivity = JavaMethod("(I)Landroid/service/settings/preferences/SettingsPreferenceMetadata$Builder;")
        setRestricted = JavaMethod("(Z)Landroid/service/settings/preferences/SettingsPreferenceMetadata$Builder;")
        setReadPermissions = JavaMethod("(Ljava/util/List;)Landroid/service/settings/preferences/SettingsPreferenceMetadata$Builder;")
        setExtras = JavaMethod("(Landroid/os/Bundle;)Landroid/service/settings/preferences/SettingsPreferenceMetadata$Builder;")
        setTitle = JavaMethod("(Ljava/lang/String;)Landroid/service/settings/preferences/SettingsPreferenceMetadata$Builder;")
        setEnabled = JavaMethod("(Z)Landroid/service/settings/preferences/SettingsPreferenceMetadata$Builder;")
        build = JavaMethod("()Landroid/service/settings/preferences/SettingsPreferenceMetadata;")
        setWritable = JavaMethod("(Z)Landroid/service/settings/preferences/SettingsPreferenceMetadata$Builder;")