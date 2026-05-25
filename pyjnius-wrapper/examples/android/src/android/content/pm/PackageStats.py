from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PackageStats"]

class PackageStats(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/pm/PackageStats"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Landroid/os/Parcel;)V", False), ("(Landroid/content/pm/PackageStats;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    cacheSize = JavaField("J")
    codeSize = JavaField("J")
    dataSize = JavaField("J")
    externalCacheSize = JavaField("J")
    externalCodeSize = JavaField("J")
    externalDataSize = JavaField("J")
    externalMediaSize = JavaField("J")
    externalObbSize = JavaField("J")
    packageName = JavaField("Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")