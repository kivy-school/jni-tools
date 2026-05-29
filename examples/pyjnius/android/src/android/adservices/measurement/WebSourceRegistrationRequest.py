from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WebSourceRegistrationRequest"]

class WebSourceRegistrationRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/measurement/WebSourceRegistrationRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getWebDestination = JavaMethod("()Landroid/net/Uri;")
    getSourceParams = JavaMethod("()Ljava/util/List;")
    getInputEvent = JavaMethod("()Landroid/view/InputEvent;")
    getAppDestination = JavaMethod("()Landroid/net/Uri;")
    getTopOriginUri = JavaMethod("()Landroid/net/Uri;")
    getVerifiedDestination = JavaMethod("()Landroid/net/Uri;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/measurement/WebSourceRegistrationRequest$Builder"
        __javaconstructor__ = [("(Ljava/util/List;Landroid/net/Uri;)V", False)]
        setInputEvent = JavaMethod("(Landroid/view/InputEvent;)Landroid/adservices/measurement/WebSourceRegistrationRequest$Builder;")
        setAppDestination = JavaMethod("(Landroid/net/Uri;)Landroid/adservices/measurement/WebSourceRegistrationRequest$Builder;")
        setWebDestination = JavaMethod("(Landroid/net/Uri;)Landroid/adservices/measurement/WebSourceRegistrationRequest$Builder;")
        setVerifiedDestination = JavaMethod("(Landroid/net/Uri;)Landroid/adservices/measurement/WebSourceRegistrationRequest$Builder;")
        build = JavaMethod("()Landroid/adservices/measurement/WebSourceRegistrationRequest;")