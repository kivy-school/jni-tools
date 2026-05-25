from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ChooserResult"]

class ChooserResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/chooser/ChooserResult"
    CHOOSER_RESULT_COPY = JavaStaticField("I")
    CHOOSER_RESULT_EDIT = JavaStaticField("I")
    CHOOSER_RESULT_SELECTED_COMPONENT = JavaStaticField("I")
    CHOOSER_RESULT_UNKNOWN = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getType = JavaMethod("()I")
    getSelectedComponent = JavaMethod("()Landroid/content/ComponentName;")
    isShortcut = JavaMethod("()Z")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")