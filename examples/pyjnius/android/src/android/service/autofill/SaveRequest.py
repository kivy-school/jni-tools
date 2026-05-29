from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SaveRequest"]

class SaveRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/autofill/SaveRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getClientState = JavaMethod("()Landroid/os/Bundle;")
    getDatasetIds = JavaMethod("()Ljava/util/List;")
    getFillContexts = JavaMethod("()Ljava/util/List;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")