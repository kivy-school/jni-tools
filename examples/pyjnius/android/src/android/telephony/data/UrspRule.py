from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UrspRule"]

class UrspRule(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/data/UrspRule"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getPrecedence = JavaMethod("()I")
    getTrafficDescriptors = JavaMethod("()Ljava/util/List;")
    getRouteSelectionDescriptor = JavaMethod("()Ljava/util/List;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")