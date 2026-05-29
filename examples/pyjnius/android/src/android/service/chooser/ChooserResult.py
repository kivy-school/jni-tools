from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ChooserResult"]

class ChooserResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/chooser/ChooserResult"
    CHOOSER_RESULT_COPY = JavaStaticField("I")
    CHOOSER_RESULT_EDIT = JavaStaticField("I")
    CHOOSER_RESULT_SELECTED_COMPONENT = JavaStaticField("I")
    CHOOSER_RESULT_UNKNOWN = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    isShortcut = JavaMethod("()Z")
    getSelectedComponent = JavaMethod("()Landroid/content/ComponentName;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getType = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")