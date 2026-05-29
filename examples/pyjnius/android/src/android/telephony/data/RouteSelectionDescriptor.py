from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RouteSelectionDescriptor"]

class RouteSelectionDescriptor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/data/RouteSelectionDescriptor"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    ROUTE_SSC_MODE_1 = JavaStaticField("I")
    ROUTE_SSC_MODE_2 = JavaStaticField("I")
    ROUTE_SSC_MODE_3 = JavaStaticField("I")
    SESSION_TYPE_IPV4 = JavaStaticField("I")
    SESSION_TYPE_IPV4V6 = JavaStaticField("I")
    SESSION_TYPE_IPV6 = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getSessionType = JavaMethod("()I")
    getPrecedence = JavaMethod("()I")
    getDataNetworkName = JavaMethod("()Ljava/util/List;")
    getSscMode = JavaMethod("()I")
    getSliceInfo = JavaMethod("()Ljava/util/List;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")