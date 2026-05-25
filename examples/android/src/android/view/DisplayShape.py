from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DisplayShape"]

class DisplayShape(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/DisplayShape"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    getPath = JavaMethod("()Landroid/graphics/Path;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")