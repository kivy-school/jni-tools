from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SaveRequest"]

class SaveRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/autofill/SaveRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getFillContexts = JavaMethod("()Ljava/util/List;")
    getClientState = JavaMethod("()Landroid/os/Bundle;")
    getDatasetIds = JavaMethod("()Ljava/util/List;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")