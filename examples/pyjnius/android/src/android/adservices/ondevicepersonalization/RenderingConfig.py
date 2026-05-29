from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RenderingConfig"]

class RenderingConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/RenderingConfig"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getKeys = JavaMethod("()Ljava/util/List;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/ondevicepersonalization/RenderingConfig$Builder"
        __javaconstructor__ = [("()V", False)]
        build = JavaMethod("()Landroid/adservices/ondevicepersonalization/RenderingConfig;")
        setKeys = JavaMethod("(Ljava/util/List;)Landroid/adservices/ondevicepersonalization/RenderingConfig$Builder;")
        addKey = JavaMethod("(Ljava/lang/String;)Landroid/adservices/ondevicepersonalization/RenderingConfig$Builder;")