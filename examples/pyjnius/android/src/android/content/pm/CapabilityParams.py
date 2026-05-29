from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CapabilityParams"]

class CapabilityParams(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/pm/CapabilityParams"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getName = JavaMethod("()Ljava/lang/String;")
    getValue = JavaMethod("()Ljava/lang/String;")
    getAliases = JavaMethod("()Ljava/util/List;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/content/pm/CapabilityParams/Builder"
        __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;)V", False)]
        addAlias = JavaMethod("(Ljava/lang/String;)Landroid/content/pm/CapabilityParams$Builder;")
        build = JavaMethod("()Landroid/content/pm/CapabilityParams;")