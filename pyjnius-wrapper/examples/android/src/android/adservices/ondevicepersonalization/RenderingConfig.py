from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RenderingConfig"]

class RenderingConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/RenderingConfig"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getKeys = JavaMethod("()Ljava/util/List;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/ondevicepersonalization/RenderingConfig/Builder"
        __javaconstructor__ = [("()V", False)]
        setKeys = JavaMethod("(Ljava/util/List;)Landroid/adservices/ondevicepersonalization/RenderingConfig$Builder;")
        addKey = JavaMethod("(Ljava/lang/String;)Landroid/adservices/ondevicepersonalization/RenderingConfig$Builder;")
        build = JavaMethod("()Landroid/adservices/ondevicepersonalization/RenderingConfig;")