from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DirectAction"]

class DirectAction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/DirectAction"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getId = JavaMethod("()Ljava/lang/String;")
    getExtras = JavaMethod("()Landroid/os/Bundle;")
    getLocusId = JavaMethod("()Landroid/content/LocusId;")
    describeContents = JavaMethod("()I")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/DirectAction/Builder"
        __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
        setExtras = JavaMethod("(Landroid/os/Bundle;)Landroid/app/DirectAction$Builder;")
        setLocusId = JavaMethod("(Landroid/content/LocusId;)Landroid/app/DirectAction$Builder;")
        build = JavaMethod("()Landroid/app/DirectAction;")