from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AwareResources"]

class AwareResources(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/aware/AwareResources"
    __javaconstructor__ = [("(III)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getAvailableDataPathsCount = JavaMethod("()I")
    getAvailablePublishSessionsCount = JavaMethod("()I")
    getAvailableSubscribeSessionsCount = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")