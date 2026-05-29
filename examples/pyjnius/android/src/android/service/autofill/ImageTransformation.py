from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ImageTransformation"]

class ImageTransformation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/autofill/ImageTransformation"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/service/autofill/ImageTransformation$Builder"
        __javaconstructor__ = [("(Landroid/view/autofill/AutofillId;Ljava/util/regex/Pattern;I)V", False), ("(Landroid/view/autofill/AutofillId;Ljava/util/regex/Pattern;ILjava/lang/CharSequence;)V", False)]
        addOption = JavaMultipleMethod([("(Ljava/util/regex/Pattern;I)Landroid/service/autofill/ImageTransformation$Builder;", False, False), ("(Ljava/util/regex/Pattern;ILjava/lang/CharSequence;)Landroid/service/autofill/ImageTransformation$Builder;", False, False)])
        build = JavaMethod("()Landroid/service/autofill/ImageTransformation;")