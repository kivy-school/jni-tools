from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SoundProfile"]

class SoundProfile(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/quality/SoundProfile"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    ERROR_DUPLICATE = JavaStaticField("I")
    ERROR_INVALID_ARGUMENT = JavaStaticField("I")
    ERROR_NOT_ALLOWLISTED = JavaStaticField("I")
    ERROR_NO_PERMISSION = JavaStaticField("I")
    ERROR_UNKNOWN = JavaStaticField("I")
    TYPE_APPLICATION = JavaStaticField("I")
    TYPE_SYSTEM = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getProfileId = JavaMethod("()Ljava/lang/String;")
    getInputId = JavaMethod("()Ljava/lang/String;")
    getProfileType = JavaMethod("()I")
    getName = JavaMethod("()Ljava/lang/String;")
    getPackageName = JavaMethod("()Ljava/lang/String;")
    getParameters = JavaMethod("()Landroid/os/PersistableBundle;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/quality/SoundProfile$Builder"
        __javaconstructor__ = [("(Landroid/media/quality/SoundProfile;)V", False), ("(Ljava/lang/String;)V", False)]
        setParameters = JavaMethod("(Landroid/os/PersistableBundle;)Landroid/media/quality/SoundProfile$Builder;")
        build = JavaMethod("()Landroid/media/quality/SoundProfile;")