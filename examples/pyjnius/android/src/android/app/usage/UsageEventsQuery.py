from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UsageEventsQuery"]

class UsageEventsQuery(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/usage/UsageEventsQuery"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getBeginTimeMillis = JavaMethod("()J")
    getEndTimeMillis = JavaMethod("()J")
    getEventTypes = JavaMethod("()[I")
    getPackageNames = JavaMethod("()Ljava/util/Set;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/usage/UsageEventsQuery$Builder"
        __javaconstructor__ = [("(JJ)V", False)]
        setPackageNames = JavaMethod("([Ljava/lang/String;)Landroid/app/usage/UsageEventsQuery$Builder;", varargs=True)
        setEventTypes = JavaMethod("([I)Landroid/app/usage/UsageEventsQuery$Builder;", varargs=True)
        build = JavaMethod("()Landroid/app/usage/UsageEventsQuery;")