from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DirectAction"]

class DirectAction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/DirectAction"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getId = JavaMethod("()Ljava/lang/String;")
    getExtras = JavaMethod("()Landroid/os/Bundle;")
    getLocusId = JavaMethod("()Landroid/content/LocusId;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/DirectAction$Builder"
        __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
        setLocusId = JavaMethod("(Landroid/content/LocusId;)Landroid/app/DirectAction$Builder;")
        setExtras = JavaMethod("(Landroid/os/Bundle;)Landroid/app/DirectAction$Builder;")
        build = JavaMethod("()Landroid/app/DirectAction;")