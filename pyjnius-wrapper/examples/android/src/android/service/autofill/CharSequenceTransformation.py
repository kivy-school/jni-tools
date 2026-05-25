from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CharSequenceTransformation"]

class CharSequenceTransformation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/autofill/CharSequenceTransformation"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/service/autofill/CharSequenceTransformation/Builder"
        __javaconstructor__ = [("(Landroid/view/autofill/AutofillId;Ljava/util/regex/Pattern;Ljava/lang/String;)V", False)]
        addField = JavaMethod("(Landroid/view/autofill/AutofillId;Ljava/util/regex/Pattern;Ljava/lang/String;)Landroid/service/autofill/CharSequenceTransformation$Builder;")
        build = JavaMethod("()Landroid/service/autofill/CharSequenceTransformation;")