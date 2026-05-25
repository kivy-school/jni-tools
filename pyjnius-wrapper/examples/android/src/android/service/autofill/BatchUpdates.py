from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BatchUpdates"]

class BatchUpdates(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/autofill/BatchUpdates"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/service/autofill/BatchUpdates/Builder"
        __javaconstructor__ = [("()V", False)]
        updateTemplate = JavaMethod("(Landroid/widget/RemoteViews;)Landroid/service/autofill/BatchUpdates$Builder;")
        transformChild = JavaMethod("(ILandroid/service/autofill/Transformation;)Landroid/service/autofill/BatchUpdates$Builder;")
        build = JavaMethod("()Landroid/service/autofill/BatchUpdates;")