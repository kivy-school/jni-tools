from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PromptContentItemPlainText"]

class PromptContentItemPlainText(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/biometrics/PromptContentItemPlainText"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")