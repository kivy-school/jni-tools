from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WebTriggerRegistrationRequest"]

class WebTriggerRegistrationRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/measurement/WebTriggerRegistrationRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getTriggerParams = JavaMethod("()Ljava/util/List;")
    getDestination = JavaMethod("()Landroid/net/Uri;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/measurement/WebTriggerRegistrationRequest$Builder"
        __javaconstructor__ = [("(Ljava/util/List;Landroid/net/Uri;)V", False)]
        build = JavaMethod("()Landroid/adservices/measurement/WebTriggerRegistrationRequest;")