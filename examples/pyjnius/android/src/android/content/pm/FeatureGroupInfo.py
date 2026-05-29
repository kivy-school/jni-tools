from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FeatureGroupInfo"]

class FeatureGroupInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/pm/FeatureGroupInfo"
    __javaconstructor__ = [("()V", False), ("(Landroid/content/pm/FeatureGroupInfo;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    features = JavaField("[Landroid/content/pm/FeatureInfo;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")