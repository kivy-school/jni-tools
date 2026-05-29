from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AwareResources"]

class AwareResources(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/aware/AwareResources"
    __javaconstructor__ = [("(III)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getAvailableDataPathsCount = JavaMethod("()I")
    getAvailablePublishSessionsCount = JavaMethod("()I")
    getAvailableSubscribeSessionsCount = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")