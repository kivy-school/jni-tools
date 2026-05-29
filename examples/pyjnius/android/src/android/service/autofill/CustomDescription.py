from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CustomDescription"]

class CustomDescription(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/autofill/CustomDescription"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/service/autofill/CustomDescription$Builder"
        __javaconstructor__ = [("(Landroid/widget/RemoteViews;)V", False)]
        addChild = JavaMethod("(ILandroid/service/autofill/Transformation;)Landroid/service/autofill/CustomDescription$Builder;")
        build = JavaMethod("()Landroid/service/autofill/CustomDescription;")
        addOnClickAction = JavaMethod("(ILandroid/service/autofill/OnClickAction;)Landroid/service/autofill/CustomDescription$Builder;")
        batchUpdate = JavaMethod("(Landroid/service/autofill/Validator;Landroid/service/autofill/BatchUpdates;)Landroid/service/autofill/CustomDescription$Builder;")