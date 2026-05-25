from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SourceRegistrationRequest"]

class SourceRegistrationRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/measurement/SourceRegistrationRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getRegistrationUris = JavaMethod("()Ljava/util/List;")
    getInputEvent = JavaMethod("()Landroid/view/InputEvent;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/measurement/SourceRegistrationRequest/Builder"
        __javaconstructor__ = [("(Ljava/util/List;)V", False)]
        setInputEvent = JavaMethod("(Landroid/view/InputEvent;)Landroid/adservices/measurement/SourceRegistrationRequest$Builder;")
        build = JavaMethod("()Landroid/adservices/measurement/SourceRegistrationRequest;")