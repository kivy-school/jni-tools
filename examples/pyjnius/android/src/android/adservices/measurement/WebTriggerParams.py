from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WebTriggerParams"]

class WebTriggerParams(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/measurement/WebTriggerParams"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    isDebugKeyAllowed = JavaMethod("()Z")
    getRegistrationUri = JavaMethod("()Landroid/net/Uri;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/measurement/WebTriggerParams$Builder"
        __javaconstructor__ = [("(Landroid/net/Uri;)V", False)]
        setDebugKeyAllowed = JavaMethod("(Z)Landroid/adservices/measurement/WebTriggerParams$Builder;")
        build = JavaMethod("()Landroid/adservices/measurement/WebTriggerParams;")