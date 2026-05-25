from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TextClassificationSessionId"]

class TextClassificationSessionId(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/textclassifier/TextClassificationSessionId"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getValue = JavaMethod("()Ljava/lang/String;")