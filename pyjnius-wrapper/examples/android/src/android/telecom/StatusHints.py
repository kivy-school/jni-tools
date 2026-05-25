from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StatusHints"]

class StatusHints(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telecom/StatusHints"
    __javaconstructor__ = [("(Ljava/lang/CharSequence;Landroid/graphics/drawable/Icon;Landroid/os/Bundle;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getLabel = JavaMethod("()Ljava/lang/CharSequence;")
    getIcon = JavaMethod("()Landroid/graphics/drawable/Icon;")
    getExtras = JavaMethod("()Landroid/os/Bundle;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")