from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UsageEventsQuery"]

class UsageEventsQuery(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/usage/UsageEventsQuery"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getBeginTimeMillis = JavaMethod("()J")
    getEndTimeMillis = JavaMethod("()J")
    getEventTypes = JavaMethod("()[I")
    getPackageNames = JavaMethod("()Ljava/util/Set;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/usage/UsageEventsQuery/Builder"
        __javaconstructor__ = [("(JJ)V", False)]
        build = JavaMethod("()Landroid/app/usage/UsageEventsQuery;")
        setEventTypes = JavaMethod("([I)Landroid/app/usage/UsageEventsQuery$Builder;", varargs=True)
        setPackageNames = JavaMethod("([Ljava/lang/String;)Landroid/app/usage/UsageEventsQuery$Builder;", varargs=True)