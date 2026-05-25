from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ListItem"]

class ListItem(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/pdf/models/ListItem"
    __javaconstructor__ = [("(Ljava/lang/String;Z)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getLabel = JavaMethod("()Ljava/lang/String;")
    isSelected = JavaMethod("()Z")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")