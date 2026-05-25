from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SliceSpec"]

class SliceSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/slice/SliceSpec"
    __javaconstructor__ = [("(Ljava/lang/String;I)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getType = JavaMethod("()Ljava/lang/String;")
    getRevision = JavaMethod("()I")
    canRender = JavaMethod("(Landroid/app/slice/SliceSpec;)Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")