from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
    getPrecedence = JavaMethod("()I")
    getSessionType = JavaMethod("()I")
    getSscMode = JavaMethod("()I")
    getSliceInfo = JavaMethod("()Ljava/util/List;")
    getDataNetworkName = JavaMethod("()Ljava/util/List;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")