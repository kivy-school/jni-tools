from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TableRequest"]

class TableRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/tv/TableRequest"
    __javaconstructor__ = [("(IIIII)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    TABLE_NAME_BAT = JavaStaticField("I")
    TABLE_NAME_CAT = JavaStaticField("I")
    TABLE_NAME_EIT = JavaStaticField("I")
    TABLE_NAME_NIT = JavaStaticField("I")
    TABLE_NAME_PAT = JavaStaticField("I")
    TABLE_NAME_PMT = JavaStaticField("I")
    TABLE_NAME_SDT = JavaStaticField("I")
    TABLE_NAME_SIT = JavaStaticField("I")
    TABLE_NAME_TDT = JavaStaticField("I")
    TABLE_NAME_TOT = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    REQUEST_OPTION_AUTO_UPDATE = JavaStaticField("I")
    REQUEST_OPTION_ONESHOT = JavaStaticField("I")
    REQUEST_OPTION_ONEWAY = JavaStaticField("I")
    REQUEST_OPTION_REPEAT = JavaStaticField("I")
    getTableId = JavaMethod("()I")
    getTableName = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getVersion = JavaMethod("()I")