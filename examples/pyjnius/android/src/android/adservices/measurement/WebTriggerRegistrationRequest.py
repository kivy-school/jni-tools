from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WebTriggerRegistrationRequest"]

class WebTriggerRegistrationRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/measurement/WebTriggerRegistrationRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getTriggerParams = JavaMethod("()Ljava/util/List;")
    getDestination = JavaMethod("()Landroid/net/Uri;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/measurement/WebTriggerRegistrationRequest/Builder"
        __javaconstructor__ = [("(Ljava/util/List;Landroid/net/Uri;)V", False)]
        build = JavaMethod("()Landroid/adservices/measurement/WebTriggerRegistrationRequest;")