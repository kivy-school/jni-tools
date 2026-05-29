from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GetValueRequest"]

class GetValueRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/settings/preferences/GetValueRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getScreenKey = JavaMethod("()Ljava/lang/String;")
    getPreferenceKey = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/service/settings/preferences/GetValueRequest$Builder"
        __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;)V", False)]
        build = JavaMethod("()Landroid/service/settings/preferences/GetValueRequest;")