from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WebTriggerParams"]

class WebTriggerParams(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/measurement/WebTriggerParams"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getRegistrationUri = JavaMethod("()Landroid/net/Uri;")
    isDebugKeyAllowed = JavaMethod("()Z")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/measurement/WebTriggerParams/Builder"
        __javaconstructor__ = [("(Landroid/net/Uri;)V", False)]
        setDebugKeyAllowed = JavaMethod("(Z)Landroid/adservices/measurement/WebTriggerParams$Builder;")
        build = JavaMethod("()Landroid/adservices/measurement/WebTriggerParams;")