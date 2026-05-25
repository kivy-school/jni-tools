from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CustomDescription"]

class CustomDescription(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/autofill/CustomDescription"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/service/autofill/CustomDescription/Builder"
        __javaconstructor__ = [("(Landroid/widget/RemoteViews;)V", False)]
        addChild = JavaMethod("(ILandroid/service/autofill/Transformation;)Landroid/service/autofill/CustomDescription$Builder;")
        batchUpdate = JavaMethod("(Landroid/service/autofill/Validator;Landroid/service/autofill/BatchUpdates;)Landroid/service/autofill/CustomDescription$Builder;")
        addOnClickAction = JavaMethod("(ILandroid/service/autofill/OnClickAction;)Landroid/service/autofill/CustomDescription$Builder;")
        build = JavaMethod("()Landroid/service/autofill/CustomDescription;")