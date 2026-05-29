from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CapabilityParams"]

class CapabilityParams(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/pm/CapabilityParams"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getAliases = JavaMethod("()Ljava/util/List;")
    getName = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getValue = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/content/pm/CapabilityParams$Builder"
        __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;)V", False)]
        addAlias = JavaMethod("(Ljava/lang/String;)Landroid/content/pm/CapabilityParams$Builder;")
        build = JavaMethod("()Landroid/content/pm/CapabilityParams;")