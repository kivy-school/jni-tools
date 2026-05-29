from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BatchUpdates"]

class BatchUpdates(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/autofill/BatchUpdates"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/service/autofill/BatchUpdates$Builder"
        __javaconstructor__ = [("()V", False)]
        transformChild = JavaMethod("(ILandroid/service/autofill/Transformation;)Landroid/service/autofill/BatchUpdates$Builder;")
        updateTemplate = JavaMethod("(Landroid/widget/RemoteViews;)Landroid/service/autofill/BatchUpdates$Builder;")
        build = JavaMethod("()Landroid/service/autofill/BatchUpdates;")